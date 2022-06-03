# Generated by Django 4.0.3 on 2022-06-02 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventpaymentoption",
            name="max_installment",
            field=models.PositiveIntegerField(
                default=1, verbose_name="Numero máximo de parcelas"
            ),
        ),
    ]
