from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False)


    def approve(self):
        self.approved_comment=True
        self.save()


    def __str__(self) -> str:
        return self.text
    