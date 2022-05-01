from django.db import models


class CardOfMainSlider(models.Model):
    title = \
        models.CharField(max_length=200)
    text = \
        models.TextField()
    path_img = \
        models.TextField(max_length=200, null=True)
