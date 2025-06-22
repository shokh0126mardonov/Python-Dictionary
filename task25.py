def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    """_summary_
    bir xil yoshdagi odamlarni bitta listga yig'amiz.
    Args:
        people (list[dict[str, int  |  str]]): _description_
        people parametri listdan iborat list ichida esa lug'at bor
        lugatimiz esa key,value = str va int va key,value = str va 
        str dan iborat
    Returns:
        dict[int, list[str]]: _description_
        lug'at qaytarib unda esa int va uni listi bo'ladi.
    """
    group = {}
    
    for i in people:
        age = i["age"]
        group[age] = []
        
    for i in people:
        age = i["age"]
        name = i["name"]
        group[age].append(name)

    return group

people = [
     {"name": "Ali", "age": 20},
     {"name": "Vali", "age": 21},
     {"name": "Soli", "age": 20},
     {'name':"shohjahon","age":19}
          ]

result = group_by_age(people)

print(result) 