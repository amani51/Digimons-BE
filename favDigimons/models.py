from django.db import models

# Create your models here.
class Digimon(models.Model):
    name=models.CharField(max_length=255,null=False)
    level=models.CharField(max_length=255,null=False)
    img=models.TextField(default='NO image available!')

    def __str__(self):
        return self.name