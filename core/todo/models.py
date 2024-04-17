from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ToDo(models.Model):
    '''
    it's a models for todo app related to user
    '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=350)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.task
    
    class Meta:
        order_with_respect_to = 'author'
        