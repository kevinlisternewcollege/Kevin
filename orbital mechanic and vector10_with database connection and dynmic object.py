import time

import pygame # we use this module for all graphics
import sys  # we use this module to exist the game
import math # we will need to use this module for the trig functions to calculate angles
import pyodbc
import datetime
from datetime import date # used to create a unique table name for access database connection
from time import gmtime, strftime
import time

def createunique_recordname():
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime()).replace(" ", "", )
                datenow = str(datetime.datetime.now())
                monthandday = str(datenow[5:7]) + str(datenow[8:11])  # extract the month and day from datenow
                timenow1 = monthandday + timenow[10:20]
                timenow2 = timenow1.replace(" ", "")
                return timenow2

class data_entry:
    def __init__(self,Body):
        self.Start_position_x = 0
        self.Start_position_y = 0
        self.mass_of_body = 0
        self.Starting_x_velocity = 0
        self.Starting_y_velocity = 0
        self.graviational_constant = 0
        self.Body = Body

    def bodydata(self):
        self.Start_position_x= input(f"Start Position x of {self.Body}, in relation to the origin = ")
        self.Start_position_y = input(f"Start Position y of {self.Body} , in relation to the origin = ")
        self.mass_of_body =input (f"mass of {self.Body} = ")
        self.Starting_x_velocity = input(f"Starting velocity of {self.Body}, x component = ")
        self.Starting_y_velocity = input(f"Starting velocity of {self.Body}, y component = ")

    def Enter_other_data (self):
        self.graviational_constant = input ("Gravitational constant = ")


class CalculateNewPixelPositionsForAGivenCorordinate:

    def __init__(self, x_position, y_position):

        self.x_position_1 = int(x_position)
        self.y_position_1 = int(y_position)

    def pixelpositions (self):
        self.x_pixel = self.x_position_1 + float(500)
        self.y_pixel = -self.y_position_1 + float(250)

class findCentrePoint:

    def __init__(self, vectorpositionformass1, vectorpositionformasss2,mass1,mass2):
        self.vectorpositionformass1 = vectorpositionformass1
        self.vectorpositionformass2 = vectorpositionformasss2
        self.mass1 = float(mass1)
        self.mass2 = float(mass2)

    def finddistance(self):
        self.changeinx = self.vectorpositionformass1[0]-self.vectorpositionformass2[0]
        self.changeiny = self.vectorpositionformass1[1]-self.vectorpositionformass2[1]


    def findcentre_of_mass (self):

        self.x_centre_of_mass_from_m = self.changeinx * self.mass2/(self.mass1 + self.mass2)
        self.y_centre_of_mass_from_m = self.changeiny * self.mass2 / (self.mass1 + self.mass2)

    def findactualposition (self):
        self.x_position_of_centre_of_mass = -self.x_centre_of_mass_from_m+self.vectorpositionformass1[0]
        self.y_position_of_centre_of_mass = -self.y_centre_of_mass_from_m+self.vectorpositionformass1[1]

class OrbitalObject:

    def __init__(self,mass,attracting_mass,x_position,y_position,x_velocity,y_velocity,x_centre_of_mass, y_centre_of_mass):
        self.mass = mass
        self.attracting_mass = attracting_mass
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x_centre_of_mass = x_centre_of_mass
        self.y_centre_of_mass = y_centre_of_mass

    def calculateDistanceFrom1stMasstoCentreOfMass(self):
        self.distance = ((self.x_position-self.x_centre_of_mass)**2+(self.y_position-self.y_centre_of_mass)**2)**0.5

    def convertpositiontopixel(self):
        self.x_starting_pixel = self.x_position+int(500)
        self.y_starting_pixel = -self.y_position+int(250)

    def calculateForce(self):
            try:
                self.force = float(Gravitational_constant)*self.mass*self.attracting_mass/(self.distance**2)
                print ("force = ", self.force)
            except ZeroDivisionError:
                print ("The plant has hit the sun")

    def caclculateXandYcomponentsofforce (self):

        distance_between_masses.append(self.distance)
        self.Angle = math.asin((self.y_position-self.y_centre_of_mass)/self.distance)


        # check which quadrant we are in

        if (self.x_position-self.x_centre_of_mass) >= 0:
            if  (self.y_position-self.y_centre_of_mass) > 0:
                self.QuadrantTest = 1
            else:
                self.QuadrantTest = 4
        elif (self.x_position-self.x_centre_of_mass) < 0:
            if  (self.y_position-self.y_centre_of_mass) > 0:
                self.QuadrantTest = 2
            else:
                self.QuadrantTest = 3

        # correct the angle based on the quadrant

        if self.QuadrantTest == 3:
            self.Angle = abs(self.Angle) + math.pi
        if self.QuadrantTest == 2:
            self.Angle = -self.Angle + math.pi

        print("Angle = ", self.Angle)

        self.x_componentofforce = -math.cos(self.Angle) * self.force
        self.y_componentofforce = -math.sin(self.Angle) * self.force

    def new_acceleration (self):

        self.x_acceleration = (self.x_componentofforce/self.mass)
        self.y_acceleration = (self.y_componentofforce/self.mass)


    def new_velocity (self):
        self.x_velocity_caclulated = self.x_velocity+self.x_acceleration
        self.y_velocity_caclulated = self.y_velocity +self.y_acceleration

    def new_pixel_position (self):
        self.new_x_pixel = self.x_starting_pixel+self.x_velocity_caclulated
        self.new_y_pixel = self.y_starting_pixel-self.y_velocity_caclulated #note the minus because pixel positions count downwards

    def new_position(self):  # convert from pixels to position in relation to origin

        self.new_x_position_after_iteration = float(self.new_x_pixel) - int(500)
        self.new_y_position_after_iteration = -float(self.new_y_pixel) + int(250)

    def shipdisplay(self):  # calls the ship diagram. Note the use of "self" in the function definition
        imagetodisplay = pygame.image.load('ship.bmp')
        transformedimage = pygame.transform.scale(imagetodisplay, (10, 10))
        screen.blit(transformedimage, (self.new_x_pixel, self.new_y_pixel))

    def sundisplay(self, x, y):  # calls the sun. Again, note the use of "self" in the function definition
        sunimagetodisplay = pygame.image.load('sun.PNG')
        transformedsunimage = pygame.transform.scale(sunimagetodisplay, (20, 20))
        screen.blit(transformedsunimage, (x, y))

if __name__ == '__main__':

    Number_of_orbital_bodies = input("number of orbital bodies = ")
    EnterDataOrSelectFromDatabase = input("do you want to enter your own data. Yes or No  ")

    # connecting string for database connection will have to be changed to a path for your database. 2 available here, one for use when I am in college and one at home
    #conn_str = (
    #    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\kevin.lister\OneDrive - New College Swindon\computing science\progamme challenge\orbital_mechanics_data.accdb;')

    conn_str = (
       r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\kevin\OneDrive - New College Swindon\computing science\progamme challenge\orbital_mechanics_data.accdb;')

    tablename = "simulationdata"+Number_of_orbital_bodies #creates name for the tables in the database
    Data_set_up_list = []
    Data_tuple_access_upload =[]
    number_of_bodies = int(Number_of_orbital_bodies)

    if EnterDataOrSelectFromDatabase == "Yes":


        unique_record_name = createunique_recordname() #this function is called to create a unique identifier for each record in the database
        Data_set_up_list.append(unique_record_name)


        Gravitational_constant = input("Input your gravitational constant =")

        for counter in range (number_of_bodies):
            counter_ref = counter+1
            Objectstring = "OrbitalBody" +str (counter_ref) + "data"
            BodyName = "Body" + str(counter_ref)
            Objectstring = data_entry(BodyName)
            Objectstring.bodydata()
            Data_set_up_list.append(int(Objectstring.Start_position_x))
            Data_set_up_list.append(int(Objectstring.Start_position_y))
            Data_set_up_list.append(int(Objectstring.mass_of_body))
            Data_set_up_list.append(int(Objectstring.Starting_x_velocity))
            Data_set_up_list.append(int(Objectstring.Starting_y_velocity))

            position_vector = [float(Objectstring.Start_position_x), float(Objectstring.Start_position_y)]
            print (position_vector)
        Data_set_up_list.append(int(Gravitational_constant))
        print (Data_set_up_list)

        #position_vector = [float(OrbitalBody1data.Start_position_x), float(OrbitalBody1data.Start_position_y)]
        #position_vector_for_mass2 = [float(OrbitalBody2data.Start_position_x), float(OrbitalBody2data.Start_position_y)]

        Load_data_in_database = input("Do you want to load this set up into a database, Yes or No = ")

        if Load_data_in_database == "Yes":
            Data_tuple_access_upload.append(tuple(Data_set_up_list))
            #  SQL string for creating the tables data into the database

            SQLString_n = ""

            for counter1 in range(int(number_of_bodies)):
                counter2 = counter1 + 1
                print(counter2)
                String1 = "Start_Position_x_body" + str(counter2) + " Double,"
                print(String1)
                String2 = "Start_Position_y_body" + str(counter2) + " Double,"
                print(String2)
                String3 = "Mass_body" + str(counter2) + " int,"
                String4 = "Start_Velocity_x_body" + str(counter2) + " Double,"
                String5 = "Start_Velocity_y_body" + str(counter2) + " Double,"
                SQLString1 = String1 + String2 + String3 + String4 + String5
                print("SQLString1 =", SQLString1)
                SQLString_n = SQLString_n + SQLString1
            SQLString_for_creation_of_table = "Uniquetime text," + SQLString_n + "Gravitational_constant int"

            print("SQL", SQLString_for_creation_of_table)

            #SQL string for insertion
            SQLStringI_n = ""

            for counter1 in range(int(number_of_bodies)):
                counter2 = counter1 + 1
                print(counter2)
                StringI1 = "Start_Position_x_body" + str(counter2) + ","
                StringI2 = "Start_Position_y_body" + str(counter2) + ","
                StringI3 = "Mass_body" + str(counter2) + ","
                StringI4 = "Start_Velocity_x_body" + str(counter2) + ","
                StringI5 = "Start_Velocity_y_body" + str(counter2) + ","
                SQLStringI1 = StringI1 + StringI2 + StringI3 + StringI4 + StringI5
                print("SQLString1 =", SQLString1)
                SQLStringI_n = SQLStringI_n + SQLStringI1
            SQLString_for_insertion_into_table = "Uniquetime," + SQLStringI_n + "Gravitational_constant"


            now = datetime.date.month

            try:

                conn = pyodbc.connect(conn_str)
                cursor = conn.cursor()
                # timenow = str(date.today())

                print ("table name = ", tablename)

                Execute_sql_string = "CREATE TABLE "+tablename+" ("+SQLString_for_creation_of_table+");"
                print (Execute_sql_string)
                cursor.execute(Execute_sql_string)

                conn.commit()
            except:
                print ("The table already exists, or there was another problem")

            Number_of_entries = 5*number_of_bodies

            # create the VALUE component of the SQL string
            value_counter_string = "?,?,"  # this adds two data entries for the unique ID and the gravitational constance
            for value_counter in range (Number_of_entries):
                value_counter_string = value_counter_string + "?,"
            print (value_counter_string[:-1])

            Insert_sql_string = "INSERT INTO " + tablename + " (" + SQLString_for_insertion_into_table + ") VALUES (" + value_counter_string[:-1]+");"  #The [:-1] strips of the last comma
            print (Insert_sql_string)

            print (Data_tuple_access_upload)
            cursor.executemany(Insert_sql_string,Data_tuple_access_upload)
            conn.commit()
    else:

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {tablename}')
        rows = cursor.fetchall()  #gets all rows from the table and stores in object, rows
        print (rows)
        rowcounter = 1
        simulationdata = []
        for row in rows:
            print("row number = ", rowcounter,row)
            simulationdata.append(row)
            rowcounter = rowcounter+1


        Simulation_selection = input("decide which row number you want to run = ")
        Data_set_up_list = simulationdata[int(Simulation_selection) - 1] # selects an entry from the list of records
        print(Data_set_up_list)
        Gravitational_constant = Data_set_up_list[5 * number_of_bodies + 1]



    distance_between_masses = []

    pygame.init()

    screen = pygame.display.set_mode((1000, 500))  # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    pygame.display.set_caption("vectors")

    bg_colour = (0, 0, 230)  # set the colour
    screen.fill(bg_colour)


    pygame.draw.line(screen, (0, 0, 255), (500, 0),
                     (500, 500))  # self.screen is referenced in the class attributes. This draws the yaxis
    pygame.draw.line(screen, (0, 0, 255), (0, 250),
                     (1000, 250))  # self.screen is referenced in the class attributes. This draws the xaxis
    #convert data extracted from database to a list
    Data = []
    for counter10 in range (len(Data_set_up_list)):
        Data.append(Data_set_up_list[counter10]) # creates data list for use by loops

    print ("Data",Data)
    running = True
    while running:
        # watch for keyboard and mouse events.

        event = pygame.event.get()  # this for loop runs continuously
        if event == pygame.QUIT:
            sys.exit()
            running = False

        # The following section calculates the centre of mass of the orbiting system for n orbital bodies

        position_vector1 = [Data[1], Data[2]]
        mass_1 = Data[3]
        for counter3 in range (number_of_bodies-1):
            print (5*counter3+1)

            position_vector2 = [Data[5*(counter3+1)+1],Data[5*(counter3+1)+2]]
            print ("position vector 1", position_vector1)
            print("position vector 2", position_vector2)


            mass_2 = Data[5*(counter3+1)+3]


            centrepoint = findCentrePoint( position_vector1,position_vector2,mass_1,mass_2)
            centrepoint.finddistance()
            centrepoint.findcentre_of_mass()
            centrepoint.findactualposition()

            x_position_for_centre_of_mass = centrepoint.x_position_of_centre_of_mass
            y_position_for_centre_of_mass = centrepoint.y_position_of_centre_of_mass

            position_vector1 =[x_position_for_centre_of_mass,y_position_for_centre_of_mass] # The centre of mass now becomes position vector 1
            mass_1 = mass_1+ mass_2 # we increment the mass once the new centre of mass has been found to repeat the process
            #convert co-ordinate to pixel positions for plotting
            print ("position of Barrycentre = ", position_vector1)
            print ("Mass of bary centre ", mass_1)

        pixel_position = CalculateNewPixelPositionsForAGivenCorordinate(x_position_for_centre_of_mass,y_position_for_centre_of_mass)
        pixel_position.pixelpositions()
        print("x pixel position = ", pixel_position.x_pixel)
        print("y pixel position =", pixel_position.y_pixel)

        pygame.draw.circle(screen, (255,   0,   0), (pixel_position.x_pixel,pixel_position.y_pixel), 1,1) # draws the point for the centre of mass

        #This section creates n obritalobjects and applies the gravitational forces to them from the centre of mass, this code needs to be developed and doesn't work yet

        for counter4 in range (number_of_bodies):

            counter_ref = counter4 + 1   # counter_ref will be used to refer to a body by its number
            #Objectstring = "OrbitalBody" + str(counter_ref) + "data"
            #BodyName = "Body" + str(counter_ref)

            #section below takes the data from the Data_set_list

            print ("Body number = ", counter_ref)
            Start_position_x = Data[counter4 * 5 + 1]
            print ("start position in x ", Start_position_x)
            Start_position_y = Data[counter4 * 5 + 2]
            print ("start position y ", Start_position_y)
            Mass_of_body = Data[counter4 * 5 + 3]
            print  ("mass of body", Mass_of_body)
            Starting_x_velocity = Data[counter4 * 5 + 4]
            print ("Start x velocity",Starting_x_velocity)
            Starting_y_velocity = Data[counter4 * 5 + 5]
            print ("Starting y velocity", Starting_y_velocity)
            OrbitalBody = OrbitalObject(Mass_of_body,mass_1,Start_position_x,Start_position_y,float(Starting_x_velocity),float(Starting_y_velocity),centrepoint.x_position_of_centre_of_mass,centrepoint.y_position_of_centre_of_mass)


            # sequence of calculations follows below

            OrbitalBody.calculateDistanceFrom1stMasstoCentreOfMass()

            distance_from_2ndmass = OrbitalBody.distance
            OrbitalBody.convertpositiontopixel()
            OrbitalBody.calculateForce()
            OrbitalBody.caclculateXandYcomponentsofforce()
            OrbitalBody.new_acceleration()
            OrbitalBody.new_velocity()
            OrbitalBody.new_pixel_position()
            OrbitalBody.new_position()

            OrbitalBody.shipdisplay()  # the ship display

            Starting_x_velocity = OrbitalBody.x_velocity_caclulated
            Starting_y_velocity = OrbitalBody.y_velocity_caclulated

            Start_position_x = float(Start_position_x) + OrbitalBody.x_velocity_caclulated
            Start_position_y = float(Start_position_y) + OrbitalBody.y_velocity_caclulated

            # update the data_set_up_list
            print ("Data =",Data)
            print(Start_position_x)
            print (Start_position_y)


            print ("data to be replaced and position")

            print(Data[5 * counter4 + 1],(5 * counter4 + 1))
            print (Data[5 * counter4 + 2],(5 * counter4 + 2))
            print (Data[5 * counter4 + 4],(5 * counter4 + 4))
            print (Data[5 * counter4 + 5],(5 * counter4 + 5))

            #remove old values from data list

            Data.pop(5 * counter4 + 1)
            Data.pop(5 * counter4 + 1) # after we pop the first the list moves one to the left
            Data.pop(5 * counter4 + 2)
            Data.pop(5 * counter4 + 2)

            print ("Data after popping = ", Data)

            # add new values into the Data

            Data.insert(5*counter4+1,Start_position_x)
            Data.insert(5*counter4+2,Start_position_y)
            Data.insert(5*counter4+4,Starting_x_velocity)
            Data.insert(5*counter4+5,Starting_y_velocity)

            position_vector = [Start_position_x,Start_position_y]
            print ("Data set up list for each body ",Data)

        print (f"position vector for mass {counter4+1} ", position_vector)
        #time.sleep(0.02)  # you can change this to increase or decrease the speed of the simulation and the display

        #position_vector_for_mass2 = [Starting_position_x_of_mass2, Starting_position_y_of_mass2 ]
        #print("position vector for mass 2", position_vector_for_mass2)
        font_obj = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)  # create a text box to display distance
        font_color = (0, 150, 250)

        #display_distance = "distance=" + str(round(orbitalbody1.distance, 2)) + " angle=" + str(round(orbitalbody1.Angle, 2))  # text box display
        #text_obj = font_obj.render(display_distance, True, font_color)  # create an object for the display data
        #blank_text = "                                                              "  # create blank to display. This will display first
        #text_obj1 = font_obj.render(blank_text, True, font_color, bg_colour)  # creat a blank object
        #screen.blit(text_obj1, (22, 0))  # display a blank box. This will remove any previous data
        pygame.display.flip()  # pygame now displays the graphic

        #screen.blit(text_obj, (22, 0))  # now add the distance text
        pygame.display.flip()  # redisplay the screen with the distance text

        #if event.type == pygame.QUIT:  # this function returns a list of events that have taken place since the time this function was called. If the player clicks the close window button, it will trigger QUIT and sys.exit
         #   sys.exit()
