from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=100)

class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendList')
    friend = models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)

