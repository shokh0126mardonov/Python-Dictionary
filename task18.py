student = {
    "name": "Ali", 
    "age": '25', 
    "grade": "A"
}


for keys,value in student.items():
    print(f"{keys.upper()} : {value.capitalize()}")