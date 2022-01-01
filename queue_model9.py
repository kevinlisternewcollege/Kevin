import datetime
import queue
import random
import math
import matplotlib.pyplot as plt
import pyodbc

class SnapshotQueue(queue.Queue):
    def snapshot(self):
        with self.mutex:
            return list(self.queue)

q1 = queue.Queue(10)  # determines we have a simple First in First out queue (FIFO)
q2 = queue.Queue(10)

Hours_for_simulation = input("Hours for simulation = ")
Seconds_for_simulation = int(Hours_for_simulation)* 3600

Number_of_people_per_Hour = input("The estimated number of people per hour = ")
Rate_Per_Second = int(Number_of_people_per_Hour) / 3600

Min_Time_In_Queue = input ("Min time in queue = ")
Max_Time_In_Queue = input ("Max time in queue = ")


Server_time = 0 #initialisation of variable
Number_taken_from_queue1 = 0
Time_for_next_server = 0
Total_queuing_time = 0  # this variable is used to accumulate the total queueing time each second
Queue_size_list = []
Counterlist = []
TotalTimeList = []
Tuple_for_database =[]

Probability_zero = Rate_Per_Second ** 0 * math.exp(-Rate_Per_Second) / math.factorial(0)  #Poisson distribution
Probability_one = Rate_Per_Second ** 1 * math.exp(-Rate_Per_Second) / math.factorial(1)
Probability_two = Rate_Per_Second ** 2 * math.exp(-Rate_Per_Second) / math.factorial(2)
Probability_three = Rate_Per_Second ** 3 * math.exp(-Rate_Per_Second) / math.factorial(3)

Cumulative_probability_to_zero = Probability_zero
Cumulative_probability_to_One = Cumulative_probability_to_zero + Probability_one
Cumulative_probability_to_Two = Cumulative_probability_to_One + Probability_two
Cumulative_probability_to_Three = Cumulative_probability_to_Two + Probability_three



for counter in range (Seconds_for_simulation):

    Random_for_queue_addition = random.random()

    if Random_for_queue_addition < Cumulative_probability_to_zero:
        Addition_to_Queue = 0
    elif Random_for_queue_addition < Cumulative_probability_to_One:
        Addition_to_Queue = 1
    elif Random_for_queue_addition < Cumulative_probability_to_Two:
        Addition_to_Queue = 2
    else:
        Addition_to_Queue = 3

    print("Number to be added to queue = ", Addition_to_Queue)

    for counter_inputs in range(Addition_to_Queue):
        time_in_q1 = random.randint(int(Min_Time_In_Queue), int(Max_Time_In_Queue))
        if q1.full() == False:
            q1.put(time_in_q1)
            print("queue size is now =", q1.qsize())

    the_snap_shot = SnapshotQueue.snapshot(q1)
    print ("the snap shot = ", the_snap_shot)

    # find the total time in the snap shot
    Total_time = 0 # initialise total time for each loop
    length_of_snap_shot = len(the_snap_shot)
    for snap_shot_counter in range (length_of_snap_shot):
        Total_time = Total_time + the_snap_shot[snap_shot_counter]
    print ("Total Time = ", Total_time)
    TotalTimeList.append(Total_time) # this list is saved for interest and further analysis

    if q1.full() == True:
        print("queue is full")



# initialisation of servers

    if Number_taken_from_queue1 == 0 and q1.empty() == False:
        Time_for_next_server = counter + int(q1.get())
        Number_taken_from_queue1 = Number_taken_from_queue1 + 1

    if counter >= Time_for_next_server and q1.empty() == False:
        time_to_process = q1.get()
        Time_for_next_server = counter + time_to_process
        print ("Time for next server = ", Time_for_next_server)

    Queue_size_list.append(q1.qsize())  # this creates a list of y values that will be used for the graph
    Counterlist.append(counter)         # this creates a list of x values that will be used for the graph

    Total_queuing_time = Total_queuing_time + Total_time # finds the total queuing time at the end of the simulation

    Tuple_data = (counter, q1.qsize(),Total_time)
    Tuple_for_database.append(Tuple_data)

# at this point the counter loop ends

    print(f"second = {counter} and queue size ={q1.qsize()}")

print('Simulated time completed')       # this prints once the loop has finished.
print (Counterlist)                     # this prints a list of the seconds, it is not important and can be hashed out
print (Queue_size_list)                 # this prints out the queue size, second by second.
print (TotalTimeList)                   # this prints out the time total time by the second that a person waits
print (Tuple_for_database)

# we can now work out the average queue time

Average_queuing_time = round ((Total_queuing_time / Seconds_for_simulation),1)  # round to 1 dp
Text_for_graph = "Average queue time " + str(Average_queuing_time)   # create text for string for graph

# this section now connects to an access database

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\kevin.lister\OneDrive - New College Swindon\computing science\progamme challenge\Database_for_queue_output.accdb;'
    )
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


Table_Name = "Simulation_time_"+Hours_for_simulation+"_people_per_hour_"+Number_of_people_per_Hour+"_Min_time_" + Min_Time_In_Queue +"_Max_time_"+ Max_Time_In_Queue
print (Table_Name)


cursor.execute(f'''
		CREATE TABLE {Table_Name} (
			second_id int primary key,
			queue_size int,
			total_time int
			)
               ''')

conn.commit()

# we now enter data into the database



cursor.executemany(f'INSERT INTO {Table_Name}(second_id,queue_size,total_time) VALUES (?,?,?)',Tuple_for_database)
conn.commit()

# we now plot

plt.plot(Counterlist,Queue_size_list )  #plt is the object and we call the method plot.
plt.ylabel('queue size')
plt.xlabel ("time in seconds")
plt.title(f"Number per hour= {Number_of_people_per_Hour}, Min time= {Min_Time_In_Queue}, Max time ={Max_Time_In_Queue}")
plt.text(1, 7, Text_for_graph , size=12, math_fontfamily='cm')  # add text string to graph

plt.show()                              #this command instructs Python to plot


quit()
