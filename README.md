# DATC RDF Calibrations

This repository provides calibrations for two basic electrical analyses, parasitic estimation and static timing analysis, using publicly-available enablements (NanGate45, SKY130). Our hope is that these calibration datasets will help boost the research community's advancement along the axes of accuracy, turnaround time, and capacity for these fundamental analyses that inform IC physical implementation. 

## Timer Calibration Data 

Our initial data compilation uses four DRV-free routed DEFs produced by the OpenROAD flow: `aes_cipher_top` and `jpeg_encoder` designs, in each of the SKY130 and NanGate45 enablements. Golden calibration data is abstracted and anonymized using a 5-worst JSON format, which we use to hold block-level worst (negative) slack, total negative slack, and number of failing endpoints (i.e., standard WNS, TNS and FEP metrics), along with detailed information for the top-5 worst timing paths (including arc delays and pin arrival times). We provide a timing report viewer that reads 5-worst JSON-formatted data and prints out a timing report in the OpenSTA tool's report format. To facilitate other calibrations of interest, we also propose an endpoints JSON format, which can capture setup slack values at every flip-flop D pin. We can compare the endpoint slacks from OpenSTA with calibration endpoint slack values. 

### JSON Format Description
#### 5 Worst JSON


#### Endpoints Slack JSON



## RCX Calibration Data
RCX calibration data is also provided as Standard Parasitic Exchange Format (SPEF) in each testcases.

## Static IR Drop Calibration Data
TBA

## File Link and Description

### Technology
* [SKY130](calibration/sky130)

  - [aes.tgz](calibration/sky130/aes.tgz): Timing and RCX calibrations archive for *aes_cipher_top* design.
  - [aes_ir.tgz](calibration/sky130/aes_ir.tgz): Static IR drop calibration archive for *aes_cipher_top* design.
  - [jpeg.tgz](calibration/sky130/jpeg.tgz): Timing and RCX calibrations archive for *jpeg_encoder* design.
  - [jpeg_ir.tgz](calibration/sky130/jpeg_ir.tgz): Static IR drop calibration archive for *jpeg_encoder* design.


* [NanGate45](calibration/NanGate45)

  - [aes.tgz](calibration/NanGate45/aes.tgz): Timing and RCX calibrations archive for *aes_cipher_top* design.
  - [jpeg.tgz](calibration/NanGate45/jpeg.tgz): Timing and RCX calibrations archive for *jpeg_encoder* design.

### Detailed Description
- Timing and RCX calibrations archive:

  * __def__: DRV-free routed DEF using [OpenROAD-flow](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts).
  * __v__: Verilog from routed DEF.
  * __sdc__: Timing constraint file. Contains clock periods. 
  * __spef__: SPEF file from routed DEF.
  * __5_worst.json__: Top 5 worst timing paths from timing report.
  * __endpoint_slacks.json__: Endpoints slack from timing report.


