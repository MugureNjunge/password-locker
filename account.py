import random
import string
# import pyperclip

class User:
    """
    class User generates new instances users.
    """
    users = []

    def __init__(self, username, password):
        """
        method that defines the user properties
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        saves new user to the user list
        """
        User.users.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.users

    def delete_user(self):
        '''
        deletes saved accounts from the list
        '''
        User.users.remove(self)

class Credentials():
    """
    class credentials creates new objects of credentials
    """
    accounts = []
    @classmethod
    def verify_user(cls,username, password):
        """
        verify if user is in our users data
        """
        user_1 = ""
        for user in User.users:
            if(user.username == username and user.password == password):
                    user_1 == user.username
        return user_1

    def __init__(self,account,userName, password):
        """
        defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        add new credential to the credentials list
        """
        Credentials.accounts.append(self)

    def delete_accounts(self):
        """
        method that deletes an account credentials from the accounts
        """
        Credentials.accounts.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """
        Method that returns a credential that matches given account name.
        """
        for credential in cls.accounts:
            if credential.account == account:
                return credential
    