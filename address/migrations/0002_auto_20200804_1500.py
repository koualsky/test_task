# Generated by Django 3.0.8 on 2020-08-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='city name', max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(help_text='city', on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='city'),
        ),
    ]
