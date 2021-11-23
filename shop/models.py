from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catogery=models.CharField(max_length=100 ,default="")
    subcatogery=models.CharField(max_length=100,default="")
    prize=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100 ,default="")
    phone = models.CharField(max_length=100,default="")
    desc = models.CharField(max_length=1000,default="")
    

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_Json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    phone = models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)

     