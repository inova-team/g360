# Generated by Django 2.2.13 on 2021-08-26 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category_article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=5000)),
                ('publication_date', models.DateTimeField(editable=False, null=True)),
                ('pdf', models.FileField(upload_to='article/pdfs/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='article/banner/')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_article.Category')),
            ],
        ),
    ]
