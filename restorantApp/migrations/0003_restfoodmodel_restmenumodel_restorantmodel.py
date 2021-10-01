# Generated by Django 3.1 on 2021-04-05 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restorantApp', '0002_auto_20210405_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='restorantModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=1000)),
                ('rest_owner_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('rest_owner_phone', models.IntegerField(blank=True, null=True)),
                ('rest_phone', models.IntegerField(blank=True, null=True)),
                ('rest_addres', models.CharField(blank=True, max_length=10000, null=True)),
                ('rest_area', models.CharField(blank=True, max_length=1000, null=True)),
                ('rest_city', models.CharField(blank=True, max_length=1000, null=True)),
                ('rest_state', models.CharField(blank=True, max_length=1000, null=True)),
                ('rest_country', models.CharField(blank=True, max_length=1000, null=True)),
                ('rest_opntime', models.TimeField(blank=True, null=True)),
                ('rest_clstime', models.TimeField(blank=True, null=True)),
                ('rest_type', models.CharField(blank=True, max_length=500, null=True)),
                ('rest_image', models.CharField(blank=True, max_length=10000, null=True)),
                ('rest_reg_date', models.DateTimeField()),
                ('rest_dislike', models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL)),
                ('rest_like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('root_usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='restMenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu', models.CharField(max_length=3000)),
                ('spacial', models.CharField(blank=True, max_length=3000, null=True)),
                ('offer', models.CharField(blank=True, max_length=3000, null=True)),
                ('restorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restorantApp.restorantmodel')),
            ],
        ),
        migrations.CreateModel(
            name='restFoodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=3000)),
                ('food_image', models.CharField(blank=True, max_length=5000, null=True)),
                ('food_description', models.TextField(blank=True, max_length=10000, null=True)),
                ('food_prize', models.PositiveIntegerField()),
                ('veg', models.BooleanField(blank=True, null=True)),
                ('nonveg', models.BooleanField(blank=True, null=True)),
                ('egg', models.BooleanField(blank=True, null=True)),
                ('Menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restorantApp.restmenumodel')),
                ('food_dislike', models.ManyToManyField(related_name='fooddislike', to=settings.AUTH_USER_MODEL)),
                ('food_like', models.ManyToManyField(related_name='foodlike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
