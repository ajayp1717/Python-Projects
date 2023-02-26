#basic salary,HRA 10% of basic,TA=5%of basic,tax=2% of Total,Calculate gross salary...
name=input("Enter employee's name: ")
basic=int(input("enter his basic salary:Rs. "))
if basic<0:
    print("Invalid Input")
HRA=.1*basic
TA=.05*basic
Total_salary=basic+HRA+TA
tax=Total_salary*.02
gross_salary=Total_salary-tax
print("Gross salary of an employee is: ",gross_salary,"Rs.")
