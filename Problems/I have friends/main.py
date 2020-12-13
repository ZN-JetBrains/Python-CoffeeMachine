class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{0} now has {1} friends.".format(self.username, self.friends))
