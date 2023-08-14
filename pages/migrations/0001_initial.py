# Generated by Django 4.2.3 on 2023-07-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='clothes/%Y%m%d/')),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('author_num', models.PositiveIntegerField()),
                ('condition', models.CharField(blank=True, choices=[('New', 'NEW'), ('Used', 'USED')], default='New', max_length=4, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
