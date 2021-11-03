# Generated by Django 3.2.7 on 2021-09-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0006_auto_20200615_2046"),
    ]

    operations = [
        migrations.AddField(
            model_name="polarisstellaraccount",
            name="muxed_account",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="polarisstellaraccount",
            unique_together={("memo", "account", "muxed_account")},
        ),
    ]