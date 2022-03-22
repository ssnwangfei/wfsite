# Generated by Django 3.2.12 on 2022-03-22 02:00

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
            name='UserRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=10, verbose_name='Relationship')),
                ('user_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me_relationships', to=settings.AUTH_USER_MODEL)),
                ('user_you', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_me_relationships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100, verbose_name='User Description')),
                ('telephone', models.CharField(blank=True, max_length=50, verbose_name='Telephone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]