# Generated by Django 2.0.2 on 2018-03-01 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tips', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='note作者'),
        ),
        migrations.AddField(
            model_name='tips',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tips.TipsCategory', verbose_name='note类目'),
        ),
        migrations.AlterUniqueTogether(
            name='tipscategory',
            unique_together={('code', 'category_type')},
        ),
    ]
