class User:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = raw_input("enter the email: ")
        password = raw_input("enter the password:")

        if(email == self.email and password == self.password):
            print "Login Successful"
        else:
            print("Login Faild")

    def logout(self):
        login = False
        print("log out")

    def islogin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.islogin():
             print "name is:"+self.name, '\n' , "email is:"+self.email
        else:
            print ('user is not log in')


user1 = User()

user1.name = 'nahid'
user1.email = 'hasan'
user1.password = '12345'


user1.profile()
user1.login()
user1.profile()
user1.logout()


