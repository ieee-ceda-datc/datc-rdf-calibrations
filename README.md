# DATC RDF Calibrations

This repository provides calibrations for two basic electrical analyses, parasitic estimation and static timing analysis, using publicly-available enablements (NanGate45, SKY130). Our hope is that these calibration datasets will help boost the research community's advancement along the axes of accuracy, turnaround time, and capacity for these fundamental analyses that inform IC physical implementation. 

## Timer Calibration Data 

Our initial data compilation uses four DRV-free routed DEFs produced by the OpenROAD flow: `aes_cipher_top` and `jpeg_encoder` designs, in each of the SKY130 and NanGate45 enablements. Golden calibration data is abstracted and anonymized using a 5-worst JSON format, which we use to hold block-level worst (negative) slack, total negative slack, and number of failing endpoints (i.e., standard WNS, TNS and FEP metrics), along with detailed information for the top-5 worst timing paths (including arc delays and pin arrival times). We provide a timing report viewer that reads 5-worst JSON-formatted data and prints out a timing report in the OpenSTA tool's report format. To facilitate other calibrations of interest, we also propose an endpoints JSON format, which can capture setup slack values at every flip-flop D pin. We can compare the endpoint slacks from OpenSTA with calibration endpoint slack values. 

### JSON Format Description
#### 5 Worst JSON
- Contains the following

  - Block-level worst (negative) slack (WNS)
  - Block-level total negative slack (TNS)
  - Block-level number of failing endpoints (FEP)
  - Detailed information for the top-5 worst timing paths (including arc delays and pin arrival times)

 
- Example

      {
        "summary": {
        "WNS": "-0.230",
        "TNS": "-10.560",
        "FEP": "139",
        "tech": "freepdk45",
        "design": "aes_cipher_top"
      },
      "detail": {
        "top1": {
          "endPoint": "_28884_/D",
          "endPointStatus": "Rising",
          "startPoint": "_28827_/Q",
          "startPointStatus": "Falling",
          "pathGroup": "reg2reg",
          "setupTime": "0.039",
          "clockPeriod": "1.000",
          "pathRAT": "1.310",
          "pathAAT": "1.541",
          "slack": "-0.230",
          "pathList": [
          {
            "pin": "clk",
            "status": "Rising",
            "net": "clk",
            "masterType": "",
            "delay": "",
            "AAT": "0.000"
          },
          {
            "pin": "clkbuf_0_clk/A",
            "status": "Rising",
            "net": "clk",
            "masterType": "BUF_X4",
            "delay": "0.009",
            "AAT": "0.009"
          },
          ...
          
  - __summary__: summary of the given design

    - __WNS__: Block-level worst (negative) slack (WNS)
    - __TNS__: Block-level total negative slack (TNS)
    - __FEP__: Block-level number of failing endpoints (FEP)
    - __tech__: Technology
    - __design__: Design name

  - __detail__: Detailed information for the top-5 worst timing paths

    - __topN__ : N-th path (N: 1~5)
      - __endPoint__: Endpoint. InstanceName + "/" + PinName
      - __endPointStatus__: Endpoint status. `Rising` or `Falling`
      - __startPoint__: Startpoint. InstanceName + "/" + PinName
      - __startPointStatus__: Startpoint status. `Rising` or `Falling`      
      - __pathGroup__: Path group. `reg2reg` 
      - __setupTime__: Setup time
      
      - __clockPeriod__: Clock period
      - __pathRAT__: Path Required Arrival Time(RAT)
      - __pathAAT__: Path Actual Arrival Time(AAT)
      - __slack__: Slack in current path
      
      - __pathList__: Detailed path list
 
      
        - __pin__: pin. InstanceName + "/" + PinName
        - __status__: Pin status. `Rising` or `Falling`,
        - __net__: Net where Pin is Located
        - __masterType__: Master Cell Where Pin is Located
        - __delay__: Delay 
        - __AAT__: Actual Arrival Time(AAT) in Pin
          
#### 5 Worst Json Timing Report Converter

- Timing report viewer [[link](calibration/timing_report_converter.py)]

  - Takes __5 Worst JSON__ and print out a timing report as [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA) style

  - Example usage
    
        python3 timing_report_converter.py aes_cipher_top_5_worst.json
    
  - Example output
  
        =========================================================
              Summary
        =========================================================
        WNS: -0.230
        TNS: -10.560
        FEP: 139
        
        ---------------------------------------------------------
          top1 worst timing path
        ---------------------------------------------------------
        Startpoint: _28827_/Q (Falling)
        Endpoint: _28884_/D (Rising)
        Path Group: reg2reg
        
          Delay    Time   Description
        ---------------------------------------------------------
           0.00    0.00 ^ clk
           0.01    0.01 ^ clkbuf_0_clk/A (BUF_X4)
           0.03    0.04 ^ clkbuf_0_clk/Z (BUF_X4)
           0.00    0.04 ^ clkbuf_1_0_0_clk/A (CLKBUF_X1)
           0.04    0.07 ^ clkbuf_1_0_0_clk/Z (CLKBUF_X1)
           0.00    0.07 ^ clkbuf_1_0_1_clk/A (CLKBUF_X1)
           0.06    0.13 ^ clkbuf_1_0_1_clk/Z (CLKBUF_X1)
        
        ...
        

#### Endpoints Slack JSON
- Contains setup slack values at every flip-flop D pin
  
- Example

       "tech": "freepdk45",
        "design": "aes_cipher_top",
        "pins": [
          "_28572_/D",
          "_28573_/D",
          ...
         ],
        "slacks": [
          "0.648",
          "0.731",
          ...
        ]


  - __tech__: Technology
  - __design__: Design name
  - __pins__: Endpoints pin lists
  - __slacks__: Corresponding endpoints slacks 
  

## RCX Calibration Data
RCX calibration data is also provided as Standard Parasitic Exchange Format (SPEF) in each testcases.

## Static IR Drop Calibration Data
TBA

## File Link and Description

### Technology
* [SKY130](calibration/sky130)

  - [aes.tgz](calibration/sky130/aes.tgz): Timing and RCX calibrations archive for `aes_cipher_top` design.
  - [aes_ir.tgz](calibration/sky130/aes_ir.tgz): Static IR drop calibration archive for `aes_cipher_top` design.
  - [jpeg.tgz](calibration/sky130/jpeg.tgz): Timing and RCX calibrations archive for `jpeg_encoder` design.
  - [jpeg_ir.tgz](calibration/sky130/jpeg_ir.tgz): Static IR drop calibration archive for `jpeg_encoder` design.


* [NanGate45](calibration/NanGate45)

  - [aes.tgz](calibration/NanGate45/aes.tgz): Timing and RCX calibrations archive for `aes_cipher_top` design.
  - [jpeg.tgz](calibration/NanGate45/jpeg.tgz): Timing and RCX calibrations archive for `jpeg_encoder` design.

### Detailed Description
- Timing and RCX calibrations archive:

  * __\*.def__: DRV-free routed DEF using [OpenROAD-flow](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts).
  * __\*.v__: Verilog from routed DEF.
  * __\*.sdc__: Timing constraint file. Contains clock periods. 
  * __\*.spef__: SPEF file from routed DEF.
  * __\*5_worst.json__: Top 5 worst timing paths from timing report.
  * __\*endpoint_slacks.json__: Endpoints slack from timing report.


