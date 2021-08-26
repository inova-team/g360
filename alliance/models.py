from django.db import models
from django.utils import timezone
from authentication.models import User

class Alliance(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(editable=False, null=True)
    banner = models.ImageField(upload_to='alliance/banner/', null=True, blank=True)
    type = models.TextField(max_length=50)
    fb_link = models.CharField(max_length=1000, null=True, blank=True)
    instagram_link = models.CharField(max_length=1000, null=True, blank=True)
    twitter_link = models.CharField(max_length=1000, null=True, blank=True)
    website_link = models.CharField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    appear_home = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.banner.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.publication_date = timezone.now()
        return super().save(*args, **kwargs)