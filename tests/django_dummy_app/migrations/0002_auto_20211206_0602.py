# Generated by Django 2.2.24 on 2021-12-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_dummy_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="null_field",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="continent",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
