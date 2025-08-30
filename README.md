# seek-coding-challenge

A Python program that reads traffic data from a file and generates required stats.

## Setup and Running the Script
Before running the script, pandas and pytest are required to be pip installed which can be found in requirements.txt:
```pip install -r requirements.txt```
or alternatively:
```pip install pandas pytest```

To run the script:
```python3 main.py traffic_data.txt```

To run the tests:
```pytest```

## Required Outputs
- The number of cars seen in total.
- A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.
- The top 3 half hours with most cars, in the same format as the input file.
- The 1.5 hour period with least cars (i.e. 3 contiguous half hour records).

## Constraints
- The program can be written in Java, Scala or Python, and with any libraries you are familiar with. You are encouraged to use modern versions of each language and make use of their features.
- The program must be accompanied with reasonable levels of unit tests.
- The solution should be developed to professional standards, the code may be used and extended by your teammates.
- The solution should be deliverable within a couple of hours - please do not spend excessive amounts of time on this.
- Avoid over-engineering.

## Thoughts
This project was made with python as it's the language I'm most comfortable in. I made use of pandas due to the nature of the data being tabular which makes it super helpful due to its built-in functions.
I've made it a class so it's easy to read and I've also included doctrings as a simple explanation for each function, covering the need for teammates being able to understand what I've done and extend on it.
