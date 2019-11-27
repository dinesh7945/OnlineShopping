from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=200)
    # product_category = models.CharField(max_length=200)
    product_category = models.CharField(max_length=50, default="")
    product_price = models.CharField(max_length=5)
    # product_price= models.IntegerField(default=0)
    product_image = models.ImageField(upload_to = "shop/images",default="")
    # method add and overtite
    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,default="")
    phone = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name
    
class Register(models.Model):
    Register_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=12)
    phone = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=10)
    
    def __str__(self):
            return self.name

    