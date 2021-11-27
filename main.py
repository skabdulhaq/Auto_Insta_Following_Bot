from instafollowers import InstaFollower


user_name = input("Username of insta\n")
password = input("Password of insta\n")
page = input("Enter page link of instagram page => ")
insta_followers = InstaFollower(page, user_name, password)

