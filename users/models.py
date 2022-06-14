from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = \
        models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = \
        models.ImageField(upload_to='user_photos')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Comment(models.Model):
    text = \
        models.CharField(max_length=500)

    user = \
        models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'comment id{self.id} of user {self.user}'


class SubComment(models.Model):
    text = \
        models.CharField(max_length=500)

    user = \
        models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    comment = \
        models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'subcomment id{self.id} of user {self.user}'
