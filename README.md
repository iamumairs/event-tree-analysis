# Event Tree Analysis
Event Tree Analysis

## Usage

A system can be given in the following form in a .csv file:

            componenet 1, component 2
            ---------------------------
           |  Sensor_1  , Sensor_2     (first row for component names)
  | State 1  |   open     ,  misaligned
  | State 2  |   short    ,  low_voltage
  | State 3  |   stuck    ,  noisy
