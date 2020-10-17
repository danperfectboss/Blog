from django.db import models

# Create your models here.
class Publication(models.Model):
    # id = models.AutoField()
    Author = models.TextField(max_length=200)
    Title = models.TextField(max_length=400)
    Content = models.TextField(max_length=10000)
    LinkImage = models.TextField(max_length=1000,default='')
    Facebook = models.BooleanField(default=False)
    Url_facebook = models.TextField(max_length=100,default='')

    Twitter = models.BooleanField(default=False)
    Url_twitter = models.TextField(max_length=100,default='')

    Instagram = models.BooleanField(default=False)
    Url_instagram = models.TextField(max_length=100,default='')

    Linkedin = models.BooleanField(default=False)
    Url_linkedin = models.TextField(max_length=100,default='')

    def __str__(self):
        return self.Title