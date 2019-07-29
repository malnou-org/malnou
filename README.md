# malnou

India suffers due to droughts every year. Droughts tend to have a huge impact on malnutrition, especially in children.

The children living in these drought-affected areas suffer from malnutrition even years after the drought has occurred. The government has established Anganwadi schools to help provide care to these children. Although the malnutrition rates have reduced, the system is not fully efficient. 

After speaking to the workers and staff in these anganwadis and the parents of these children, we were able to identify these 3 main problems.

## Problems

1. Lack of motivation to do extra work because the Anganwadi staff gets a fixed salary irrespective of how much work extra work they do.

2. It's very difficult to keep a track of the health of children that belong to migrant workers as they keep changing their place of stay every few weeks.

3. Parents withdraw their children from anganwadis as they are abused by the staff and the parents feel powerless to stand up to the staff. They feel it's easier to just withdraw the child from the Anganwadi.

## Solutions

Our project consists of a multipart solution to address these above problems.
![Solution](https://github.com/malnou-org/malnou/blob/master/images/solution.jpg)

* ***malnou_sms*** 

Our SMS based communication system using Watson NLU. The parents can raise complaints they have related to child abuse, poor infrastructure, food conditions, etc. This enables the parents to receive notifications related to their child's health status, a food plan of the Anganwadi and any other activities. If the parents feel like they are part of the system, they feel more empowered thereby reducing the no of kids that are leaving these anganwadis.

To learn more about malnou_sms check it's readme [here.](https://github.com/malnou-org/malnou/blob/master/malnou_sms/README.md)

* ***L.I.S.A*** 

LISA is our low-cost IoT solution to help screen children to enable efficient tracking of their health data. The current method of diagnosing and tracking involves maintaining data in the form of a paper register. Our solution measures these metrics electronically and streams them to IBM cloud where they are stored. Unlike the existing system, we don't just measure BMI, we are ale to measure Protein percentage, Muscle mass, Bone mass, Body fat percent, and many other metrics. 

If we can identify that the state of the child is improving from this data, we can provide an incentive-based raise to the workers which should motivate them to put that extra effort that will go a long way in improving the condition of the child. Since all the data is measured electronically and sent to the cloud, there is no room for manipulation.

For more information related to L.I.S.A check it's [readme.](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/README.md)

* ***NFC based Identification and Tracking***

NFC modules are implemented in L.I.S.A, We use NFC tags to identify and verify the child during the medical screening process. A child is assigned to an NFC tag during registration and this is the unique ID of the child. If a child moves to a different place we still have the medical and educational data of the child stored in the cloud so re-enrolling in a new Anganwadi should be super easy. This will enable better tracking of these migrant children to ensure that their health condition is improving. 

## Project roadmap
![roadmap](https://github.com/malnou-org/malnou/blob/master/images/screencapture-infograph-venngage-edit-b3669ab5-45d1-4e6f-87da-0b867703503b-2019-07-29-22_27_46.png)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/malnou-org/malnou/blob/master/CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/malnou-org/malnou/blob/master/LICENSE) file for details
