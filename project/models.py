from django.db import models


class Project(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pic', verbose_name='projects_pic')

    def __str__(self):
        return self.title
    