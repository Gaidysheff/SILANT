# Generated by Django 4.2.2 on 2023-06-10 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='modelMachine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelMachines', to='crm_app.modelmachine'),
        ),
    ]
