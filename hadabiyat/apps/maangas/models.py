from django.db import models

class Maanga(models.Model):
    maanga_title = models.CharField("title", max_length=200)
    maanga_text = models.TextField("text")
    maanga_publ = models.DateTimeField("Publish date")

class Comment(models.Model):
    maanga = models.ForeignKey(Maanga, on_delete = models.CASCADE)
    author_name = models.CharField("commenator's name", max_length=50)
    comment_text = models.CharField("comment text", max_length=200)

