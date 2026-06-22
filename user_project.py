class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password =password
def Display():
  for user in users:
    print(f"firstname : {user.first_name},lastname : {user.last_name},email : {user.email}")      
    pass
def create_user():
  first_name = input("please enter your first name :")
  last_name = input("please enter your last name :")
  email = input("please enter your email :")
  password = input("please enter your password :")
  user = User(first_name,last_name,email,password)
  return user
  
users = []

while True:
    try:
        action = int(input("please choose the action : 1) Create user 2) Display 3) Exit "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        continue

    if action == 1:
        user = create_user()
        users.append(user)
    elif action == 2:
        Display()
    elif action == 3:
        print("the app exiting ....")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")