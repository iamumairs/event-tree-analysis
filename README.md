# Event Tree Analysis
This is a simple code of event tree analysis. I have a plan to add more features in future. 

## System Description

A system can be given in the following form in a .csv file:

```
            componenet 1, component 2
            ---------------------------
           |  Sensor_1  , Sensor_2     (first row for component names)
  State 1  |   open     ,  misaligned
  State 2  |   short    ,  low_voltage
  State 3  |   stuck    ,  noisy
  
  ```
  
  ## Usage
  
  ```
  
  usage: et_tool.py [-h] [-s SYSTEM] [-o OUT]

Event Tree Analysis Tool

optional arguments:

  -h, --help  show this help message and exit
  -s SYSTEM   System Description -- components and associated states
  -o OUT      Name of the output analysis file
  
  ```
