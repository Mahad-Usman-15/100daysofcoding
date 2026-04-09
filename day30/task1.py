# Commision Tracker
# Commission = (Hours Logged / Total Project Hours) × (Project Value × Commission %)
import time
isApproved=False
password=input('Enter the password')
# This keyword is only applied in the functions to ensure to use the global variable
global commission
    




if password=="1234":
  
    print("Admin logging in...")
    time.sleep(1)
    hours_logged = float(input("Enter hours logged: "))
    total_project_hours = float(input("Enter total project hours: "))
    project_value = float(input("Enter project value: "))
    commission_percent = float(input("Enter commission percentage: "))
    commission = (hours_logged / total_project_hours) * (project_value * commission_percent)
    enter=input("Enter lock")
    isApproved=True
else:
    print("Incorrect password")    

if isApproved:
    print(f"Commission: {commission}")
else:
    print("Hours rejected")    