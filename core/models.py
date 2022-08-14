from email.policy import default
from pyexpat import model
from django.db import models
from django.conf import settings

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=5000  , null=True)
    subtitle = models.CharField(max_length=200, blank = True, null = True)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish', null = True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',null = True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank = True,default='default.png',null = True)
    publish = models.DateTimeField(default=timezone.now, null = True)
    
    created = models.DateTimeField(auto_now_add=True,null = True)
    updated = models.DateTimeField(auto_now=True, null = True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',null = True)
    featured = models.BooleanField(default = False, null =True)
    tags = TaggableManager()
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


        
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


# comment system
class Comment(models.Model):
    #related name allows me to post.comments.all()
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80, null = True)
    email = models.EmailField(null = True)
    body = models.TextField(null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now=True,null = True)
    #we can use this active feature to manually deactivate a comment
    active = models.BooleanField(default=True, null = True)
    featured = models.BooleanField(default = False, null = True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
