# Generated by Django 3.2.9 on 2021-12-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_link_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='img_url',
            field=models.URLField(blank=True),
        ),
    ]