from django.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=120)
    state_name = models.TextField()
    stats = models.TextField()
    
    def _str_(self):
        return self.title
        