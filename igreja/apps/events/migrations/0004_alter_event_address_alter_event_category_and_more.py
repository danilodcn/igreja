# Generated by Django 4.0.3 on 2022-06-07 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_remove_profile_social_media_contactmeans_user"),
        ("financial", "0002_alter_payment_number_of_installments"),
        ("church", "0003_churchministry_remove_ministry_description_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0003_alter_eventpaymentoption_max_installment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="account.address",
                verbose_name="Endereço",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.category",
                verbose_name="Categoria",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="church",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="church.church",
                verbose_name="Igreja",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="Fim"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="events.event",
                verbose_name="Evento",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="financial.payment",
                verbose_name="Pagamento",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Atualizado por",
            ),
        ),
    ]