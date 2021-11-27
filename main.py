from instafollowers import InstaFollower
# Username of insta
# user = "mebel83229"
# password of insta
# pass_ = "skabdulhaq"
user_name = input("Username of insta\n")
password = input("Password of insta\n")
page = input("Enter page link of instagram page => ")
insta_followers = InstaFollower(page, user_name, password)

