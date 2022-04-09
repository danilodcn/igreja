# Generated by Django 4.0.3 on 2022-04-09 15:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Novo'), (1, 'Escrevendo'), (2, 'Aguardando revisão'), (3, 'Aguardando publicação'), (3, 'Publicado')], default=0, verbose_name='Status')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=255, verbose_name='Subtítulo')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem')),
                ('document', models.FileField(blank=True, null=True, upload_to='', verbose_name='Documento')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Conteúdo')),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de publicação')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de revisão')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Título')),
                ('comment', models.TextField(help_text='Comentário com até 500 caracteres', max_length=500, verbose_name='Comentário')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.post')),
            ],
            options={
                'verbose_name': 'Revisão',
                'verbose_name_plural': 'Revisões',
                'ordering': ['-review_date'],
            },
        ),
    ]
