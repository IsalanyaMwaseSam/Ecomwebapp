from audioop import add
from termios import TIOCGWINSZ
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.conf import settings


CATEGORY_CHOICES = (
    ('F', 'Fashion'),
    ('El', 'Electronics'),
    ('HB', 'Health & Beauty'),
    ('G', 'Gardening'),
    ('SP', 'Sports'),
    ('HO', 'Home & Office'),
)

LABEL_CHOICES = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'Danger'),
)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    seller = models.CharField(max_length=200, blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    characteristics = models.TextField(max_length=3000, null=True)
    description = models.TextField(max_length=3000, null=True)
    specifications = models.TextField(max_length=3000, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("homeapp:product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("homeapp:add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("homeapp:remove-from-cart", kwargs={'slug': self.slug})

    @property
    def image1URL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url
    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url
    @property
    def image4URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url

class Cart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    
    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    def get_final_price(self):
        return self.get_total_discount_product_price()



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


    
    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_final_price()
        return total

class FlashSales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name_plural = 'Flash sales'

class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

class Billing(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    other_names = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)