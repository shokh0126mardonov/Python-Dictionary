users = {
    'first_name' : 'Shohjahon',
    'last_name' : 'Mardonov',
    'age' : '19'
} 

kalit = input("users_key : ")

if kalit in users:
    print(users[kalit])
else:
    print("topilmadi")