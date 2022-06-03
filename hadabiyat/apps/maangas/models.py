import datetime
from distutils.command.upload import upload
from operator import mod 
from django.db import models
from django.utils import timezone

class Maanga(models.Model):
    maanga_title = models.CharField("title", max_length=200)
    maanga_text = models.TextField("text")
    maanga_publ = models.DateTimeField("Publish date")
    
    def  __str__(self):
        return self.maanga_title

    def was_published_recently(self):
        return self.maanga_publ >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    maanga = models.ForeignKey(Maanga, default=None, on_delete = models.CASCADE)
    author_name = models.CharField("commenator's name", max_length=50)
    comment_text = models.CharField("comment text", max_length=200)

    def  __str__(self):
        return self.author_name

class Chapter(models.Model):
    maanga = models.ForeignKey(Maanga, default=None, on_delete = models.CASCADE)
    chapter_page = models.ImageField("chapter page")

