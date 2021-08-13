from django.db import models
from django.utils import timezone
import math
from category_article.models import Category
from authentication.models import Staff


class Article(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    author = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(editable=False, null=True)
    pdf = models.FileField(upload_to='article/pdfs/')
    banner = models.ImageField(upload_to='article/banner/', null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.banner.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.publication_date = timezone.now()
        return super().save(*args, **kwargs)