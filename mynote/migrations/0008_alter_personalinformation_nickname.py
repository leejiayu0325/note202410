# Generated by Django 4.2.16 on 2024-10-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mynote", "0007_personalinformation_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinformation",
            name="nickname",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
