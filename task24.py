def most_common_char(text: str) -> str:
    """_summary_
    text parametri qabul qilgan harflardan eng kop 
    qaysi harf kelganini aniqlovchi funksiya bo'ladi.

    Args:
        text (str): _description_
        text parametrimiz faqatgina  stringlardan iborat bo'ladi.

    Returns:
        str: _description_
        
    """
    group = {}
    
    for ch in text:
        group[ch] = text.count(ch)
        kop_soni =  max(group.values())
    
    for ch in text:
       if group[ch] == kop_soni:
           kop_harf = ch
       
    return f"eng kop kelgan harf {kop_harf} va {kop_soni} ta " 
        
   
    
    
    
    
text = 'kjhzdvjldkcxnmlaaaaaaaaaaaueqfausakjcuewh'
result = most_common_char(text)

print(result)