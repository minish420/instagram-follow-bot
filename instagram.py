from instapy import InstaPy

session = InstaPy(username = "_datanaut_", password = "12121212444dddssss")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["bmw", "women"], amount = 3)
session.set_dont_like(["nsfw"])

session.end()