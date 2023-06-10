# Generated by Django 4.2.2 on 2023-06-10 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModelDriveAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModelEngine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModelMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModelSteeringAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModelTransmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenanceDate', models.DateField()),
                ('operatingTime', models.IntegerField()),
                ('workOrder', models.CharField(max_length=255)),
                ('workOrderDate', models.DateField()),
                ('executor', models.CharField(max_length=255)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.modelmachine')),
                ('serviceCompany', models.ManyToManyField(to='crm_app.servicecompany')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceTypes', to='crm_app.maintenancetype')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=255)),
                ('serialNumberEngine', models.CharField(max_length=255)),
                ('serialDriveAxle', models.CharField(max_length=255)),
                ('serialSteeringAxle', models.CharField(max_length=255)),
                ('deliveryContract', models.CharField(max_length=255)),
                ('shipmentDate', models.DateField()),
                ('consignee', models.CharField(max_length=255)),
                ('deliveryAddress', models.CharField(max_length=255)),
                ('additionalOptions', models.TextField(default='Комплектация не указана')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
                ('modelDriveAxle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelDriveAxles', to='crm_app.modeldriveaxle')),
                ('modelEngine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelEngines', to='crm_app.modelengine')),
                ('modelMachine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.modelmachine')),
                ('modelSteeringAxle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelSteeringAxles', to='crm_app.modelsteeringaxle')),
                ('modelTransmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelTransmissions', to='crm_app.modeltransmission')),
                ('serviceCompany', models.ManyToManyField(to='crm_app.servicecompany')),
            ],
        ),
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operatingTime', models.IntegerField()),
                ('breakdownDate', models.DateField()),
                ('breakdownDescription', models.TextField()),
                ('usedSpareParts', models.TextField()),
                ('recoverDate', models.DateField()),
                ('downtime', models.IntegerField()),
                ('breakdownNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breakdowns', to='crm_app.breakdown')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.modelmachine')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recoveryMethods', to='crm_app.recoverymethod')),
                ('serviceCompany', models.ManyToManyField(to='crm_app.servicecompany')),
            ],
        ),
    ]
