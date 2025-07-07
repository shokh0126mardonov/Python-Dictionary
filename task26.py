def merge_dicts(a: dict, b: dict) -> dict:
    """_summary_
    berilgan value qiymatlarini solishtirib chiqaman.
    2 ta lug'atni solishtiramiz agar bir xil key bo'lsa
    ularning qaysi birini value qiymat katta bo'lsa o'shani olamiz.
    
    Args:
        a (dict): _description_
        b (dict): _description_
        2 ta lug'at bo'ladi
        

    Returns:
        dict: _description_
        return lug'at
    """
    result = {}
    result.update(a)
    result.update(b)
    return result


student = {
    'first_name' : 'shohjahon',
    'age' : 19,
    'region':'Buxoro',
    'last_name':'Mardonov'
}    
teacher = {
    'first_name' : 'Diyorbek',
    'age' : 25,
    'region':'Jizzax'
}    

result = merge_dicts(student,teacher)

print(result)