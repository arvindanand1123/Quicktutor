<<<<<<< HEAD
# Generated by Django 3.0.2 on 2020-04-03 02:40
=======
# Generated by Django 3.0.2 on 2020-04-05 17:33
>>>>>>> mattbranch

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
<<<<<<< HEAD
=======
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
>>>>>>> mattbranch
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(default=None, verbose_name='date account created')),
                ('picture', models.URLField(default='https://source.unsplash.com/random/200×200/?fruit', max_length=500)),
                ('classes', models.CharField(default='None', max_length=400)),
                ('helped', models.BooleanField(default=False)),
                ('is_tutor', models.BooleanField(default=False)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
