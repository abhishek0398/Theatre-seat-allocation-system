import os
import sys


def count_available_seats(seats):
    """
    This function takes input as the seats of the theatre and returns the number of available seats for allocation
    """
    total_seats = 0
    for row in seats:
        total_seats += row.count(0)
    return total_seats
def block_seats_safety(index, start, end, seats):
    if start-3 >= 0:
        row = seats[index]
        for i in range(start-3, start):
            row[i] = 1
    if end+3 <=19:
        row = seats[index]
        for i in range(end, end+3):
            row[i] = 1
    if index > 0:
        prev_row = seats[index-1]
        for i in range(start, end):
            prev_row[i] = 1
    if index < 9:
        next_row = seats[index+1]    
        for i in range(start, end):
            next_row[i] = 1
            
         
def remainder_allocation(seats, row_priority, seat_count):
    """
    This function is used to allocate seats on random without any priority
    """
    row_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    seat_numbers = []
    while seat_count != 0:
        for row in range(len(seats)):
            if seats[row].count(0) != 0:
                seat_index = [i for i in range(len(seats[row])) if seats[row][i] == 0]
                for index in seat_index:
                    seat_count -= 1
                    seats[row][index] = 1
                    seat_numbers.append(row_name[row] + str(index))
        return seat_numbers
    return -1
                
                
def priority_allocation(seat_count, row_priority, seats):
    """
    This function allocates seats on priority: People booking will all sit together, seats are allocated on priority set on rows.
    """
    for row in range(10):
        row_index = list(row_priority[row + 1].values())[0]
        row_data = seats[row_index]
        if row_data.count(0) < seat_count:
            continue
        else:
            for i in range(0,len(row_data)):
                if i+seat_count <=20 and row_data[i:i+seat_count] and 1 not in row_data[i:i+seat_count]:
                    # print(i, i+seat_count)
                    seat_names = []
                    for j in range(i, i+seat_count):
                        row_data[j] = 1
                        seat_names.append(list(row_priority[row + 1].keys())[0] + str(j))
                    block_seats_safety(row_index, i, i+seat_count, seats)
                    return seat_names
    return remainder_allocation(seats, row_priority, seat_count)
            

def allocate_seats(request, total_seats, row_priority, seats):
    """
    This function checks the availability in the theatre and calls the priority allocation function
    """
    request_number, seat_count = request.split(" ")
    if int(seat_count) > total_seats:
        return -1
    elif int(seat_count) >20:
        seat_count = int(seat_count)
        quotient = seat_count // 20
        remainder = seat_count % 20
        seat_number = []
        for i in range(quotient):
            seat_number.extend(priority_allocation(20, row_priority, seats))
        seat_number.extend(priority_allocation(remainder, row_priority, seats))
        return seat_number      
    else:
        seat_number = priority_allocation(int(seat_count), row_priority, seats)
        return seat_number


def main(file_content, path):
    """
    This is the main function
    """
    folder_path = os.path.split(path)[0]
    output_file_path = os.path.join(folder_path, "output_file.txt")
    print("output file path: ",output_file_path)
    output_writer = open(output_file_path, 'w')
    row_priority = {1: {"E": 4}, 2: {"F": 5}, 3: {"G": 6}, 4: {"D": 3}, 
                    5: {"H": 7}, 6: {"C": 2}, 7: {"I": 8}, 8: {"J": 9}, 
                    9: {"B": 1}, 10: {"A": 0}}

    seats = []
    for i in range(10):
        seats.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        
    for record in file_content:
        total_seats = count_available_seats(seats)
        # print("Available seats: ",total_seats)
        res = allocate_seats(record, total_seats, row_priority, seats)
        if res == -1:
            # print("No seats available")
            output_writer.write("No more seats available \n")
        else:
            # print(seats)
            # print(res)
            output_writer.write(record.split(' ')[0] + " " + ", ".join(res) + "\n")
    output_writer.close()


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    file_data = open(input_file_path, 'r').readlines()
    # file_data = open("request history.txt", 'r').readlines()
    output = main(file_data, input_file_path)
