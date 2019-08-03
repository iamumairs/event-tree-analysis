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

## Usage

### Example
```
python3 et_tool.py  -s=system.csv -o=analysis.txt

```

### Output 

```
*********************************************************************
                                System Description
*********************************************************************
  Sensor_1      Sensor_2
0     open   misaligned 
1    short  low_voltage 
2    stuck         noisy
 
*********************************************************************
                                Event Tree Graph
*********************************************************************

                   /-misaligned
                  |
         /- /open-|--low_voltage
        |         |
        |          \-noisy
        |
        |           /-misaligned
        |          |
-SYSTEM-|-- /short-|--low_voltage
        |          |
        |           \-noisy
        |
        |           /-misaligned
        |          |
         \- /stuck-|--low_voltage
                   |
                    \-noisy
 
*********************************************************************
                                All Paths
*********************************************************************

Path 1 = ('open', 'misaligned ')
Path 2 = ('open', 'low_voltage ')
Path 3 = ('open', 'noisy')
Path 4 = ('short', 'misaligned ')
Path 5 = ('short', 'low_voltage ')
Path 6 = ('short', 'noisy')
Path 7 = ('stuck', 'misaligned ')
Path 8 = ('stuck', 'low_voltage ')
Path 9 = ('stuck', 'noisy')

```

