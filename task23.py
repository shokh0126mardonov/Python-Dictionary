def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    """ dastur har bitta xil elementni qaysi 
    indexda ekanligini aniqlab beradi.
    Args:
        numbers (list[int]): _description_
        numbers parametri listdan iborat list esa faqat
        butun sonlardan iborat bo'ladi

    Returns:
        dict[int, list[int]]: _description_
        funksiya esa lug'at ichida butun son va list 
        ko'rinishida esa uni indexlarini aniqlab beradi.
    """
    group = {}
    index = 0
    
    for number in numbers:
        group[number] = []
    
    for number in numbers:
        group[number].append(index)
        index+=1
    
    return group


numbers = [1, 2, 1, 3, 2, 1]

result = group_indices(numbers)

print(result)