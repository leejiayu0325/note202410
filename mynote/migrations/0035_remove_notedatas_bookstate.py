# Generated by Django 4.2.16 on 2024-10-24 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mynote", "0034_notedatas_bookstate_alter_creatuser_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notedatas",
            name="bookstate",
        ),
    ]
