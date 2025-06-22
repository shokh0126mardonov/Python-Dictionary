users = [
    {
    'name' : 'shohjahon',
    'age' : 20,
    'last_name': 'mardonov'
    },
    
    {
    'name' : 'Ali',
    'age' : 12,
    'last_name': 'Valiyev'
    },
    
    {
    'name' : 'sardor',
    'age' : 99,
    'last_name': 'salohiddinov'
    },
    
]

max = users[0]['age']

for user in users:
    if user['age'] > max:
        max = user['age']

print(max)



