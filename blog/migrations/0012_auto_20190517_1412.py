# Generated by Django 2.2 on 2019-05-17 11:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190517_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studydoc',
            name='document',
            field=models.FileField(upload_to=blog.models.content_file_name),
        ),
    ]
