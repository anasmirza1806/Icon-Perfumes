from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # Add your custom fields if needed
#     pass
# # Create your models here


STATE_CHOICES = (
    ('Gujrat','Gujrat'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('UP','UP'),
)
class Customer(models.Model):
    # customer_id  = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_name = models.CharField(max_length=20) #name
    customer_email = models.EmailField(max_length=30) #phone
    password = models.CharField(max_length=30,default='')
    # gender = models.CharField(max_length=10)
    # address_Line1 = models.CharField(max_length=50)
    # address_Line2 = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    # state = models.CharField(choices=STATE_CHOICES,max_length=50)
    # pincode = models.IntegerField()
    # mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_name



# CATEGORY_CHOICES = (
#     ('A','Attar'),
#     ('L','Limesticks'),
#     ('P','Perfumes'),
# )
class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(max_length=100)
    description = models.TextField(max_length=100)
    category_id = models.ForeignKey('category', on_delete=models.CASCADE, related_name='products',default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    new_arrival = models.CharField(max_length=20,default='')
    popular_products = models.CharField(max_length=20,default='')

    def __str__(self):
        return (self.product_name)

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=20)
    category_description = models.TextField(max_length=100) 
    category_image = models.ImageField(max_length=100)
    
    def __str__(self):
        return self.category_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return self.cart_id

    @property
    def total_cost(self):
        return float((self.quantity) * (self.product_id.price))

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)
class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address_Line1 = models.CharField(max_length=50)
    address_Line2 = models.CharField(max_length=50, null=True, blank=True)
    products = models.ManyToManyField(Product, through="OrderItem",blank=True)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    subtotal = models.IntegerField()
    gst = models.IntegerField()
    total_amount = models.IntegerField()
    order_status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='pending')
    payment_status = models.CharField(max_length=30,default='pending')
    order_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def _str_(self):
        return str(self.id)
    
    @property
    def total_amount_order(self):
        return str(int(self.quantity) * float(self.product.price))
    
class Payment(models.Model):
    payment_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)


class Feedback(models.Model):
    feedback_id = models.IntegerField()
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    feedback_title = models.CharField(max_length=50)
    feedback_comment = models.CharField(max_length=100)
    feedback_rating = models.IntegerField()
       
