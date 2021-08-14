from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    banner = models.ImageField(upload_to='category/banner')
    responsable = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    has_father = models.BooleanField(default=False)
    category_father = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.banner.delete()
        super().delete(*args, **kwargs)