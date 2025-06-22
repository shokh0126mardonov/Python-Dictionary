
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """_summary_
    listni ichidagi so'zlarni uzunligiga qarab guruhlab qo'shadi

    Args:
        words (list[str]): _description_
        words paramteri listdan iborat list esa string qiymat qabul qiladi.
        
    Returns:
        dict[int, list[str]]: _description_
        return lug'at ichida string qiymat qaytaradi.
    """
    
    group = {}
    
    for word in words:
        group[len(word)] = []
    
    
    for word in words:
           group[len(word)].append(word)
    
    return group
    
words = ["olma", "banan", "uzum", "gilos", "anor"]
  
result = group_by_length(words)

print(result)