class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age




    def sit (self):
        print (f"{self.name} is now sitting")

    def roll(self):
        print(f"{self.name} is now rolling")

    def update_dog_age(self, age):  #this function allows updating the dogs age
        self.age = age
        if self.age > 15:
            self.age = 15
            print("The dog dead would be dead, so the age must be",self.age)

    def increment_the_dogs_age(self,additional_year):  #this function increments the age by a given amount
        self.age += int(additional_year)

class guard(dog):       # this is the child class
    def __init__(self,name,age):    # we define the child class
        dog.__init__(self,name,age) # we pass the attributes from the parent class
        self.teeth_size = 10        # we add other attributes.


    def warn_about_the_teeth(self): # we have a method we can call in the child class that uses the new attributes
        print(f"{self.name} has teeth that are {self.teeth_size}  cm")

    def roll(self):     #if someone call a parent method that doesn't apply to the child
        print(f"{self.name} is a guard dog and doesn't roll")


My_dog = dog("willie",6)


print (f"My dog's name is {My_dog.name}")

hotday = input("is it a hot day, yes or no ?")

if hotday == 'yes':

    My_dog.sit()
else:
    My_dog.roll()

# change the My_dog's age

My_dog.age = input("enter a new dog age = ")
print ("My dog's age is = ", My_dog.age)

# update the age using a function
input()
Age_to_pass_to_function = input ("enter another new age for the dog = ")

My_dog.update_dog_age(int(Age_to_pass_to_function))
print ("My dog's age is updated from a function = ", My_dog.age)

additional_years  = input ("now some years have passed and the dog is older, how many years")
My_dog.increment_the_dogs_age(int(additional_years))
print(f"  {My_dog.name} is now {My_dog.age}")

# child code runs from here



My_guard_dog =  guard("Tyson",5)
print(f"{My_guard_dog.name} is my guard dog")
My_guard_dog.warn_about_the_teeth()
My_guard_dog.roll()



