from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Категорія', max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField()
    description = RichTextField(verbose_name='Опис', blank=True)
    price = models.DecimalField(
        verbose_name='Ціна', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
