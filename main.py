# # imutible int , str , float , tuple , boolen
# #murible list,dictionary,set

# """Dictionary lug'atlarda faqatgina imutibllar ishlatiishi mumkin"""

# person = {
#     "first_name" : "Shohjahon",
#     "last_name" : "Mardonov",
#     "age" : "21",
#     "phone" : "+998940810126",
#     "cars" : ['malibu','kobalt','jentra','matiz'],
   
#     }

# """Dictionaryda qanqa keylar va valuelar bor ekanlligini aniqlab olamiz?"""

# items = person.items()

# print(items)   



# """Dictionaryda qanqa keylar bor ekanlligini aniqlab olamiz?"""

# values = person.values()

# print(values)   
    
# """Dictionaryda qanqa keylar bor ekanlligini aniqlab olamiz?"""

# keys = person.keys()

# print(keys)   
    

# """Dictionary elementiga ya'ni keyga murojaat qilish murojat qilishni o'rganamiz!"""

# age = person.get("age",False)

# print(age)

# print(age)


# name = input("name : ")
# age = input("age : ")
# phone = input("phone : ")

# royxat = {
#     "name" : name,
#     "age" : age,
#     "phone" : phone
# }

# print(royxat)

users = {
    'first_name' : 'shohjahon',
    'last_name' : "Mardonov",
    'age' : '21'
}

users['phone'] = '+998_94_081_01_26'

print(users)