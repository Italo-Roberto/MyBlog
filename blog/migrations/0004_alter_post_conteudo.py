# Generated by Django 4.0.4 on 2022-05-24 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_conteudo_alter_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(),
        ),
    ]
