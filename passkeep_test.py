class user :

  users = ['Maureen', 'Evans']
  caps = string.ascii_uppercase
  numbers = []
  for i in range(0,10):
    numbers.append(str(i))
  special_chars = ['@', '#', '!']  
  name_check = False

  def __init__(self, username, password ):

    self.username = username
    self.password = password

class credentials(user):
  def __init__ (self, instagram, twitter):
    self.instagram = instagram
    self.twitter = twitter
