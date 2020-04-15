from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Tablet_Name = models.CharField(max_length=200)
    Buying_Rate = models.FloatField(null=True)
    Pieces=models.IntegerField(null=True)
    Selling_Rate=models.FloatField(null=True)
    Profit=models.FloatField(default=0.0,null=True)
    @property
    def calc_profit(self):
       return self.Selling_Rate-self.Buying_Rate
    
    
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    #publish_now=models.BooleanField(default=True)
    def save(self,*args,**kwargs):
        self.Profit=self.calc_profit
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.Tablet_Name)
