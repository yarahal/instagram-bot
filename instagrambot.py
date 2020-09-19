import downloadinstaposts


class InstagramBot:
    def __init__(self):
        self.username = ""

    def setUsername(self, username):
        self.username = username

    def downloadUserPosts(self):
        if(self.username == ""):
            print("You must initialize a username")
        else:
            downloadinstaposts.download_instagram_posts(self.username)
