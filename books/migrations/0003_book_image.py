# Generated by Django 4.2.7 on 2023-12-04 14:14

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_featured_image_book_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="placeholder",
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[400, None],
                upload_to="books/",
            ),
            preserve_default=False,
        ),
    ]
