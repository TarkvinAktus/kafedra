# Generated by Django 2.2 on 2019-05-22 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190522_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labinfoname', to='blog.LabInfo'),
        ),
    ]