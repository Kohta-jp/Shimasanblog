# Generated by Django 3.2 on 2021-05-19 02:08

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文'),
        ),
    ]
