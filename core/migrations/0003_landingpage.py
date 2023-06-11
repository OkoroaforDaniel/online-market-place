# Generated by Django 4.2.1 on 2023-06-10 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_mymodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default value', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
                ('is_sold', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landing_pages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]