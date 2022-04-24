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
 





    

# class credentials(user):
#   def __init__ (self, instagram, twitter):
#     self.instagram = instagram
#     self.twitter = twitter
