from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hostname+'  '+str(self.timestamp)


class Preference(models.Model):
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.key+'  '+str(self.value)