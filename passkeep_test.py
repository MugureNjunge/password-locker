class user :

  def __init__(self, username, password ):

    self.username = username
    self.password = password

class credentials(user):
  def __init__ (self, instagram, twitter):
    self.instagram = instagram
    self.twitter = twitter
