users = {
    'first_name':'Shohjahon',
    'last_name':'Mardonov',
    'year' : '2006'
}

key = input("search key input : ")

if key in users:
    users.pop(key)
    print(users)
else:
    print('Bunaqa kalit mavjud emas')