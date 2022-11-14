
# class Car:
#     def __init__(self, licenseNumber):
#         self.licenseNumber = licenseNumber

# class ParkingSlot:
#     def __init__(self, row, spotNumber, level, car):
#         self.row = row
#         self.spotNumber = spotNumber
#         self.level = level
#         self.car = car

#     def isAvailable(self):
#         return self.car == None
    
#     def park(self, vehicle):
#         self.car = vehicle

#     def removeVehicle(self):
#         self.car = None

# class Level:
#     def __init__(self, rows, levelNumber):
#         self.levelNumber = levelNumber
#         self.rows = rows
#         self.spotsPerRow = 2
#         self.parkingSlots = []
#         self.availableSpots =  rows * self.spotsPerRow

#     def findAvailableSlot(self):
#         if(self.availableSpots <=0):
#             return None
#         else:
#             if(len(self.parkingSlots)== 0):
#                 return ParkingSlot(0,0,0, None)
#             else:
#                 lastCarParked = self.parkingSlots[-1]

#             if(lastCarParked.spotNumber<self.spotsPerRow):
#                 return ParkingSlot(lastCarParked.row, lastCarParked.spotNumber+1,self.levelNumber,None)
#             if(lastCarParked.row<self.rows):
#                 return ParkingSlot(lastCarParked.row+1,0,self.levelNumnber,None)
            
#     def park(self, vehicle):

#         freeParkingSpot = self.findAvailableSlot()
#         if(not(freeParkingSpot)):
#             return False

#         else:
#             freeParkingSpot.park(vehicle)

# class ParkingLot:
#     def __init__(self, levels):
#         self.levels = levels
    
#     def park(self, car):
#         for level in self.levels:
#             if(level.park(car)):
#                 return True
#             else:
#                 continue
        
#         return False

################## CHARACTER CREATION ##################

class Characters():
    def __init__(self, name, realm, char_class, race):
        self.name = name
        self.realm = realm
        self.race = race
        self.char_class = char_class
        self.char_list = {}
        self.char_list2 = {}
        self.num_of_characters = 0

    def create_character(self):
        
        name = input('What is your name, stranger? ').title()
        realm = input('Which realm will you traverse? GOOD, CHAOS or EVIL: ' ).upper()
        self.char_list[name] = realm
        self.num_of_characters += 1
        race = input('Which race will you be? HUMAN, ELF, DWARF: ').title()
        char_class = input('What class shall you pursue? THIEF, MAGE, WARRIOR, NECROMANCER, EMPATH, RANGER: ').title()
        self.char_list2[race] = char_class
        print(f"{name} the {race} {char_class} has been added to {realm}. ")

    def show_character_list(self):
        print(f"- - - CURRENT CHARACTER LIST - - -")
        print(f"Character Count: {self.num_of_characters}")
        for k,v in self.char_list.items():
            print(k,v)
    
    # def show_character(self):
    #     print(f"- - - CURRENT CHARACTER LIST - - -")
    #     print(f"Character Count: {self.num_of_chracters}")
    #     for k,v in self.char_list.items() and self.char_list2():
    #         print(k,v)
    #     name= input('Which character would you like to view?')
    #     if name in self.char_list:
    #         print(f"{name} is a {self.race} {self.char_class} in the realm of {self.realm})")
    #     else:
    #         print('Character does not exist in any realm!')

    def delete_character(self):
        name = input('Which player would you like eradicated?').title()
        if name in self.char_list:
            print(f"{name} the {self.race} {self.char_class} has been wiped off the realm of {self.realm}!)")
            del self.char_list[name]
            self.num_of_characters -=1
        else:
            print('Character does not exist in any realm!')

    
       
    def runner(self):
            while True:
                print('\n- - - WELCOME TO THE REALM OF THIEVES - - -')
                user_choice= input('\n\n[C]REATE a new character\n[L]IST your characters\n[D]ELETE a character\n[Q]UIT\n\nWhat would you like to do?  ').lower()

                if user_choice == 'c':
                    self.create_character()
                

                elif user_choice == 'l':
                    self.show_character_list ()
                
            
                # elif user_choice == 'v':
                #     self.show_character()
                

                elif user_choice == 'd':
                    self.delete_character() 
                
                elif user_choice == 'q':
                    self.show_character_list()
                    print('Good luck on your journey!')
                    break
                else:
                    print('Invalide choice, try again...')  

user_sean = Characters("","","","")

user_sean.runner()




        

    
  





    


