# Generated by Django 2.2 on 2019-05-17 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_studydoc_common'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studydoc',
            name='course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='blog.Course'),
        ),
    ]
