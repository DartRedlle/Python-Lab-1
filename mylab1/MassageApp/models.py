from django.db import models
from django.conf import settings
# Create your models here.

class Massage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header = models.CharField(max_length=250)
    text = models.TextField()
    def SaveMassage(self):
        self.save()

    def str(self):
        return self.title