class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Jerry")
user_2 = User("002", "Jack")
print(user_1.id)
print(user_2.name)
print(user_1.follower)

user_1.follow(user_2) #user_1 = self, user_2 = user
print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)


