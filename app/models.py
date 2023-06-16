
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Customer(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     name = models.CharField(max_length=200)
     locality =models.CharField(max_length=200)
     city = models.CharField(max_length=50)
     zipcode =models.IntegerField()
     state = models.CharField(choices=STATE_CHOICES,max_length=50)

     def __str__(self):
        return str(self.id)

class Category(models.Model):
    url=models.CharField(max_length=100 ,null=True)
    cat_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to='category/',null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%"  />'.format(self.image))

    def __str__(self):
        return self.title


class Product (models.Model):
    url=models.CharField(max_length=100,null=True)
    title= models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    brand =models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    product_image =models.ImageField(upload_to='product',null=True)

    def image(self):
            return format_html('<img src="/media/{} " style="width:40px;height:40px;border-radius:50%"  />'.format(self.product_image))

    def image_tag(self):
            return format_html('<img src="/media/{} " style="width:50px;height:75px;"  />'.format(self.product_image))

    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return str(self.id)
    # @property
    # def total_cost(self):
    #     return self.quantity * self.product.discounted_price

STATUS_CHOICE =(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('OnTheWay','On-The-Way'),
    ('Delivered','Delivered'),
    ('Cancle','Cancle'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default="Pending")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

