def count_names(names: list[str]) -> dict[str, int]:
    """ ismlarni sanaydi

    Args:
        names (list[str]): 
        names parametri listdan iborat bo'ladi list esa string matnlardan iborat bo'ladi

    Returns:
        dict[str, int]:
        bu esa Dictionary esa matn va int qiymat qaytarishi kerak
    """
    user = {}
    
    for name in names:
        user[name] = names.count(name)
      
    for name in names :
        pass
         
    
    return user

names = ['ali','vali','bob','vali','ali','bob','jon','ali']

result = count_names(names)

print(result)