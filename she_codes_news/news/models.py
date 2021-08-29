from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
   # img_url = models.URLField(default='https://placebear.com/200/300')

    #class Meta:
     #   ordering = ['pub_date']
