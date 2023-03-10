# Generated by Django 4.1.6 on 2023-02-13 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopy_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout', models.BooleanField(default=False)),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopy_api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopy_api.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
