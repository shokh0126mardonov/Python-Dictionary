def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    """ qaysi guruhda qaysi bollar o'qishini saralab beradigan dastur

    Args:
        students (list[dict[str, str]]):
        students parametri listdan iborat bo'ladi listni ichida lug'at bo'ladi lugat esa faqat str key va str valuedan iborat bo'ladi
    Returns:
        dict[str, list[str]]: 
        qiymat qaytaradi lug'at ichida esa key string bo'ladi value esa list bo'ladi
    """
    group = {}
    
    for student in students:
        
        group[student['group']] = []
        
    for student in students:
        group[student['group']].append(student['name'])
    
    return group  


students = [
    {
        'name':'Ali',
        'group':'A'
    },
    {
        'name':'Vali',
        'group':'A'
    },
    {
        'name':'Jon',
        'group':'B'
    },
    {
        'name':'Bob',
        'group':'B'
    },
    {
        'name':'soli',
        'group':'S'
    },
]

result = group_students(students)

print(result)
