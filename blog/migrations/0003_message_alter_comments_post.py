# Generated by Django 4.1.5 on 2023-01-16 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_delete_blog_comments_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.CharField(max_length=1500)),
            ],
        ),
        migrations.AlterField(
            model_name="comments",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.post",
                verbose_name="Article",
            ),
        ),
    ]
