# DATC RDF Calibrations

This repository provides calibrations for two basic electrical analyses, parasitic estimation and static timing analysis, using publicly-available enablements (NanGate45, SKY130). Our hope is that these calibration datasets will help boost the research community's advancement along the axes of accuracy, turnaround time, and capacity for these fundamental analyses that inform IC physical implementation. 

## Timer Calibration Data 

Our initial data compilation uses four DRV-free routed DEFs produced by the OpenROAD flow: `aes_cipher_top` and `jpeg_encoder` designs, in each of the SKY130 and NanGate45 enablements. Golden calibration data is abstracted and anonymized using a 5-worst JSON format, which we use to hold block-level worst (negative) slack, total negative slack, and number of failing endpoints (i.e., standard WNS, TNS and FEP metrics), along with detailed information for the top-5 worst timing paths (including arc delays and pin arrival times). We provide a timing report viewer that reads 5-worst JSON-formatted data and prints out a timing report in the OpenSTA tool's report format. To facilitate other calibrations of interest, we also propose an endpoints JSON format, which can capture setup slack values at every flip-flop D pin. We can compare the endpoint slacks from OpenSTA with calibration endpoint slack values. 

### JSON Format Description

TBA


## RCX and Static IR Drop Calibration Data

TBBA
