from bs4 import BeautifulSoup  # this is called from BeautifulSoup4
import requests

team_points = []
team_name =[]

# prior to running the programme you need to install the package lxml

html_text_of_page = requests.get("https://www.premierleague.com/tables?co=1&se=418&ha=-1",verify=False).text

#html_text_of_page = requests.get("https://www.premierleague.com/tables?co=1&se=-1&ha=-1").text

#print (html_text_of_page)

soup2 = BeautifulSoup(html_text_of_page, "lxml")
#print (soup2.prettify())

tags3 = soup2.find_all('td',class_="points") # applies the method of find_all from the class Beautiful Soup
                                                # td is the heading title from the html page
tags4 = soup2.find_all ('span', class_="long")

print (tags3)
print (tags4)

for points in tags3:
        print(points)

# code to cleanse the data

for points in tags3:
    points_string = str(points)
    #if len(points_string) ==
    #print(len(points_string))
    if len(points_string)==26:
        actual_points =points_string[19:21]
        print(points_string[19:21])
    else:
        actual_points = points_string[19:20]
        print(points_string[19:20])

    team_points.append(actual_points)
    #print ("stripped data = ",stripped_data)

#for teams in tags4:
#   print(teams)

for long in tags4:  # code to strip out team name from string, thanks to Shraddha
    name = str(long)
    size = len(name)
    Teams = name[19:size]
    Teams2 = Teams[:-7]
    team_name.append(Teams2)
    print(Teams2)

# brining together the points and the teams, thanks for Frank

taggs1 = []
taggs2 = []

for points in tags3:
    point = list(points)
    taggs1.append(point[0])
    print(point[0])

for teams in tags4:
    team = list(teams)
    taggs2.append(team[0])
    print(team[0])
print(taggs1)
for i in range(0,len(taggs1)):
    print(taggs2[i] + " : " + taggs1[i])