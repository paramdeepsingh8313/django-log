from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    date = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.id) + "_" + self.title