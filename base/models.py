from django.db import models

class PlantsProducts(models.Model):
    type = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['type','price']
 
    def __str__(self):
           return self.type