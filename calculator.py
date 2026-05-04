while True:
#Take two numbers

   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))

   print("Numbers are", a, b)

#Choose operation

   print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
   choice = input("Enter your choice: ")

#Perform calculation

   if choice == "1":
    print("Result:", a + b)
   elif choice == "2":
    print("Result:", a - b)
   elif choice == "3":
    print("Result:", a * b)
   elif choice == "4":
    print("Result:", a / b)
   else:
    print("Invalid choice")

#Add Loop (Make it continous)

   again = input("Do you want to continue? (yes/no): ")
   if again.lower() != "yes":
        break