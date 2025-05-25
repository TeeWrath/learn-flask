# role based access control
user = {"name": "Jonathan", "access_level": "admin"}

def get_admin_password():
    print("1234")

def make_secure(func):
    def secure_function():
        if(user["access_level"] == "admin"):
            return func()
        else:
            print(f"No admin permission for user {user["name"]}")
        
    return secure_function

get_admin_password = make_secure(get_admin_password)
get_admin_password()