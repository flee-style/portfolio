from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.content