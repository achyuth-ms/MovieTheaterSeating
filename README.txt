Coding problem title:	Movie Theater Seating Challenge

Description:	This program is built to solve the problem of allocating maximum seats to customers by meeting the constrains of 
customer satisfaction and customer safety in a theater consisting of 10 rows where each row consists of 20 seats. In this theater rows 
are labelled from A to J with J being the farthest to the screen and A being nearest to the screen. This program is built in python
 which takes the inputs requests from customers in a first come first serve order (FIFO) thereby allocating the seats to the topmost 
request first. If a user requests 8 seats, then the algorithm allocates the next available 8 seats to the user in a row if where there 
are 8 continuous available 8 seats then buffers the next 3 seats in that specific row and all the seats which are above and below 
the selected row are also buffered.

Assumptions made:
The Algorithmic approach is Greedy which starts filling the seats from the topmost edge seat
If number of seats requested are greater than 20 then a row buffer of one is not created as all belong to the same group
Further all remaining seats are buffered if the begin or end allocated seat is less than 3 seats from the beginning or ending
Constraints considered for customer satisfaction are: 
Customer prefer seats farthest from the screen so fills from topmost seat
Seats are filled in unidirectional sequence
Returns "House Full" is the requested number of seats are greater than the number of vacent seats present

Instructions to execute: 
Open the command prompt
Execute the code by entering python3 <path to the file>
Enter the path of the input file
The output file path is displayed in the terminal which is created at the same location as that of input file titled as output.txt
To further build and execute various tests create a text document and repeat the above steps

Example execution:
Sample Input:
R0001 2
R0002 10
R0003 20
R0004 6
R0005 12
R0006 3
R0007 5
R0008 7
R0009 2
R0010 18
R0011 4
R0012 2
R0013 23

Output for given sample Input:
R0001 J1,J2
R0002 J6,J7,J8,J9,J10,J11,J12,J13,J14,J15
R0003 H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20
R0004 F1,F2,F3,F4,F5,F6
R0005 E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18
R0006 D1,D2,D3
R0007 C4,C5,C6,C7,C8
R0008 C12,C13,C14,C15,C16,C17,C18
R0009 J19,J20
R0010 A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18
R0011 F19,F20,D19,D20
R0012 B19,B20
R0013 House Full

Time Complexity = O(m x n x k)
Here m = number of rows
n = number of seats in each row
k = number of lines in the input text file which is number of seat requests 
Implementation is Greedy where rows are filled from topmost seat that is farthest from the screen
Maximum seats that can be filled are 100

Space Complexity = O(1)
No extra space considered

Libraries used: os – to extract the path of the file

Possible Improvements: 
Considering if customer prefers seats in the center than at the corners 
Safety can be further improved by assigning seats farthest away from the previous assignment but might not lead to 
optimal filling of all seats farthest calculated by mean of start seats and mean of end seats
Can be extended to provide the max number of seats available if the requested number of seats are not available
