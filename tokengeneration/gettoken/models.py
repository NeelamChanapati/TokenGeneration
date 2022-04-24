from django.db import models

# Create your models here.
class token(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    ph_no = models.IntegerField()
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.name