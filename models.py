# liveblog/models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
  title = models.CharField(blank=False, null=False)
  author = models.ForeignKey(User, related_name='posts')
  created = models.DateTimeField(u'Date Created', blank=False, null=False, default=datetime.now)
  slug = models.SlugField(prepopulate_from=("title",))
  def __str__(self):
    return self.title

class PostItem(models.Model):
  post = models.ForeignKey(Post, related_name='items')
  created = models.DateTimeField(u'Date Created', blank=False, default=datetime.now)
  image = models.ImageField(upload_to="uploads", blank=True)
  content = models.TextField(blank=True)

  def __str__(self):
    return "Post Item for '%s' created at %s" % \
            (self.post.title, self.created.strftime('%I:%M %p %Z'))
