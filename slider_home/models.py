from django.db import models

# Create your models here.
from article.models import Article
from event.models import Event


class SliderItem(models.Model):
    EVENT = 'EVENT'
    ARTICLE = 'ARTICLE'
    item_choices = [
        (EVENT, 'Event'),
        (ARTICLE, 'Article')
    ]
    type_item = models.CharField(max_length=10,choices=item_choices)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.event is None:
            return self.event.name
        else:
            return self.article.name