# Generated by Django 5.0.2 on 2024-03-12 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mashapp', '0003_create_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='mashapp.category'),
        ),
    ]
