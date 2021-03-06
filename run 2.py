import string

# create variables
users = ['Maureen', 'Evans']
caps = string.ascii_uppercase
numbers = []
for i in range(0,10):
  numbers.append(str(i))
special_chars = ['@', '#', '!']  
name_check = False
instagramusername = "",
instagramusers = []
instagrampass = ""
instagrampasswords = []
twitterusername = "",
twitterusers = []
twitterpass = ""
twitterpasswords = []
social = ""
# handleuser = open("text-user.txt", "a+")
# handleinstagram = open("text-instagram.txt", "a+")
# handletwitter = open("text-twitter.txt", "a+")

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
            print("  ")
            print(f"Hi {username},Welcome to PassKeep!Your account has been successfully created.")
            print("  ")
            print("Here are your social media accounts:")
            print("  ")
            print ("Instagram       Twitter")
            print("  ")
            # handleuser.write(f"{username},{password}:\n")
            social = input("Choose a social media site(Instagram/Twitter):")
            if social == "Instagram":
              #Creating Instagram user
                instagramusername = input ("Enter your Instagram Username:") 
                if 2 <len(instagramusername) < 13:
                  name_check = True
                  instagramusers.append(instagramusername)
                  print("Instagram Username successfully created")
                else:
                  print("Username should contain between 3-12 characters")

                #Creating Instagram password

                instagrampass = input ("Kindly enter your Instagram password:")
                instagrampasswords.append(instagrampass)
                print(f"Your Instagram username is {instagramusername} and your Instagram password is {instagrampass}")
                print("  ")
                print(f"Username : {instagramusers[0]}, Password : {instagrampasswords[0]}")
                # handleinstagram.write(f"{instagramusername},{instagrampass}:\n")
                print (f"User account credentials are Username:{username} Password: {password}")
                print (f"Instagram account credentials are Username:{instagramusername} Password: {instagrampass}")
                # print(handleuser.readline())
                # handleuser.close()
                # print(handleinstagram.readline())
                # handleinstagram.close()
                # print(handletwitter.readline())
                # handletwitter.close()
                break

             #Creating twitter user
            elif social == "Twitter":
                twitterusername = input ("Enter your Twitter Username:") 
                if 2 <len(twitterusername) < 13:
                  name_check = True
                  twitterusers.append(twitterusername)
                  print("Twitter Username successfully created")
                else:
                  print("Username should contain between 3-12 characters")

                #Creating Twitter password

                twitterpass = input ("Kindly enter your Twitter password:")
                twitterpasswords.append(twitterpass)
                print(f"Your Twitter username is {twitterusername} and your Twitter password is {twitterpass}")
                print("  ")
                print(f"Username : {twitterusers[0]}, Password : {twitterpasswords[0]}")
                # handletwitter.write(f"{twitterusername},{twitterpass}:\n")
                print (f"User account credentials are Username:{username} Password: {password}")
                # print(handleuser.readlines())
                print (f"Instagram account credentials are Username:{instagramusername} Password: {instagrampass}")
                # print(handleinstagram.readlines())
                print (f"Twitter account credentials are Username:{twitterusername} Password: {twitterpass}")
                # print(handletwitter.readlines())
                # handletwitter.close()
                break
            else:
              print("Invalid Social media account")
              break
          else:
            print("Your password must be at least 6 characters long")
        else:
          print("Your password must contain at least one number")
      else:
        print("Your password must contain one of these special characters: ('@', '#', '!')")
    else:
      print("Your password must contain at least one uppercase")

     
