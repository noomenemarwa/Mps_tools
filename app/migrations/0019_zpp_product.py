# Generated by Django 4.0.5 on 2022-10-31 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='zpp',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
