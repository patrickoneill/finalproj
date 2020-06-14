from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, uniqui=True)
    slug = models.SlugField(max_length=250, uniqui=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def __str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, uniqui=True)
    slug = models.SlugField(max_length=250, uniqui=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCASE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name