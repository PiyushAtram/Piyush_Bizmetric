import sys
class Choice:

    def __init__(self):
        self.subjects = ["HR", "Finance", "Marketing", "DS"]
        self.fees = 200000.0
        self.amount=200000.0
        self.analyt=0.0
        self.hostel=0.0
        self.food=0.0
        self.transport=0.0


    def select_subject(self):
        try:
            print("Available subjects:", self.subjects)
            self.s = input("Enter your subject: ")

            if self.s not in self.subjects:
                print("Please select a valid subject from above list")
                return False
            return True
        except:
            print(sys.exc_info())


    def add_analytics(self):
        try:
            a = input("Having Analytics (yes/no): ")
            if a.lower() == "yes":
                self.fees += self.fees * 0.1
                self.analyt= self.fees * 0.1
        except:
            print(sys.exc_info())

    def add_hostel(self):
        try:
            self.h = input("Do you want hostel (yes/no): ")
            if self.h.lower() == "yes":
                d = int(input("For how many years (digit): "))
                self.fees += d * 200000
                self.hostel= d * 200000
        except:
            print(sys.exc_info())

    def add_food(self):
        try:
            if self.h=='yes':
                f = input("Do you want food in hostel (yes/no): ")
                if f.lower() == "yes":
                    c = int(input("For how many months (digit): "))
                    self.fees += c * 2000
                    self.food=c*2000
                else:
                    pass
        except:
            print(sys.exc_info())

    def add_transport(self):
        try:
            t = input("Do you want transport facility (yes/no): ")
            if t.lower() == "yes":
                p = int(input("For how many semesters: "))
                self.fees += p * 13000
                self.transport=p*13000
        except:
            print(sys.exc_info())
class CollegeFees(Choice):
    def __init__(self):
        super().__init__()
        if self.select_subject(): 
            self.add_analytics()
            self.add_hostel()
            self.add_food()
            self.add_transport()
            self.print_bill()
        else:
            print("enter valid course: ")

    def print_bill(self):
        print("{:^30}".format("Total Amount"))
        print("-"*30)
        print("{:<15}".format(self.s),end="")
        print("{:>10}".format(str(self.amount)))
        print("{:<15}".format("Analytics"),end="")
        print("{:>10}".format(str(self.analyt)))
        print("{:<15}".format("Hostel"),end="")
        print("{:>10}".format(str(self.hostel)))
        print("{:<15}".format("Food"),end="")
        print("{:>10}".format(str(self.food)))
        print("{:<15}".format("Transport"),end="")
        print("{:>10}".format(str(self.transport)))
        print("-"*30)
        print("{:<15}".format("Total"),end="")
        print("{:>10}".format(str(self.fees)))
    
obj = CollegeFees() 