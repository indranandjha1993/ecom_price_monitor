# Generated by Django 4.2.6 on 2023-10-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]
