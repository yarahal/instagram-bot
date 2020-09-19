from instagrambot import InstagramBot

Bot = InstagramBot()
username = input("Username: @")
Bot.setUsername(username)
Bot.downloadUserPosts()

