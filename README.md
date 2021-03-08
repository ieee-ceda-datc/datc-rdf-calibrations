# DATC RDF Calibrations

This repository provides calibrations for three basic electrical analyses: (1)parasitic estimation, (2) static timing analysis, and (3) static IR drop estimation using publicly-available enablements (NanGate45, SKY130). Our hope is that these calibration datasets will help boost the research community's advancement along the axes of accuracy, turnaround time, and capacity for these fundamental analyses that inform IC physical implementation.

## Timer Calibration Data

Our initial data compilation uses four DRV-free routed DEFs produced by the OpenROAD flow: `aes_cipher_top` and `jpeg_encoder` designs, in each of the SKY130 and NanGate45 enablements. Golden calibration data is abstracted and anonymized using a 5-worst JSON format, which we use to hold block-level worst (negative) slack, total negative slack, and number of failing endpoints (i.e., standard WNS, TNS and FEP metrics), along with detailed information for the top-5 worst timing paths (including arc delays and pin arrival times). We provide a timing report viewer that reads 5-worst JSON-formatted data and prints out a timing report in the OpenSTA tool's report format. To facilitate other calibrations of interest, we also propose an endpoints JSON format, which can capture setup slack values at every flip-flop D pin. We can compare the endpoint slacks from OpenSTA with calibration endpoint slack values.


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

  * `*.def`: DRV-free routed DEF using [OpenROAD-flow](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts).
  * `*.v`: Verilog from routed DEF.
  * `*.sdc`: Timing constraint file. Contains clock periods.
  * `*.spef`: SPEF file from routed DEF.
  * `*5_worst.json`: Top 5 worst timing paths from timing report.
  * `*endpoint_slacks.json`: Endpoints slack from timing report.

- IR drop calibration archive:

  * `*.<vdd/vss>.json`: Per-instance static IR drop.
  * `*.vsrc.json`: VDD and VSS Voltage source location files.


### JSON Format Description

#### 5 Worst JSON

* Contains the following
  - Block-level worst (negative) slack (WNS)
  - Block-level total negative slack (TNS)
  - Block-level number of failing endpoints (FEP)
  - Detailed information for the top-5 worst timing paths (including arc delays and pin arrival times)

* Example
    ```json
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
    ```

  - `summary`: summary of the given design
    - `WNS`: Block-level worst (negative) slack (WNS)
    - `TNS`: Block-level total negative slack (TNS)
    - `FEP`: Block-level number of failing endpoints (FEP)
    - `tech`: Technology
    - `design`: Design name
  - `detail`: Detailed information for the top-5 worst timing paths
    - `topN` : N-th path (N: 1~5)
      - `endPoint`: Endpoint. InstanceName + "/" + PinName
      - `endPointStatus`: Endpoint status. `Rising` or `Falling`
      - `startPoint`: Startpoint. InstanceName + "/" + PinName
      - `startPointStatus`: Startpoint status. `Rising` or `Falling`
      - `pathGroup`: Path group. `reg2reg`
      - `setupTime`: Setup time
      - `clockPeriod`: Clock period
      - `pathRAT`: Path Required Arrival Time(RAT)
      - `pathAAT`: Path Actual Arrival Time(AAT)
      - `slack`: Slack in current path
      - `pathList`: Detailed path list
        - `pin`: pin. InstanceName + "/" + PinName
        - `status`: Pin status. `Rising` or `Falling`,
        - `net`: Net where Pin is Located
        - `masterType`: Master Cell Where Pin is Located
        - `delay`: Delay
        - `AAT`: Actual Arrival Time(AAT) in Pin

#### 5 Worst JSON Timing Report Converter

- Timing report viewer [[link](calibration/timing_report_converter.py)]
  - Takes __5 Worst JSON__ and print out a timing report as [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA) style
  - Example usage
    ```bash
        python3 timing_report_converter.py aes_cipher_top_5_worst.json
     ```

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
-
    ```json
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
    ```

  - `tech`: Technology
  - `design`: Design name
  - `pins`: Endpoints pin lists
  - `slacks`: Corresponding endpoints slacks


## RCX Calibration Data
RCX calibration data is also provided as Standard Parasitic Exchange Format (SPEF) in each testcases.

## Static IR Drop Calibration Data
The static IR drop calibration data is currently availble for the SKY130 enablement. Golden data static IR drop data is anonymized and made availble on a per instance basis for 'aes_cipher_top' and the 'jpeg_encoder' in a JSON format. The location of voltage sources using which these golden per instance IR drop values are obtained are also anonymized and reported in a JSON format. **The IR drop calibration numbers are obtained using the same .def, .v, .sdc, and .spef as the timing calibration results.**


### JSON Format Description

The golden IR drop reports are anonymized in the JSON format described below:

#### File: \<design_name\>.\<vdd/vss\>.ir.json

There are two sections in this file:

- a summary section: lists the design_name, technology, voltage values, timing corner, and a summary of the worstcase IR drop in the "wir" section. The wir section has the worstcase static IR drop value, the metal layer on which it occurs, and the instance name with the worstcase IR drop.
- a detail section: provides a list of instances in the design alson with its corresponding voltage values.

Example of the summary and detail section of the JSON is shown below:


```json
{ "summary": {
    "design": desing_name,
    "powerNet": net_name,
    "tech": ,
    "timingCorner": "tt_025C_1v80",
    "vdd": 1.8000,
    "vss": 0,
    "wir": {
      "instanceName": "_28766_",
      "ir": 0.0310,
      "layer": "met1",
      "voltage": 1.7690
    }
"detail": {
    "instanceList": ["_28766_", "FILLER_170_1364", "FILLER_170_1362", "FILLER_170_1358"],
    "voltages": [1.7690, 1.7690, 1.7691, 1.7691]
    }
}
```


#### File: \<design\>.vsrc.json

This is an input file which is necessary for static IR drop analysis. It contains the location of the voltage sources both VDD and VSS. The JSON described below creates an anonymized representation for specifying these inputs. It consists of two sections a summary and detailed sections
- summary section: lists design name, number of VDD and VSS voltage sources, the topmost metal layer on which these voltage sources are attached to, and the technology.
- detail section: provides details of the name of the voltage source, its type (either VDD/VSS) and its location.

Example of this file is shown below:

```json
 { "summary": {
    "design": design_name,
    "numVddSrcs": 1,
    "numVssSrcs": 1,
    "tech": "sky130",
    "vdd": 1.8,
    "voltageSrcMetalLayer": "met4",
    "vss": 0
  }
    "detail": {
    "voltageSrcList": [
      {
        "type": "VDD",
        "voltageSrcName": "VDD100",
        "xLocation": 12.0,
        "yLocation": 12.0
      },
      {
        "type": "VSS",
        "voltageSrcName": "VSS101",
        "xLocation": 544.0,
        "yLocation": 12.0
      }
    }
}
```



## Citation
 Please cite the following paper

- J. Chen, I. H.-R. Jiang, J. Jung, A. B. Kahng, V. N. Kravets, Y.-L. Li, S.-T. Lin and M. Woo, "DATC RDF-2020: Strengthening the Foundation for Academic Research in IC Physical Design", Proc. IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2020. (Invited)


