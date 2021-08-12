from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Word_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    banner = models.ImageField(upload_to='word_category/banner')
    register_date = models.DateTimeField(editable=False, null=True)
    register_author = models.ForeignKey(User,related_name="register_author_wc", null=True, blank=True, on_delete=models.CASCADE)
    update_date = models.DateTimeField(editable=True, null=True)
    update_author = models.ForeignKey(User,related_name="update_author_wc", null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.banner.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.register_date = timezone.now()
        return super().save(*args, **kwargs)


class Words(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField(max_length=1000)
    category = models.ForeignKey(Word_Category, null=True, blank=True, on_delete=models.CASCADE)
    register_date = models.DateTimeField(editable=False, null=True)
    register_author = models.ForeignKey(User, related_name="register_author_w", null=True, blank=True, on_delete=models.CASCADE)
    update_date = models.DateTimeField(editable=True, null=True)
    update_author = models.ForeignKey(User,related_name="update_author_w", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.register_date = timezone.now()
        return super().save(*args, **kwargs)
