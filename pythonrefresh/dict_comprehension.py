users = [
    (0,"Bob","password" ,),
    (1,"Ryan", "123456789",),
    (2,"Rolf","56789",),
]

username_mapping = {user[1] : user for user in users}

print(username_mapping["Bob"])