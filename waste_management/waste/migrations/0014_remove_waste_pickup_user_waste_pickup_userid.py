# Generated by Django 4.2.1 on 2023-07-05 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0013_alter_waste_pickup_collector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waste_pickup',
            name='user',
        ),
        migrations.AddField(
            model_name='waste_pickup',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='waste.user_registration'),
        ),
    ]