def count_letters(text: str) -> dict[str, int]:
    """_summary_
        harflarni sanaydi
    Args:
        text (str): _description_
        text parametri stringdan iborat
    Returns:
        dict[str, int]: _description_
        return listni ichida esa harf va
        uni necha marta qatnashganini qaytariladi.
    """
    sanoq = {}
    for i in text:
        sanoq[i] = text.count(i)
    return sanoq   
   
text = 'assalomu alaykum' 

result = count_letters(text) 

print(result)  