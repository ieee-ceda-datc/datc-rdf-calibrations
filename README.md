# DATC RDF Calibrations (2021)

This repository provides calibrations for three basic electrical analyses using publicly-available enablements (NanGate45, SKY130HD, and SKY130HS): 

1. Timer calibration data for static timing analysis
1. RC parasitic calibration data
1. Static IR drop estimation

Our hope is that these calibration datasets will help boost the research community's advancement along the axes of accuracy, turnaround time, and capacity for these fundamental analyses that inform IC physical implementation.

## Contributions

- Thanks to Jagang Lee(POSTECH) for providing all OpenROAD SPNR calibration testcases!
- Thanks to Vidya Chhabria(UMN) for providing the IR drop simulation and JSONs!

## Calibration Data: Overview

PDK        |  Design   |  Init. Util  |  Final Util  |  GP Density  |  Clock Period[ns]  |  WNS[ns]  |  Effective Clock Period[ns]  |  Total WireLength[um]
-----------|-----------|--------------|--------------|--------------|--------------------|-----------|------------------------------|----------------------
nangate45  |  [aes_1](calibration/nangate45/aes_cipher_top)    |  21          |  22          |  0.6         |  0.8109            |  -0.145   |  0.956                       |  458260
nangate45  |  [aes_2](calibration/nangate45/aes_cipher_top)    |  14          |  15          |  0.65        |  0.8109            |  -0.16    |  0.971                       |  455773
nangate45  |  [aes_3](calibration/nangate45/aes_cipher_top)    |  23          |  25          |  0.7         |  0.8109            |  -0.138   |  0.949                       |  439631
nangate45  |  [gcd_1](calibration/nangate45/gcd)    |  20          |  24          |  0.6         |  0.4574            |  -0.035   |  0.492                       |  4383
nangate45  |  [gcd_2](calibration/nangate45/gcd)    |  15          |  18          |  0.65        |  0.4574            |  -0.017   |  0.474                       |  4474
nangate45  |  [gcd_3](calibration/nangate45/gcd)    |  25          |  30          |  0.7         |  0.4574            |  -0.022   |  0.479                       |  3983
nangate45  |  [jpeg_1](calibration/nangate45/jpeg_encoder)   |  20          |  21          |  0.6         |  1.9775            |  0.133    |  1.845                       |  709239
nangate45  |  [jpeg_2](calibration/nangate45/jpeg_encoder)   |  15          |  15          |  0.65        |  1.9775            |  0.074    |  1.904                       |  688885
nangate45  |  [jpeg_3](calibration/nangate45/jpeg_encoder)   |  25          |  26          |  0.7         |  1.9775            |  0.143    |  1.835                       |  665946
nangate45  |  [ibex_1](calibration/nangate45/ibex_core)   |  19          |  21          |  0.6         |  5.3433            |  1.832    |  3.511                       |  362275
nangate45  |  [ibex_2](calibration/nangate45/ibex_core)   |  14          |  16          |  0.65        |  5.3433            |  1.885    |  3.458                       |  360671
nangate45  |  [ibex_3](calibration/nangate45/ibex_core)   |  24          |  26          |  0.7         |  5.3433            |  1.861    |  3.482                       |  339120
nangate45  |  [swerv_1](calibration/nangate45/swerv)  |  19          |  22          |  0.45        |  3.4012            |  -0.447   |  3.848                       |  4179350
nangate45  |  [swerv_2](calibration/nangate45/swerv)  |  14          |  17          |  0.5         |  3.4012            |  -0.288   |  3.689                       |  4224750
nangate45  |  [swerv_3](calibration/nangate45/swerv)  |  16          |  18          |  0.55        |  3.4012            |  -0.686   |  4.087                       |  4506998
sky130hd   |  [aes_1](calibration/sky130hd/aes_cipher_top)    |  14          |  23          |  0.6         |  3.7439            |  -1.059   |  4.803                       |  1391315
sky130hd   |  [aes_2](calibration/sky130hd/aes_cipher_top)    |  10          |  16          |  0.65        |  3.7439            |  -1.478   |  5.222                       |  1408681
sky130hd   |  [aes_3](calibration/sky130hd/aes_cipher_top)    |  19          |  29          |  0.7         |  3.7439            |  -1.047   |  4.791                       |  1308739
sky130hd   |  [gcd_1](calibration/sky130hd/gcd)    |  19          |  30          |  0.6         |  4.3647            |  -0.409   |  4.774                       |  8590
sky130hd   |  [gcd_2](calibration/sky130hd/gcd)     |  15          |  21          |  0.65        |  4.3647            |  -0.247   |  4.612                       |  8441
sky130hd   |  [gcd_3](calibration/sky130hd/gcd)     |  24          |  34          |  0.7         |  4.3647            |  -0.377   |  4.742                       |  7871
sky130hd   |  [jpeg_1](calibration/sky130hd/jpeg_encoder)    |  20          |  23          |  0.6         |  8.087             |  -2.066   |  10.153                      |  1593695
sky130hd   |  [jpeg_2](calibration/sky130hd/jpeg_encoder)   |  15          |  17          |  0.65        |  8.087             |  -2.262   |  10.349                      |  1555760
sky130hd   |  [jpeg_3](calibration/sky130hd/jpeg_encoder)   |  25          |  28          |  0.7         |  8.087             |  -1.846   |  9.933                       |  1523968
sky130hd   |  [ibex_1](calibration/sky130hd/ibex_core)   |  19          |  35          |  0.45        |  15.155            |  -3.521   |  18.676                      |  1080702
sky130hd   |  [ibex_2](calibration/sky130hd/ibex_core)   |  17          |  31          |  0.5         |  15.155            |  -3.925   |  19.08                       |  1052423
sky130hd   |  [ibex_3](calibration/sky130hd/ibex_core)   |  15          |  26          |  0.55        |  15.155            |  -3.18    |  18.335                      |  1006384
sky130hs   |  [aes_1](calibration/sky130hs/aes_cipher_top)    |  14          |  25          |  0.6         |  2.8113            |  -0.97    |  3.781                       |  1443899
sky130hs   |  [aes_2](calibration/sky130hs/aes_cipher_top)    |  10          |  17          |  0.65        |  2.8113            |  -1.148   |  3.959                       |  1456477
sky130hs   |  [aes_3](calibration/sky130hs/aes_cipher_top)     |  19          |  33          |  0.7         |  2.8113            |  -0.895   |  3.706                       |  1368246
sky130hs   |  [gcd_1](calibration/sky130hs/gcd)    |  20          |  27          |  0.6         |  1.7798            |  -0.057   |  1.837                       |  10462
sky130hs   |  [gcd_2](calibration/sky130hs/gcd)    |  15          |  21          |  0.65        |  1.7798            |  -0.094   |  1.874                       |  10845
sky130hs   |  [gcd_3](calibration/sky130hs/gcd)    |  25          |  32          |  0.7         |  1.7798            |  -0.11    |  1.89                        |  9858
sky130hs   |  [jpeg_1](calibration/sky130hs/jpeg_encoder)   |  20          |  24          |  0.6         |  6.3874            |  -0.688   |  7.075                       |  2073532
sky130hs   |  [jpeg_2](calibration/sky130hs/jpeg_encoder)   |  15          |  18          |  0.65        |  6.3874            |  -1.137   |  7.524                       |  2024417
sky130hs   |  [jpeg_3](calibration/sky130hs/jpeg_encoder)   |  25          |  29          |  0.7         |  6.3874            |  -1.16    |  7.547                       |  1973860
sky130hs   |  [ibex_1](calibration/sky130hs/ibex_core)   |  19          |  33          |  0.45        |  11.2897           |  -2.71    |  14                          |  1397685
sky130hs   |  [ibex_2](calibration/sky130hs/ibex_core)    |  17          |  30          |  0.5         |  11.2897           |  -3.639   |  14.929                      |  1420173
sky130hs   |  [ibex_3](calibration/sky130hs/ibex_core)    |  15          |  26          |  0.55        |  11.2897           |  -2.579   |  13.869                      |  1339622

Each calibration data consists of the following files:

* Timing and RCX calibrations:
  - `*.def`: DRV-free routed DEF using [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts).
  - `*.v`: Verilog from routed DEF.
  - `*.sdc`: Timing constraint file. Contains clock periods.
  - `*.spef`: SPEF file from routed DEF.
  - `*5_worst.json`: Top 5 worst timing paths from timing report.
  - `*5_worst.json.rpt` : Top 5 worst timing report as OpenSTA format.
  - `*endpoint_slacks.json`: Endpoints slack from timing report.

* IR drop calibration:
  - `*_ir.[VDD/VSS].json`: Per-instance static IR drop.
  - `*.vsrc.json`: VDD and VSS Voltage source location files.

## Timer Calibration Data

Our initial data compilation uses four DRV-free routed DEFs produced by the OpenROAD flow: `aes_cipher_top` and `jpeg_encoder` designs, in each of the SKY130 and NanGate45 enablements. Golden calibration data is abstracted and anonymized using a 5-worst JSON format, which we use to hold block-level worst (negative) slack, total negative slack, and number of failing endpoints (i.e., standard WNS, TNS and FEP metrics), along with detailed information for the top-5 worst timing paths (including arc delays and pin arrival times). We provide a timing report viewer that reads 5-worst JSON-formatted data and prints out a timing report in the OpenSTA tool's report format. To facilitate other calibrations of interest, we also propose an endpoints JSON format, which can capture setup slack values at every flip-flop D pin. We can compare the endpoint slacks from OpenSTA with calibration endpoint slack values.


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
The static IR drop calibration data is currently availble for the SKY130 enablement. Golden data static IR drop data is anonymized and made availble on a per instance basis for `aes_cipher_top` and the `jpeg_encoder` in a JSON format. The location of voltage sources using which these golden per instance IR drop values are obtained are also anonymized and reported in a JSON format. **The IR drop calibration numbers are obtained using the same `.def`, `.v`, `.sdc`, and `.spef` as the timing calibration results.**

### JSON Format Description

The golden IR drop reports are anonymized in the JSON format described below:

#### File: \<design_name\>.\<vdd/vss\>.ir.json

There are two sections in this file:

- a summary section: lists the design_name, technology, voltage values, timing corner, and a summary of the worstcase IR drop in the "wir" section. The wir section has the worstcase static IR drop value, the metal layer on which it occurs, and the instance name with the worstcase IR drop.
- a detail section: provides a list of instances in the design alson with its corresponding voltage values.

Example of the summary and detail section of the JSON is shown below:


```json
{ "summary": {
    "design": design_name,
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
    },
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
  },
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

### Further Resources

In an effort to drive PDN analysis and synthesis research, the following repository contains PDN benchmarks in SPICE format (similar to the [IBM PG benchmarks](https://web.ece.ucsb.edu/~lip/PGBenchmarks/ibmpgbench.html) in a 45nm technology with opensource designs using both OpenROAD flow and commercial tools. In addition, in an attempt to generate a larger benchmark set for ML calibrations,  the repo also contains 10 synthetic current maps generated by GANs (BeGAN benchmarks). These benchmarks maintain characteristic traits of real current maps while being sufficiently different: https://github.com/PDN-BeGAN/BeGAN-benchmarks


## Citation

 Please cite the following paper
 
- J. Chen, I. H.-R. Jiang, J. Jung, A. B. Kahng, V. N. Kravets, Y.-L. Li, S.-T. Lin and M. Woo, "DATC RDF-2020: Strengthening the Foundation for Academic Research in IC Physical Design", Proc. IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2020. (Invited)
- J. Chen, I. H.-R. Jiang, J. Jung, A. B. Kahng, S. Kim, V. N. Kravets, Y.-L. Li, R. Varadarajan and M. Woo, "DATC RDF-2021: Design Flow and Beyond", Proc. ACM/IEEE International Conference on Computer-Aided Design (ICCAD), 2021. (Invited)


