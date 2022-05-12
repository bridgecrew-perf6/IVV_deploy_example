
""" initial """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Class of Migration"""
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
