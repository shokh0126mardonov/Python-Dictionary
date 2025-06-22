def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    """_summary_
        valuesi 0 dan katta bo'lgan barcha key larni 
        alohida dictionary yaratiladi.
    Args:
        d (dict[str, int]): _description_
        paramtr lug'atdan iborat uning ichida esa key = string values = int
        tipida bo'ladi.
    Returns:
        dict[str, int]: _description_
        lug'at qaytaradigan string va int tipidagi lug'at bo'ladi
    """
    
    group = {}
    
    for key,value in d.items():
        if value > 0:
            group[key] = value
    
    return group
    
d = {
    "olma": 3,
    "anor": 0,
    "banan": 5,
    "gilos": 0
}

result = filter_non_zero(d)  

print(result)