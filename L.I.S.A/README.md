# L.I.S.A (Low-cost Impedance Sensor and Analyser)

L.I.S.A is a low-cost IoT screening and assessment tool to detect malnutrition.  

L.I.S.A is a part of our whole solution which is used to gather data metrics like height, weight, and impedance of kids and estimate Body mass Index, Lean body mass, Body fat percentage, Water percentage, Protein percentage, Bone mass, Muscle mass, Visceral mass, and Basal metabolism rate.

The current system to screen and asses malnutrition in India relies on BMI and upper arm circumference test and all the record is maintained in a paper register. 

These tests, however, don't give us the entire picture. BMI alone cannot be used to asses the condition of the child. For example, according to the BMI scale, Mike Tyson is obese with a BMI of around 34.

It's also important to have an electronic system to maintain the record of these kids since a few of these kids are constantly migrating and it would be convenient to have a continuous record of their health and stats. 

## Our solution

Our solution consists of 
* A height scanner which uses an ultrasonic sensor.
* A Xiaomi scale 2 to obtain the weight and impedance values of the child.
* An NFC module(PN532) to read the ID card data of the child.
* A Raspberry Pi to read all these data and estimate the body metrics then send all the data to the Watson IoT platform.

## How does it work?

1. A child is made to stand on the weight scale and the scale measures the weight of the child and the impedance.
![Scale](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/scaletest.jpeg)
2. The ID card of the child is swiped on the NFC module and the child's ID is obtained.
![IDcard](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/IDcard.jpg)
3. The height of the child is obtained using the height scanner. A spirit level attached to the scanner is used to keep the sensor pointed perpendicularly down towards the ground.
![Height](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/heightscannerTest.jpg)
4. The raspberry pi recieves these metrics and estimates the previously mentioned body metrics. Then it sends all these data to the watson Iot platform.
![Data](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/data.png)
