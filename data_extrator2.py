import matplotlib.pyplot as plt



filename ="co2_mlo_surface-flask_1_ccgg_month.txt"
list_for_data = []
countlist = []
count = 0
with open("co2_mlo_surface-flask_1_ccgg_month.txt") as file_object:
        lines = file_object.readlines()

length = len(lines)
print("Number of lines =", length)

for line in range (71,length):        # the first line of data starts on line 70
    linedata =(lines[line][-7:])
    linedata_2 =float(linedata[:5])  # gets rid of the last two blank spaces from the string
    print (linedata_2)
    list_for_data.append(linedata_2)
    count = count+1
    countlist.append(count)

print (list_for_data)

plt.plot(countlist,list_for_data)

plt.ylabel("CO2 level")
plt.title("CO2 trend")
plt.axis([0, 600, 300, 450])
#plt.yticks(" ")

plt.show()
