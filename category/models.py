from django.db import models
from django.urls import reverse


class category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name