# Generated by Django 5.1.6 on 2025-02-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocate',
            name='practice_area',
        ),
        migrations.AddField(
            model_name='advocate',
            name='practice_areas',
            field=models.ManyToManyField(to='advocates.area'),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='firm',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
