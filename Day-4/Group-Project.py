license_plate = input("What is your license?")

class ParkingGarage():
    def __init__(self, license_plate, parking_spots = 20, total_tickets = 20, customerTicket = {}):
        self.total_tickets = total_tickets
        self.parking_spots = parking_spots
        self.license_plate = license_plate
        self.customerTicket = customerTicket

    def takeTicket(self):
        if self.total_tickets and self.parking_spots !=0:
            self.total_tickets - 1
            self.parking_spots -1
            self.customerTicket[self.license_plate] = False
        else:
            print("Sorry, we are full")

    def payForTicket(self): 
        if False in self.customerTicket :
            payment_amount = input("Please pay $20:\nHow much are you paying?")
            self.customerTicket[license_plate] = True 
        if payment_amount == 20 :
            print("You have already paid.")

        

    def leaveGarage(self):
        if self.customerTicket[license_plate] == True:
            print("Thanks have a nice day")

        else:
            payment_amount = input("Please enter $20:")
            
            

    

    def runner(self):       

        while True:
                
                user_choice= input('\n\n[T]ake a ticket\n[P]ay for parking\n[L]eavea character\n\nWhat would you like to do?  ').lower()

                if user_choice == 't':
                    self.takeTicket()
                

                elif user_choice == 'p':
                    self.payForTicket()
                
                elif user_choice == 'l':
                    self.leaveGarage()
                    
                    print("Thanks you have a nice day")
                    break
                
                else:
                    print('Invalide choice, try again...')  






