user = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]
 
 
for active in user:
    active['active'] = False

print(user)