# Generated by Django 4.1.3 on 2022-11-29 14:23

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_upload',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default=[1], to='blog.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
