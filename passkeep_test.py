class user :

  users = ['Maureen', 'Evans']
  caps = string.ascii_uppercase
  numbers = []
  for i in range(0,10):
    numbers.append(str(i))
  special_chars = ['@', '#', '!']  
  name_check = False

  # ensuring username starts with caps
  def add_name(name):
    if name.title() in users :
      return False
    else:
      return True

      # ensuring username contains no numbers
  def number_added(name):
    found = False
    for number in numbers:
      if name.find(number)> -1:
        found =True
    return found  

    # ensure password has uppercase
  def caps_added(pw):
    found = False
    for letter in caps :
      if pw.find(letter) >-1:
        found = True
    return found  

    #  ensure password has special characters 
  def special_added(pw):
    found = False
    for char in special_chars:
      if pw.find(char) >-1:
        found = True
    return found  

    # username and password validation
  while True:
    # username validation
    if not name_check:
      username = input ("Enter your username:") 
      if add_name(username):
        if not number_added(username):
          if 2 <len(username) < 13:
            name_check = True
            users.append(username)
            print("Username successfully created")
          else:
            print("Username should contain between 3-12 characters")
        else :
          print("Username should only contain letters")
      else:
        print("Username taken, Please choose another username:")

        # password validation
    else:
      password = input ("Kindly enter your password:")
      if caps_added(password):
        if special_added(password):
          if number_added(password):
            if len(password) >5:
              print(f"Your username is {username} and your password is {password}")
              break
            else:
              print("Your password must be at least 6 characters long")
          else:
            print("Your password must contain at least one number")
        else:
          print("Your password must contain one of these special characters: ('@', '#', '!')")
      else:
        print("Your password must contain at least one uppercase")

  





      

  # class credentials(user):
  #   def __init__ (self, instagram, twitter):
  #     self.instagram = instagram
  #     self.twitter = twitter
