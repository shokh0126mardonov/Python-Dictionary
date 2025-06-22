def count_names(names: list[str]) -> dict[str, int]:
    """ Ismlarni sanash

    Args:
        names (list[str]): ismlar ro'yxati

    Returns:
        dict[str, int]: natijasi
    """
    user = {}
    for name in names:
        user[name] = 0
     
    for name in names:
        user[name] = names.count(name)  
        
    return user


names = ['ali', 'vali', 'jon', 'bob', 'ali', 'vali', 'ali', 'vali', 'bob']
result = count_names(names)
print(result)
