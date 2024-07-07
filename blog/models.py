from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Category(models.Model):
    name = models.CharField(max_length=20)
        
# Create your models here.
class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
