class animal:
   def __init__(self, name, age, colour):
      self.name = name
      self.age = age
      self.colour = colour

class dog(animal):
   def __init__(self, name, age, colour):
      super().__init__(name, age, colour)
   def sit(self):
      print(f"{self.name} is now sitting.")
   def roll(self):
      print(f"{self.name} is now rolling.")
   def eat(self):
      food_menu = {
         "courses":
            [
               {
                  "starter":
                     [
                        "Biscuits",
                        "Chew Stick"
                     ]
               },
               {
                  "main":
                     [
                        "Spare Steak",
                        "Leftover Lasagna",
                        "Floor Food"
                     ]
               },
               {
                  "dessert":
                     [
                        "Ice Cream",
                        "Special Biscuits"
                     ]
               }
            ]
      }
      print(food_menu)
      food_choice = input(f"What would {self.name} like to eat?: ")
      print(f"{self.name} eats the {food_choice}.")

class lizard(animal):
   def __init__(self, name, age, colour):
      super().__init__(name, age, colour)
   def lounge(self, time_to_lounge):
      print(f"{self.name} is lounging for {time_to_lounge}")

class cool_lizard(lizard):
   def __init__(self, name, age, colour, superpower):
      super().__init__(name, age, colour)
      self.superpower = superpower
   def use_super(self):
      if self.superpower.lower() == "flying":
         print(f"{self.name} flies around the room!")
      elif self.superpower.lower() == "strong":
         print(f"{self.name} is so strong he lifts a car!")
      elif self.superpower.lower() == "speed":
         print(f"{self.name} runs 12 times around the earth in seconds!")
      else:
         print("Sorry, we've never seen that superpower before...")

# Define my_dog
dog_name = input("What is your dog's name?: ")
dog_age = input(f"How old is {dog_name}?: ")
dog_colour = input(f"What colour is {dog_name}?: ")
my_dog = dog(dog_name, dog_age, dog_colour)  # Initialize the dog
# Define my_lizard
lizard_name = input("What is your lizard's name?: ")
lizard_age = input(f"How old is {lizard_name}?: ")
lizard_colour = input(f"What colour is {lizard_name}?: ")
is_lizard_super = input(f"Is your lizard a Super Lizard™?: ")
if is_lizard_super.lower() == "yes" or is_lizard_super.lower() == "yah":
   lizard_power = input(f"What is their superpower [Speed/Strong/Flying]?: ")
   my_lizard = cool_lizard(lizard_name, lizard_age, lizard_colour, lizard_power)  # Initialize the SUPER lizard
else:
   my_lizard = lizard(lizard_name, lizard_age, lizard_colour)
is_hot_day = input("Is it a hot day?: ")
if is_hot_day.lower() == "yes" or is_hot_day.lower() == "yah":
   my_dog.sit()
   it_is_this_hot = int(input("How hot is it [C]?: "))
   if it_is_this_hot >= 25:  # If HOT
      my_lizard.lounge(it_is_this_hot * 4)
   elif it_is_this_hot < 25 >= 15:  # If OK
      my_lizard.lounge(it_is_this_hot * 2)
      if is_lizard_super.lower() == "yes" or is_lizard_super.lower() == "yah":
         my_lizard.use_super()
   elif it_is_this_hot < 15:  # If COLD
      print(f"{my_lizard.name} is not lounging because they're too cold!")
   else:
      print("Thermometer comparison broken.")
elif is_hot_day.lower() == "no" or is_hot_day.lower() == "nah":
   my_dog.roll()
else:
   print("Something ain't right...")
exit()