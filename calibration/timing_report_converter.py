# 5-worst json to OSTA timing report converter
# written by mgwoo (20.11.05)

import json
import sys 

def PrintTimingReport(jsonDict):
    print("=========================================================")
    sDict = jsonDict["summary"]
    print("      Summary ") 
    print("=========================================================")
    print("WNS:", sDict["WNS"])
    print("TNS:", sDict["TNS"])
    print("FEP:", sDict["FEP"])
    print(" ")
    dDict = jsonDict["detail"]
 
    # print from Top1 to Top5
    for i in range(1,6):
        PrintTimingPathReport(dDict, "top" + str(i))

def PrintTimingPathReport(dDict, key): 
    if key in dDict == False:
        return
    
    print("---------------------------------------------------------")
    print("  %s worst timing path " %(key))
    print("---------------------------------------------------------")

    pDict = dDict[key]
    pathArrivalTime = float(pDict["pathAAT"])
    print( "Startpoint: %s (%s)" %(pDict["startPoint"], pDict["startPointStatus"]))
    print( "Endpoint: %s (%s)" %(pDict["endPoint"], pDict["endPointStatus"]))
    print( "Path Group: %s" %(pDict["pathGroup"]))
    print("")
    print("  Delay    Time   Description")
    print("---------------------------------------------------------")
    plDict = pDict["pathList"]
    for path in plDict:
        delay = 0.0 if path["delay"] == "" else float(path["delay"])
        aat = 0.0 if path["AAT"] == "" else float(path["AAT"])
        rfStr = "^" if path["status"] == "Rising" else "v" if path["status"] == "Falling" else ""
        masterStr = "" if path["masterType"] == "" else "(%s)" %(path["masterType"])
        print( "%7.02f %7.02f %s %s %s" % (delay, 
            aat, rfStr, path["pin"], masterStr ) )

    print("        %7.02f   data arrival time" % (pathArrivalTime) )
    print("")

    cplDict = pDict["clockPathList"]
    clk = float(pDict["clockPeriod"])
    setupTime = -1 * float(pDict["setupTime"])
    for path in cplDict:
        delay = 0.0 if path["delay"] == "" else float(path["delay"])
        aat = 0.0 if path["AAT"] == "" else float(path["AAT"])
        rfStr = "^" if path["status"] == "Rising" else "v" if path["status"] == "Falling" else ""
        masterStr = "" if path["masterType"] == "" else "(%s)" %(path["masterType"])
        print( "%7.02f %7.02f %s %s %s" % (delay, 
            clk + aat, rfStr, path["pin"], masterStr ) )
    
    print("%7.02f %7.02f   library setup time" % (setupTime, setupTime + clk + aat))
    print("        %7.02f   data required time" % (setupTime + clk + aat))
    print("---------------------------------------------------------")
    print("        %7.02f   data required time" % (setupTime + clk + aat))
    print("        %7.02f   data arrival time" % (pathArrivalTime))
    print("---------------------------------------------------------")
    slackVar = setupTime + clk + aat - pathArrivalTime
    slackString = "MET" if slackVar >= 0.0 else "VIOLATED"
    print("        %7.02f   slack (%s)" % (slackVar, slackString) )
    print("")


def main():
    print("Input JSON:" + sys.argv[1])
    f = open(sys.argv[1], 'r')
    cont = f.read()
    f.close()
    jsonDict = json.loads(cont)
    
    PrintTimingReport(jsonDict)

if __name__ == "__main__":  
    main()
