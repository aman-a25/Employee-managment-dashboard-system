import DB_connector
import random
obj = DB_connector.connectDb()

class emp:
    def __init__(self, e_id,e_name,post,e_sal):
        self.e_id = e_id
        self.e_sal = e_sal
        self.e_name = e_name
        self.post = post

    def __str__(self):
        return f"Employee ID: {self.e_id}\nEmployee Name: {self.e_name}\n Employee post : {self.post}\nEmployee Salary: {self.e_sal}"

def menu(): 
    while True:
        print("\n\n------------------------------------------------------------------------------------------------------------------------------------\n")
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Promote (update) Employee status")
        print("3 to Remove Employee")
        print("4 to Display Employees")
        print("5 exporting data to file")
        print("6 to Exit")
        print("\n------------------------------------------------------------------------------------------------------------------------------------\n")
        
        ch = int(input("Enter your Choice: "))

        if ch == 1:
            Id =int(input("Enter Employee Id: "))
            if obj.check_employee(Id):
                print("Employee already exists. Please try again.")
                continue
    
            Name = input("Enter Employee Name: ")
            Post = input("Enter Employee Post: ")
            Salary = int(input("Enter Employee Salary: "))
            e = emp(Id, Name, Post, Salary)
            print(e)
            obj.insert(e)

            
        elif ch == 2:
            Id = int(input("Enter Employee Id: "))
            if not obj.check_employee(Id):
                print("Employee do not exists. Please try again.")
                continue

            print('1. update name')
            print('2. update post')
            print('3. update salary')

            print("\n-------------------------------------------------------------\n")
            option = int(input('Enter your choice: '))
            if option == 1:
                newname = input("Enter Employee new Name: ")
                obj.update_name(Id,newname)
                print("Employee Name Updated Successfully")

            elif option == 2:
                Post = input("Enter Employee Post: ")
                obj.update_post(Id,Post)
                print("Employee Post Updated Successfully")

            elif option == 3:
                Salary = int(input("Enter Employee Salary: "))
                obj.update_salary(Id,Salary)
                print("Employee Salary Updated Successfully")

            else:
                print("Invalid Choice! Please try again.")
                

        elif ch == 3:
            id = int(input("Enter Employee ID Who you want to remove: "))
            if not obj.check_employee(id):
                print("Employee do not exists. Please try again.")
                return
            otp = random.randint(1000,9999)
            f=open('otp.txt','w')
            f.write(f"{otp}")
            f.close()
            print("OTP has been given to you for verification in otp.txt file")
            print("Enter the OTP to remove the employee")
            user_otp = int(input("Enter OTP: "))
            if user_otp == otp:
                obj.delete_employee(id)
                print("Employee Removed Successfully")
            else:
                print("Invalid OTP! Please try again.")

        elif ch == 4:
            obj.display()

        elif ch == 5:
            
            print("choose in which file format you want to export")
            print("1. txt")
            print("2. csv")
            print("3. excel")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                f=open('employee.txt','w')
                f.write("Employee ID,Employee Name,Employee Post,Employee Salary\n")
                cur=obj.con.cursor()
                cur.execute("select * from emp")
                for row in cur:
                    f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
                f.close()
                print("Data Exported Successfully to employee.txt file")
            elif choice == 2:
                f=open('employee.csv','w')
                f.write("Employee ID,Employee Name,Employee Post,Employee Salary\n")
                cur=obj.con.cursor()
                cur.execute("select * from emp")
                for row in cur:
                    f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
                f.close()
                print("Data Exported Successfully to employee.csv file")
            elif choice == 3:
                f=open('employee.xlsx','w')
                f.write("Employee ID,Employee Name,Employee Post,Employee Salary\n")
                cur=obj.con.cursor()
                cur.execute("select * from emp")
                for row in cur:
                    f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
                f.close()
                print("Data Exported Successfully to employee.xlsx file")
            else:
                print("Invalid Choice! Please try again.")

        elif ch == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid Choice! Please try again.")

