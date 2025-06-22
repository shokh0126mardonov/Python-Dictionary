def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    """_summary_

    Args:
        users (dict[str, dict[str, bool  |  str]]): _description_
        users lug'atdan iborat bo'ladi lug'at ichida esa 
    Returns:
        list[str]: _description_
    """
    group = []
    
    for key,value in users.items():
        if value["active"] == True:
            group.append(key)
        
    return group

users = {
    "Ali": {
        "active": True,
        "role": "admin"
    },
    "Vali": {
        "active": False,
        "role": "moderator"
    },
    "Sami": {
        "active": True,
        "role": "user"
    },
    "Laylo": {
        "active": False,
        "role": "user"
    },
    "Diyor": {
        "active": True,
        "role": "editor"
    }
}

result = get_active_users(users)

print(result)    