# Generated by Django 4.0.3 on 2022-04-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_resume"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="test",
            field=models.BooleanField(default=False, verbose_name="Em teste"),
        ),
        migrations.AddField(
            model_name="post",
            name="visualizations",
            field=models.IntegerField(
                default=0, editable=False, verbose_name="Visualizações"
            ),
        ),
    ]
