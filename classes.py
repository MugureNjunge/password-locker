# import unittest

# class readfiles(unittest.TestCase):


class user :
  """
  new instances of user
  """
  user_list = []
  def  mainlog(self, username, password ):

    self.username = username
    self.password = password
  
  def save_user(self):

    """
    saves any new user to user_list
    """
    user.user_list.append(self)

class credentials :

  def accounts(self, instagram, twitter):
    self.instagram = instagram
    self.twitter = twitter

