from django.db import models  
class Laptop(models.Model):  
    lid = models.IntegerField()  
    lname = models.CharField(max_length=100)  
    picture = models.ImageField()
    lbrand = models.CharField(max_length=50)  
    lproc = models.CharField(max_length=15)
    lstock = models.CharField(max_length=3, default='No')
    lprice = models.IntegerField(default='0')
    class Meta:  
        db_table = "Laptop"  