from instapy import InstaPy 
  
session = InstaPy(username="your username",password="your password") 
session.login()
session.like_by_tags(["cybersecurity", "books", "animation"], amount=10, interact=True)