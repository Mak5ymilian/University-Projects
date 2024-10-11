#Creates a class for the laptop
class Laptop:
    def spec_list(self): #self references instance of class
        print("The specifications for the chosen laptop are:\n\t"
              #self.XXXXX displays variables in the class
              + self.display,'\n\t' 
              + self.touchscreen,'\n\t'
              + self.cpu,'\n\t'
              + self.ram,'\n\t'
              + self.gpu,'\n\t'
              + self.storage,'\n\t'
              )
        
#variables
laptop = Laptop() #Uses laptop variable for self
total_price = [] #Empty list for price of laptop components

#Asks for user input for the budget
def budget():

    #makes budget1 a global variable
    global budget1 
    while True:
        
        try: #error handling if user inputs a non digit value
            budget1 = float(input("Please enter your budget from 160-925: "))

            if 160 > budget1 or budget1 > 925:
                print("Budget out of range\n")
                continue
                
            
            #breaks loop if budget is not out of range
            else:
                break
            
        
            #returns the global variables new value
            return budget1

        #prevents program from quitting due to error
        except ValueError:
            print("You entered a non digit value. Try again\n")
            
#Introduction to program
def intro():
    print("""
Welcome to the laptop chooser program!
This program will choose the perfect laptop for you based on your choices!
The laptop may be slightly above or below the budget to see whether you would
need to spend more for it to be perfect or for future price reductions.
Lets start!

"""
          )
    global budget1
    while True:

        choice = input("Do you have a budget? (y/n)").lower()
        #.lower() is a function that returns values in lowercase

        if choice == "y":
            budget() #runs the budget funtion
            break

        elif choice == "n":
            print("Okay")
            budget1= 1000 #Asigns value greater than maximum budget
            break

        else:
            print("Invalid option chosen. Try again\n")

    return budget1


#Displays options for display of laptop    
def display_choice():
    print("""
Laptops have different display sizes.
Choose a number based on the size you would like to have:

1) 17 inches
2) 15 inches
3) 13 inches
4) 11 inches
"""
          )
    while True:

        display_size = input("The number you will choose is (1-4): ")
        

        if display_size == "1":
            print("You have chosen the 17 inch display\n")
            laptop.display = "17' Display"
            total_price.append(100)
            break

        elif display_size == "2":
            print("You have chosen the 15 inch display\n")
            laptop.display = "15' Display"
            total_price.append(75)
            break

        elif display_size == "3":
            print("You have chosen the 13 inch display\n")
            laptop.display = "13' Display"
            total_price.append(50)
            break

        elif display_size == "4":
            print("You have chosen the 11 inch display\n")
            laptop.display = "11' Display"
            total_price.append(25)
            break

    #If an option other than 1-4 is chosen then it will ask again until a
    #correct answer is chosen
        else:
            print("You have chosen an invalid option. Try again\n")

def display_choice1():
    print("""
Laptops have different display sizes.
Choose a number based on the size you would like to have:

1) 13 inches
2) 11 inches
"""
          )
    while True:

        display_size = input("The number you will choose is (1 or 2): ")

        if display_size == "1":
            print("You have chosen the 13 inch display\n")
            laptop.display = "13' Display"
            total_price.append(50)
            break

        elif display_size == "2":
            print("You have chosen the 11 inch display\n")
            laptop.display = "11' Display"
            total_price.append(25)
            break

        else:
            print("You have chosen an invalid option. Try again\n")

    
def display_choice2():
    print("""
Laptops have different display sizes.
Choose a number based on the size you would like to have:

1) 15 inches
2) 13 inches
3) 11 inches
"""
          )
    while True:

        display_size = input("The number you will choose is (1-3): ")
        

        if display_size == "1":
            print("You have chosen the 15 inch display\n")
            laptop.display = "15' Display"
            total_price.append(75)
            break

        elif display_size == "2":
            print("You have chosen the 13 inch display\n")
            laptop.display = "13' Display"
            total_price.append(50)
            break

        elif display_size == "3":
            print("You have chosen the 11 inch display\n")
            laptop.display = "11' Display"
            total_price.append(25)
            break

        else:
            print("You have chosen an invalid option. Try again\n")
            

#Yes or no for touchscreen choice
def touchscreen_choice():
    while True:

        #returns string in lower case
        choice = input("Would you like to have a touchscreen display? (y/n)").lower()

        if choice == "y":
            print("The laptop will have a touchscreen display\n")
            laptop.touchscreen = "Touchscreen"
            total_price.append(50)
            break
            
        elif choice =="n":
            print("The laptop will not have a touchscreen display\n")
            laptop.touchscreen = "No Touchscreen"
            total_price.append(0)
            break
            
        else:
            print("You have not chosen a valid option. Try again\n")

#Displays options for appropriate CPU and RAM
def cpu_choice():
    print("""
Now we will determine the CPU and RAM for the laptop.
Choose a number based on how you will be typically using the laptop:

1) Simple programs that do not require heavy CPU
   usage and minimal multitasking e.g.:
       *Watching Movies
       *Surfing on the internet
       
2) Simple programs or programs that are slightly
   more demanding with multitasking e.g.:
        *Having many applications open at once
        *Many tabs open in web browser

3) Programs that require heavy CPU usage e.g.:
        * Video editing
        * High FPS gaming

4) Highest performing CPU that will not slow down
   the laptop whilst supporting business applications
   and intensive multitasking
   
"""
          )
    while True:

        cpu = input("The number you will choose is (1-4): ")

        if cpu == "1":
            print("You have chosen the Intel Pentium Processor with 4GB RAM\n")
            laptop.cpu = "Intel Pentium" #asigns values to laptop class
            laptop.ram = "4GB  RAM"
            total_price.append(100)#appends price to the list
            total_price.append(10)
            break

        elif cpu == "2":
            print("You have chosen the Intel Core i3 Processor with 8GB RAM\n")
            laptop.cpu = "Intel Core i3"
            laptop.ram = "8GB  RAM"
            total_price.append(150)
            total_price.append(25)
            break

        elif cpu == "3":
            print("You have chosen the Intel Core i5 Processor with 16GB RAM\n")
            laptop.cpu = "Intel Core i5"
            laptop.ram = "16GB RAM"
            total_price.append(200)
            total_price.append(50)
            break
        
        elif cpu == "4":
            print("You have chosen the Intel Core i7 Processor with 32GB RAM\n")
            laptop.cpu = "Intel Core i7"
            laptop.ram = "32GB RAM"
            total_price.append(300)
            total_price.append(75)
            break

    #If an option other than 1-4 is chosen then it will ask again until a
    #correct answer is chosen
        else:
            print("You have chosen an invalid option. Try again\n")

def cpu_choice1():
    print("""
Now we will determine the CPU and RAM for the laptop.
Choose a number based on how you will be typically using the laptop:

1) Simple programs that do not require heavy CPU
   usage and minimal multitasking e.g.:
       *Watching Movies
       *Surfing on the internet
       
2) Simple programs or programs that are slightly
   more demanding with multitasking e.g.:
        *Having many applications open at once
        *Many tabs open in web browser
   
"""
          )
    while True:

        cpu = input("The number you will choose is (1 or 2): ")

        if cpu == "1":
            print("You have chosen the Intel Pentium Processor with 4GB RAM\n")
            laptop.cpu = "Intel Pentium" #asigns values to laptop class
            laptop.ram = "4GB  RAM"
            total_price.append(100)#appends price to the list
            total_price.append(10)
            break

        elif cpu == "2":
            print("You have chosen the Intel Core i3 Processor with 8GB RAM\n")
            laptop.cpu = "Intel Core i3"
            laptop.ram = "8GB  RAM"
            total_price.append(150)
            total_price.append(25)
            break

    #If an option other than 1-4 is chosen then it will ask again until a
    #correct answer is chosen
        else:
            print("You have chosen an invalid option. Try again\n")

def cpu_choice2():
    print("""
Now we will determine the CPU and RAM for the laptop.
Choose a number based on how you will be typically using the laptop:

1) Simple programs that do not require heavy CPU
   usage and minimal multitasking e.g.:
       *Watching Movies
       *Surfing on the internet
       
2) Simple programs or programs that are slightly
   more demanding with multitasking e.g.:
        *Having many applications open at once
        *Many tabs open in web browser

3) Programs that require heavy CPU usage e.g.:
        * Video editing
        * High FPS gaming
   
"""
          )
    while True:

        cpu = input("The number you will choose is (1-3): ")

        if cpu == "1":
            print("You have chosen the Intel Pentium Processor with 4GB RAM\n")
            laptop.cpu = "Intel Pentium" #asigns values to laptop class
            laptop.ram = "4GB  RAM"
            total_price.append(100)#appends price to the list
            total_price.append(10)
            break

        elif cpu == "2":
            print("You have chosen the Intel Core i3 Processor with 8GB RAM\n")
            laptop.cpu = "Intel Core i3"
            laptop.ram = "8GB  RAM"
            total_price.append(150)
            total_price.append(25)
            break

        elif cpu == "3":
            print("You have chosen the Intel Core i5 Processor with 16GB RAM\n")
            laptop.cpu = "Intel Core i5"
            laptop.ram = "16GB RAM"
            total_price.append(200)
            total_price.append(50)
            break
        
    #If an option other than 1-4 is chosen then it will ask again until a
    #correct answer is chosen
        else:
            print("You have chosen an invalid option. Try again\n")


#Yes or no option for GPU
def gpu_option():

    global budget1
    while True:

        #returns string in lower case
        choice = input("Will you be playing games on the laptop?(y/n)").lower()

        if choice == "y":
            print("Okay\n")
            if budget1 >= 701:
                #runs function to choose gpu
                gpu_choice()
                break
            elif budget1 <= 700:
                gpu_choice1()
                break
            break
            
        elif choice =="n":
            print("The laptop will not have a dedicated GPU")
            laptop.gpu = "No Gaming GPU"
            total_price.append(0) #Asigns value to avoid error
            break
            
        else:
            print("You have not chosen a valid option. Try again\n")

#Choice for GPU
def gpu_choice():
        print("""
Choose a number based on how you will be typically using the GPU:

1) Low graphical intensive games designed
   to run older games but not newest games
       
2) GPU capable to run latest games at minimal
   settings.

3) High intensive games that can be ran on highest
   quality or high fps with good quality

4) Best possible GPU that can run all games
   with the best possible quality and highest fps
   
"""
        )
        while True:

            gpu = input("The number you will choose is (1-4): ")

            if gpu == "1":
                print("You have chosen the GTX 1650 GPU")
                laptop.gpu = "GTX 1650 GPU"
                total_price.append(100)
                break

            elif gpu == "2":
                print("You have chosen the GTX 1660TI GPU\n")
                laptop.gpu = "GTX 1660TI GPU"
                total_price.append(150)
                break

            elif gpu == "3":
                print("You have chosen the RTX 2070 GPU\n")
                laptop.gpu = "RTX 2070 GPU"
                total_price.append(200)
                break
            
            elif gpu == "4":
                print("You have chosen the RTX 3090 GPU\n")
                laptop.gpu = "RTX 3090 GPU"
                total_price.append(300)
                break

        #If an option other than 1-4 is chosen then it will ask again until a
        #correct answer is chosen
            else:
                print("You have chosen an invalid option. Try again\n")

def gpu_choice1():
        print("""
Choose a number based on how you will be typically using the GPU:

1) Low graphical intensive games designed
   to run older games but not newest games
       
2) GPU capable to run latest games at minimal
   settings.

3) High intensive games that can be ran on highest
   quality or high fps with good quality
   
"""
        )
        while True:

            gpu = input("The number you will choose is (1-3): ")

            if gpu == "1":
                print("You have chosen the GTX 1650 GPU")
                laptop.gpu = "GTX 1650 GPU"
                total_price.append(100)
                break

            elif gpu == "2":
                print("You have chosen the GTX 1660TI GPU\n")
                laptop.gpu = "GTX 1660TI GPU"
                total_price.append(150)
                break

            elif gpu == "3":
                print("You have chosen the RTX 2070 GPU\n")
                laptop.gpu = "RTX 2070 GPU"
                total_price.append(200)
                break

        #If an option other than 1-4 is chosen then it will ask again until a
        #correct answer is chosen
            else:
                print("You have chosen an invalid option. Try again\n")
          
#storage option
def storage_choice():
    print ("""
Please specify the amount of storage you want.
Storage is offered from 128GB to 1TB(1000GB)
Enter the storage in GB and the appropriate
storage size will be chosen.
"""
           )
    
    while True:
        try:
            storage = float(input("Please enter storage size in GB: "))

            #Asigns variable if in the chosen range
            if storage in range(1,129): 
                print ("128GB chosen\n") 
                laptop.storage = "128GB Storage"
                total_price.append(25)
                break

            elif storage in range(129,257):
                print ("256GB chosen\n") 
                laptop.storage = "256GB Storage"
                total_price.append(50)
                break

            elif storage in range(257,513):
                print ("512GB chosen\n") 
                laptop.storage = "512GB Storage"
                total_price.append(70)
                break

            elif storage in range(513,1001):
                print ("1TB chosen\n") 
                laptop.storage = "1TB Storage"
                total_price.append(100)
                break

            else:
                print ("Incorrect value chosen. Try again\n")

        except ValueError:
            print("You entered a non digit value. Try again")

def storage_choice1():
    print ("""
Please specify the amount of storage you want.
Storage is offered from 128GB to 256GB
Enter the storage in GB and the appropriate
storage size will be chosen.
"""
           )
    
    while True:
        try:
            storage = float(input("Please enter storage size in GB: "))

            #Asigns variable if in the chosen range
            if storage in range(1,129): 
                print ("128GB chosen\n") 
                laptop.storage = "128GB Storage"
                total_price.append(25)
                break

            elif storage in range(129,257):
                print ("256GB chosen\n") 
                laptop.storage = "256GB Storage"
                total_price.append(50)
                break

            else:
                print ("Incorrect value chosen. Try again\n")

        except ValueError:
            print("You entered a non digit value. Try again")

def invoice():
    
    #Sums all the prices in list
    total = sum(total_price)
    print ("The total price for the configured laptop is: ", total)

    if budget1 == 1000:
        print("No budget was configured")
    
    elif budget1 < total:
        print("The configured laptop is above the budget\n")

    elif budget1 >= total:
        print("The configured laptop is within the budget\n")
    
    
    while True:
        #asks fot invoice
        choice = input("Would you like an invoice for the laptop? (y/n)").lower()

        if choice == "y":
            laptop_invoice = open("Invoice.txt","wt") #opens txt file for writing and text
            #writes variables from class and prices
            laptop_invoice.write("-----------------------------------------------------\n")
            laptop_invoice.write("\t\tLaptop Specifications\n")
            laptop_invoice.write("-----------------------------------------------------\n")
            laptop_invoice.write("\tHardware\t\tPrice\n")
            laptop_invoice.write("\t" + laptop.display + "\t\t" + (str(total_price[0])) + "\n")
            laptop_invoice.write("\t" + laptop.touchscreen + "\t\t" + (str(total_price[1])) + "\n")
            laptop_invoice.write("\t" + laptop.cpu + "\t\t" + (str(total_price[2])) + "\n")
            laptop_invoice.write("\t" + laptop.ram + "\t\t" + (str(total_price[3])) + "\n")
            laptop_invoice.write("\t" + laptop.gpu + "\t\t" + (str(total_price[4])) + "\n")
            laptop_invoice.write("\t" + laptop.storage + "\t\t" + (str(total_price[5])) + "\n")
            laptop_invoice.write("-----------------------------------------------------\n")
            laptop_invoice.write("\tTotal Price: " + "\t\t" + (str(total)) + "\n")
            laptop_invoice.write("-----------------------------------------------------\n")
            laptop_invoice.close()#closes txt file
            print("Invoice printed")
            break

        elif choice == "n":
            print("Okay an invoice will not be printed\n")
            break

        else:
            ("Invalid option chosen. Try again\n")
            
#runs program and asigns functions to budget
def main():      
    intro()
    if budget1 >= 701: 
        display_choice()
        touchscreen_choice()
        cpu_choice()
        gpu_option()
        storage_choice()

    elif 160 <= budget1 <= 325:
        display_choice1()
        touchscreen_choice()
        cpu_choice1()
        storage_choice1()
        laptop.gpu = "No Gaming GPU"
        total_price.append(0) #Asigns value to avoid error

    elif 325 < budget1 <= 700:
        display_choice2()
        touchscreen_choice()
        cpu_choice2()
        gpu_option()
        storage_choice()

    laptop.spec_list()
    invoice()
    total_price.clear() #clears the total price

    #asks for another go
    while True:
        again = input("would you like to have another go? (y/n)").lower()

        if again == "y":
            main()
            break

        elif again == "n":
            break

        else:
            print("Invalid option chosen. Try again\n")


main()
input("\n\nPress Enter key to exit")
