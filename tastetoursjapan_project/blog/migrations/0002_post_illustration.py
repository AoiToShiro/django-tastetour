# Generated by Django 2.0.2 on 2018-03-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='illustration',
            field=models.ImageField(default="{% static 'images/LogoLarge.svg' %}", upload_to="{% static 'images/blog/' %}"),
        ),
    ]
