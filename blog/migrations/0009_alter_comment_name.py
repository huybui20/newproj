# Generated by Django 4.1.3 on 2022-11-30 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_remove_comment_email_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
