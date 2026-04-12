# This is called linear search
class Student:
    roll_number: int
    total_marks: int

result_list = [
    {"roll_number": 101, "total_marks": 445},
    {"roll_number": 102, "total_marks": 390},
    {"roll_number": 103, "total_marks": 412},
    {"roll_number": 104, "total_marks": 325},
    {"roll_number": 105, "total_marks": 478},
    {"roll_number": 106, "total_marks": 210},
    {"roll_number": 107, "total_marks": 385},
    {"roll_number": 108, "total_marks": 456},
    {"roll_number": 109, "total_marks": 298},
    {"roll_number": 110, "total_marks": 415}
]

def distinction():
    max_student=result_list[0]
    for result in result_list:
      if result["total_marks"]>max_student["total_marks"]:
           max_student=result
      
    return  max_student  
    
userinput=int(input("Enter your roll_number:"))

for result in result_list:
    if result["roll_number"]==userinput:
        re1=distinction()
        if result["roll_number"]==re1["roll_number"]:
            print("You got highest")
            print(result)
            break
        print(result)