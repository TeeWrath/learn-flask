import functools

# role based access control
user = {"name": "Jonathan", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if(user["access_level"] == access_level):
                return func()
            else:
                print(f"No {access_level} level permission for user {user["name"]}")
        
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    print("admin: 1234")
    
@make_secure("user")
def get_dashboard_password():
    print("user: user password")

# print(get_admin_password.__name__)
get_admin_password()
get_dashboard_password()