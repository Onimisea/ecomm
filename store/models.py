from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
  def get_queryset(self):
    return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    verbose_name_plural = "categories"
  
  def get_absolute_url(self):
    return reverse('store:category_list', args=[self.slug])

  def __str__(self):
    return self.name


class Subcategory(models.Model):
  category = models.ForeignKey(Category, related_name="subcategory", on_delete=models.PROTECT)
  name = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True)
  
  class Meta:
    verbose_name_plural = "subcategories"

  # def get_absolute_url(self):
  #   return reverse('store:subcategory_list', args=[self.slug])

  def __str__(self):
    return self.name


class Product(models.Model):
  category = models.ForeignKey(Category, related_name="product_category", on_delete=models.PROTECT)
  subcategory = models.ForeignKey(Subcategory, related_name="product_subcategory", on_delete=models.PROTECT)
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True)
  author = models.CharField(max_length=255, default="Admin")
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to="images/", default='images/default.png')
  price = models.DecimalField(max_digits=4, decimal_places=2)
  added_by = models.ForeignKey(User, related_name="vendor", on_delete=models.CASCADE)
  in_stock = models.BooleanField(default=True)
  is_active = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  objects = models.Manager()
  products = ProductManager()
  
  class Meta:
    verbose_name_plural = "products"
    ordering = ("-created",)
  
  def get_absolute_url(self):
    return reverse('store:product_detail', args=[self.slug])
  
  def __str__(self):
    return self.title
