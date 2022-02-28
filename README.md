Movie theatre seat allocation for allocating requested seats to customers based on maximizing customer satisfaction, seat allocation and customer safety. 

Implemented in **Python**. 

**Features of the model:**
1. A priority based approach was used to assign the seats. This priority is depicted below: 
<pre>
Row Name  Priority 
E            1
F            2
G            3
D            4
H            5
C            6
I            7
J            8
B            9
A            10
</pre>
Here, priority of 1 denotes the highest priority and 10 denotes the least priority. 

2. A customer who has requested a specific number of seats is preffered to be given seats together. But, if the theatre does not have consecutive seats, then random allocation occurs. 

3. If the requested seats is more than the available seats, then the user is promoted with an appropiate message saying that the seats requested is not available. 

4. The program is a command line executable which takes an input file with requests and prints the output seat allocated for all the requests in an output file. 

5. If the seats requested is greater than the maximum row count, the seats are split based on the maximum row count avaiable and allocates based on maximum customer satisfaction and safety. 

**Instructions:**

1. Download theatre_seat_allocation.py
2. Open command line and run the python file in the same repository as the code using "python theatre.seat_allocation.py <input_text_file>"
4. Read output_file.txt file that will be created in the same directory as the code file. 

**Further Improvements:**
1. Coumn wise priority can be implemented to assign the middle seats first to the customers. 
2. When assigning random seats in the cases where the theatre does not have continuous seats left, we can assign seats based on column and row-wise priority. 
