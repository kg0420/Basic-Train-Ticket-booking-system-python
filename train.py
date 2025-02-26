from datetime import datetime

class train:
    def __init__(self,Acfare,Accfare,gfare):
        self.Acfare=Acfare
        self.Accfare=Accfare
        self.gfare=gfare
        self.no_of_gseats=400
        self.Acc_seats=400
        self.Ac_seats=500
        self.user={}
        self.seats={}
    def initialize_seats(self, date):
        if date not in self.seats:
            self.seats[date] = {"General": 400, "Chaired AC": 400, "AC": 500}
    def general(self,no_of_gtickets):
        if no_of_gtickets>self.no_of_gseats: 
            print(f"Sorry! only {self.no_of_gseats} seats are available")    
        elif no_of_gtickets<self.no_of_gseats:
            self.no_of_gseats-=no_of_gtickets
            print(f"Seats available in general coach is {self.no_of_gseats-no_of_gtickets}")

    def Chair_Ac(self,no_of_Acctickets):
        if no_of_Acctickets>self.Acc_seats:
            print(f"Sorry! only {self.Acc_seats} seats are available")
        elif no_of_Acctickets<self.Acc_seats:
            train.Acc_seats-=no_of_Acctickets
            print(f"Seats available in Chaired Ac coach is {self.Acc_seats-no_of_Acctickets}")

    def AC(self,no_of_Actickets):
        if no_of_Actickets>self.Ac_seats:
            print(f"Sorry! only {self.Ac_seats} seats are available")
        elif no_of_Actickets<self.Ac_seats:
            train.Ac_seats-=no_of_Actickets
            print(f"Seats available in AC coach  is {self.Ac_seats}")
    def details(self,name,age,date ,coach,Tickets):
        with open("passenger_details.txt","a") as file:
            file.write(f"Name: {name}, Age: {age}, Date: {date}, Coach: {coach}, Tickets: {Tickets}\n")
    def registration(self):
        print("Enter Your Details for registration")
        phone_number=input("Enter phone no:-")
        print(phone_number)
        username=input("Enter user name:-")
        password=input("Enter Password of min 8 letters:-")
        if not (phone_number.isdigit()) or len(phone_number)!=10:
            print("Invalid phone number")
        elif len(password)<8:
            print("invalid password")
        self.user[username]=[phone_number,password]
        print(self.user)
        print("Registration Successfull")
    def login(self):
        print("please Sign In")
        try:
            username=input("username:-")
            password=input("password:-")
            if username in self.user and self.user[username][1]==password:
                print("login Successful")
                return True
            else:
                print("No User Found.......")
                exit()
        except ValueError:
                print("Invalid input!")
        
            

if __name__=="__main__":
    train.no_of_gseats=400
    train.Acc_seats=400
    train.Ac_seats=500
    obj=train(650,400,150)
    obj.registration()
    obj.login()

    while(True):
         
        print("Welcome to Deccan Queen Express")
        print("1.Check Fare \n2.Book tickets \n3.Train timing \n4.platform Number \n5.Seats Available")
        choice=int(input("Which details you want from above list:- "))
        if choice==1:
            print(f"Fare of Ac Coach is: ₹650\n Fare of Chair AC coach is: ₹400\n Fare of general coach is: ₹150\n ")
        elif choice==3:
            print("pune junction:-3:25 pm \nLonavala Station:-4:30 pm \nKarjat Station:-5:10 pm \nKalyan Junction:- 6:30 pm \nCSMT:8 pm")
        elif choice==4:
            print("platfom no 4(At pune junction)\nplatform no:-2(At Lonavala Station) \nplatform no:-(At Karjat Station)\n platform :-5(Kalyan Junction) \nplatform no:- 1(At CSMT)")
        elif choice==5:
            print(f"Seats Available in General coach is {obj.no_of_gseats}")
            print(f"Seats Available in AC coach is {obj.Acc_seats}")
            print(f"Seats available in chaired AC coach is {obj.Ac_seats}")

        elif choice==2:
            print(f"\nFare of Ac Coach is: 650\n Fare of Chair AC coach is: 400\n Fare of general coach is: 150\n ")
            print("Please Select  Which class Ticket you want to book")
            print("1.Genral\n 2.AC Class\n 3.Chaired AC Class")
            choice2=int(input("Please Select  Which class Ticket you want to book:- "))
            name=input("Enter your name: ")
            age=int(input("Enter your Age: "))
            while True:
                travel_date = input("Enter travel date (YYYY-MM-DD): ")
                try:
                    travel_date = datetime.strptime(travel_date, "%Y-%m-%d").date()
                    if travel_date >= datetime.today().date():
                        break
                    else:
                        print("You cannot book tickets for past dates.")
                except ValueError:
                    print("Invalid date format! Please enter in YYYY-MM-DD format.")
            if choice2==1:
                no_of_gtickets=int(input("Enter the number of tickets you want:- "))            
                obj.details(name,age,"GENERAL",no_of_gtickets)
                obj.general(no_of_gtickets)
                print(f"The {no_of_gtickets} seats are Booked in General coach")
                obj.details(name, age, "GENERAL", no_of_gtickets)
                print("Your requirement is fulllfilled")
                print("Happy Journey......\nRegards \nINDIAN RAILWAY")
                
            elif choice2==2:
                no_of_Actickets=int(input("Enter the number of tickets you want:- "))
                obj.AC(no_of_Actickets)
                print(f"The {no_of_Actickets} seats are Booked in AC coach")
                obj.details(name, age, "AC", no_of_gtickets)
                print("Your requirement is fulllfilled")
                print("Happy Journey......\nRegards \nKrish Gupta")
                   
            if choice2==3: 
                no_of_Acctickets=int(input("Enter the number of tickets you want:- "))
                obj.Chair_Ac(no_of_Acctickets)
                print(f"The {no_of_Acctickets} seats are Booked in Chaired AC coach")
                obj.details(name, age, "Chaired AC", no_of_gtickets)
                print("Your requirement is fulllfilled")
                print("Happy Journey......\nRegards \nKrish Gupta")
        choice3=input("print C to continue and Q to exit the application:- ").islower()
        if choice3=="C":
            continue
        elif choice3=="Q":
            exit()
            
