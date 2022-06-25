from django.conf import settings
from django.db import models
from methodical_material.models import EduMaterial


class Profile(models.Model):
    user = \
        models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    img = \
        models.ImageField(upload_to='user_photos', null=True, blank=True)

    collection_material = \
        models.ManyToManyField(EduMaterial, related_name='collection')

    liked = \
        models.ManyToManyField(EduMaterial, related_name='liked')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


# Favorite
# class UserCollectionMaterial(models.Model):
#     user = \
#         models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     material = \
#         models.ManyToManyField(EduMaterial)


class Comment(models.Model):
    edu_material = \
        models.ForeignKey(EduMaterial, on_delete=models.CASCADE)

    user = \
        models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    text = \
        models.CharField(max_length=500)

    date = \
        models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'comment id{self.id} of user {self.user}'


class SubComment(models.Model):
    text = \
        models.CharField(max_length=500)

    user = \
        models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    comment = \
        models.ForeignKey(Comment, on_delete=models.CASCADE)

    date = \
        models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'subcomment id{self.id} of user {self.user}'
