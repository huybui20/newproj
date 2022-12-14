# Generated by Django 4.1.3 on 2022-11-29 14:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_content_upload_alter_post_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content_upload',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
