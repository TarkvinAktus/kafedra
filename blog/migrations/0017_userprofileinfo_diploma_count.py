# Generated by Django 2.2 on 2019-05-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_diploma'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='diploma_count',
            field=models.IntegerField(default=0),
        ),
    ]
