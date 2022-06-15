# MapReduce
From a history report of various vehicles, the MapReduce program will produce a report of accidents per make and year of the car.

The history reports are stored as CSV files in HDFS with the following schema: 
| Column     | Type        |
|------------|:------------|
| incident_id | INT |
|incident_type | STRING (I: initial sale, A: accident, R: repair) |
| vin_number | STRING |
| make | STRING (The brand of the car, only populated with incident type “I”) |
| model | STRING (The model of the car, only populated with incident type “I”) |
| year | STRING (The year of the car, only populated with incident type “I”) |
| Incident_date | DATE (Date of the incident occurrence) |
| description | STRING |

## autoinc_mapper1.py

A mapper that reads the input data (data.csv) and propagates the make and year to the accident records (Incident Type A).

### Key / Value Pair
- Key: vin_number
- Value: (incident type, make, year)

**Input:**

[root@sandbox ~]# cat data.csv | python autoinc_mapper1.py

**Output:**       

VXIO456XLBB630221       ('I', 'Nissan', '2003')                                                                         
INU45KIOOPA343980       ('I', 'Mercedes', '2015')                                                                       
VXIO456XLBB630221       ('A', '', '')                                                                                   
VXIO456XLBB630221       ('R', '', '')                                                                                   
VOME254OOXW344325       ('I', 'Mercedes', '2015')                                                                       
VOME254OOXW344325       ('R', '', '')                                                                                   
VXIO456XLBB630221       ('R', '', '')                                                                                   
EXOA00341AB123456       ('I', 'Mercedes', '2016')                                                                       
VOME254OOXW344325       ('A', '', '')                                                                                   
VOME254OOXW344325       ('R', '', '')                                                                                   
EXOA00341AB123456       ('R', '', '')                                                                                   
EXOA00341AB123456       ('A', '', '')                                                                                   
VOME254OOXW344325       ('R', '', '')                                                                                   
UXIA769ABCC447906       ('I', 'Toyota', '2017')                                                                         
UXIA769ABCC447906       ('R', '', '')                                                                                   
INU45KIOOPA343980       ('A', '', '')

## autoinc_reducer1.py

- A reducer that reads from autoinc_mapper1.py
- Within a vin_number group, autoinc_reducer1.py iterates through all the records to find the ones that have the make and year available by identifying any record with an incident type I (Initial sale).
- After identifying the records with incident type I, it's captured in the group-level master info. 
- As autoinc_reducer1.py comes across accident records, those records are modified by adding the master info that was captured in the first iteration.


### Key / Value Pair
- Key: vin_number
- Value: (incident type, make, year)

**Input:**

[root@sandbox ~]# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py   

**Output:**

EXOA00341AB123456       ('A', 'Mercedes', '2016')                                                                       
INU45KIOOPA343980       ('A', 'Mercedes', '2015')                                                                       
VOME254OOXW344325       ('A', 'Mercedes', '2015')                                                                       
VXIO456XLBB630221       ('A', 'Nissan', '2003')

## autoinc_mapper2.py

- A mapper that reads the previous reducer output (autoinc_reducer1.py)

### Key / Value Pair
- Key: Concatenation of vehicle make and year
- Value: Count of vehicle make and year

**Input:**

[root@sandbox ~]# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py

**Output:**

Mercedes 2016    1                                                                                                       
Mercedes 2015    1                                                                                                       
Mercedes 2015    1                                                                                                       
Nissan 2003      1

## autoinc_reducer2.py

- A reducer that reads from autoinc_mapper2.py
- Within a group of cars and their make and years, sum the values provided from autoinc_mapper2.py

### Key / Value Pair
- Key: Concatenation of vehicle make and year
- Value: Count of vehicle make and year

**Input:**

[root@sandbox ~]# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort | python autoinc_reducer2.py

**Output:**

Mercedes 2015    2                                                                                                       
Mercedes 2016    1                                                                                                       
Nissan 2003      1
