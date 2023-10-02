# Generated by Django 4.2.1 on 2023-08-08 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UKiyoapp', '0006_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField()),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UKiyoapp.applicant')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UKiyoapp.company')),
                ('packages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UKiyoapp.packages')),
                ('travelAgency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UKiyoapp.travelagency')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
                'db_table': 'bookings',
            },
        ),
    ]