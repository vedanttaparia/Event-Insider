# Generated by Django 3.0.5 on 2020-04-26 01:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='clubdefault.jpg', upload_to='club_images\\')),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('insta', models.URLField(blank=True, null=True)),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('club_joined', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.club')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='defaultpost.jpg', upload_to='event_images\\')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.club')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.BlogComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.post_event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
