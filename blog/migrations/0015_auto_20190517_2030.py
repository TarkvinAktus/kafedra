# Generated by Django 2.2 on 2019-05-17 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190517_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studydoc',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='blog.Course'),
        ),
    ]
