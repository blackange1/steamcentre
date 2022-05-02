from django.db import models


class MainSlider(models.Model):
    title = \
        models.CharField(max_length=200)
    text = \
        models.TextField()
    img = \
        models.ImageField(upload_to='main_slider')
