# Generated by Django 4.2.13 on 2024-07-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=32)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('location', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('repassword', models.CharField(max_length=32)),
            ],
        ),
    ]
