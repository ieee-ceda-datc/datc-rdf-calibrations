import re
import sys
import json
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import griddata

def create_ir_map(def_data):
    x = []
    y = []
    volt = []
    for inst_name, details in def_data['instances'].items():
        try:
            v= details['voltage']
            x.append(details['ll_x'])
            y.append(details['ll_y'])
            volt.append(v)
        except KeyError:
            pass
    xmin = min(x)
    xmax=max(x)
    ymin = min(y)
    ymax=max(y)
    grid_x, grid_y = np.mgrid[xmin:xmax:1000j, ymin:ymax:1000j]
    zi = griddata((x,y), volt,(grid_x, grid_y) , method='linear')
    plt.figure()
    plt.imshow(zi,cmap='jet',extent=[xmin,xmax,ymin,ymax],
           origin="lower")
    cb=plt.colorbar(shrink=0.75)
    cb.set_label('Voltage(V)')
    
    plt.show()

def read_def(def_file):
    print('Reading DEF file ')
    def_data = {}
    def_data['instances'] = {}
    with open(def_file) as f:
        components = 0
        count = 0
        comp_syn = 0
        cur_key = ""
        for line in f:
            if re.match(r'^[\t ]*UNITS', line, flags=re.IGNORECASE):
                data = re.findall(r'[\d]+', line)
                def_data['units_per_micron'] = int(data[0])
            if re.match(r'^[\t ]*COMPONENTS \d+', line, flags=re.IGNORECASE):
                components = 1
            if re.match(r'^[\t ]*END COMPONENTS', line, flags=re.IGNORECASE):
                components = 0
            if components == 1:
                if re.match(r'^\s*-\s+[\w/\.]+\s+\w+', line):
                    data = re.findall(r'[\w\./]+', line)
                    cur_key = data[0].strip()
                    cell = data[1].strip()
                    comp_syn = 1
                    def_data['instances'][cur_key] = {}
                    def_data['instances'][cur_key]['cell'] = cell
                if re.match(
                        r'^[\t ]*;', line
                ) and comp_syn == 1:    #semicolon at the begining of the line
                    comp_syn = 0
                    cur_key = ""

                if re.search(r'PLACED|FIXED|COVER', line,
                             flags=re.IGNORECASE) and comp_syn == 1:
                    for m in re.finditer(r'PLACED|FIXED|COVER', line):
                        loc = m.start()
                        data = re.findall(r'[\w]+', line[loc:])
                        def_data['instances'][cur_key]['ll_x'] = int(data[1]) / def_data['units_per_micron']
                        def_data['instances'][cur_key]['ll_y'] = int(data[2]) / def_data['units_per_micron']
                if (re.search(';', line)
                        and comp_syn == 1):    #semicolon at the end of the line
                    comp_syn = 0
                    cur_key = ""

    return def_data

def read_json(json_file, def_data):
    print('Reading JSON file ')
    with open(json_file) as file_json:
        ir_inst = json.loads(file_json.read())
    ir_inst = ir_inst['detail']
    ir_inst_list = ir_inst['instanceList']
    volt_list = ir_inst['voltages']
    for i in range(len(ir_inst_list)):
        def_data['instances'][ir_inst_list[i]]['voltage'] = volt_list[i]
    return def_data

def main():
    if len(sys.argv) != 3:
        print("ERROR Insufficient arguments")
        print(
            "Enter the full path names of the DEF file and json files")
        print(" Example: python3 IRdrop_plot.pt <def_file> <json_rpt>")
        sys.exit(-1)
    def_file = sys.argv[1]
    json_file = sys.argv[2]
    def_data = {}
    def_data = read_def(def_file)
    def_data = read_json(json_file, def_data)
    create_ir_map(def_data)

main()
