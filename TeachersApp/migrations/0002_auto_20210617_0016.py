# Generated by Django 3.1.6 on 2021-06-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeachersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='profilepic',
            field=models.ImageField(upload_to='uploads/profilepic/'),
        ),
    ]