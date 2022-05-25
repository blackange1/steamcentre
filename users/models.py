from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = \
        models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = \
        models.ImageField(upload_to='user_photos')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
