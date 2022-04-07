# Generated by Django 4.0.3 on 2022-04-06 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_alter_category_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="review_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Revisado por",
            ),
        ),
    ]