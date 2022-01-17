from django.db import models
from django.db.models.fields import BigIntegerField

import user

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    mobile = BigIntegerField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50, null=True)


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(height_field=None,
                            width_field=None, max_length=None)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    brief = models.TextField()
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
