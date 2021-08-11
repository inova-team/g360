from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    document_number= models.CharField(max_length=20)
    banner = models.ImageField(upload_to='staff/banner/', null=True, blank=True)
    number_contact = models.CharField(max_length=20)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    admission_date = models.DateTimeField(editable=False)
    departure_date = models.DateTimeField(editable=False, null=True, blank=True)

    def __str__(self):
        return str(self.user.first_name + " " + self.user.last_name)

    def delete(self, *args, **kwargs):
        self.banner.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.admission_date = timezone.now()
        if not self.is_active:
            self.departure_date = timezone.now()
        return super().save(*args, **kwargs)