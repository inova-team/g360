from django.db import models

# Create your models here.
from django.utils import timezone

from authentication.models import Staff


class Event(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    user_register = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="event_user_register")
    user_last_update = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="event_user_last_update")
    date_register = models.DateTimeField(editable=False)
    date_last_update = models.DateTimeField(editable=True, null=True)
    date_event = models.DateTimeField(editable=True)
    responsible = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="event_responsable")
    banner = models.ImageField(upload_to='article/banner/', null=True, blank=True)
    link_event = models.CharField(max_length=1000)
    link_form = models.CharField(max_length=500)
    number_participants = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.banner.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_register = timezone.now()
        self.date_last_update= timezone.now()
        return super().save(*args, **kwargs)