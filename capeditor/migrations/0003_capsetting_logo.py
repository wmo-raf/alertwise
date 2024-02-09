# Generated by Django 4.1.10 on 2024-02-07 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('capeditor', '0002_alter_capsetting_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capsetting',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo of the sending institution'),
        ),
    ]
