# Generated by Django 4.1.7 on 2023-02-28 02:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_productimage_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productimage",
            name="name",
        ),
    ]
