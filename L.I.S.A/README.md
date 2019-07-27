# L.I.S.A (Low-cost Impedance Sensor and Analyser)

L.I.S.A is a low-cost IoT screening and assessment tool to detect malnutrition.  

L.I.S.A is a part of our whole solution which is used to gather data metrics like height, weight, and impedance of kids and estimate Body mass Index, Lean body mass, Body fat percentage, Water percentage, Protein percentage, Bone mass, Muscle mass, Visceral mass, and Basal metabolism rate.

The current system to screen and asses malnutrition in India relies on BMI and upper arm circumference test and all the record is maintained in a paper register. 

These tests, however, don't give us the entire picture. BMI alone cannot be used to asses the condition of the child. For example, according to the BMI scale, Mike Tyson is obese with a BMI of around 34.

It's also important to have an electronic system to maintain the record of these kids since a few of these kids are constantly migrating and it would be convenient to have a continuous record of their health and stats. 

## Our solution

Our solution consists of 
* A height scanner which uses an ultrasonic sensor.
* A Xiomi scale 2 to obtain the weight and impedance values of the child.
* An NFC module(PN532) to read the ID card data of the child.
* A Raspberry Pi to read all these data and estimate the body metrics then send all the data to the Watson IoT platform.

## How does it work?
