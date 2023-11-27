from django.db import models
from django.db.models.query import QuerySet
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField
class PublishedManager(models.Manager):
    def get_queryset(self):
       return super(PublishedManager,self).get_queryset().filter(status='published')


class Categories(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(null=False,unique=True,db_index=True,editable=False)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)


    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
            return reverse('blog:blogs_by_category',args=[self.slug])
  

class Post(models.Model):
    STATUS_CHOICE=(
        ('draft','Draft'),
        ('published','Published'),
    )

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish',unique=True,db_index=True)
    image=models.ImageField(upload_to="images")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=RichTextField()
    
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    objects=models.Manager()
    published=PublishedManager()
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
            return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)



class Comment(models.Model):
     post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
     name=models.CharField(max_length=80)
     email=models.EmailField()
     body=models.TextField()
     created=models.DateTimeField(auto_now_add=True)
     updated=models.DateTimeField(auto_now=True)
     active=models.BooleanField(default=True)
     class Meta:
        ordering=('created',)

     def __str__(self):
        return f'comment by {self.name} on {self.post}'



# Create your models here.
