from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Tablet_Name = models.CharField(max_length=200)
    Buying_Rate = models.FloatField(null=True)
    Pieces=models.IntegerField(null=True)
    Selling_Rate=models.FloatField(null=True)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    #publish_now=models.BooleanField(default=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #return self.title
        pass
