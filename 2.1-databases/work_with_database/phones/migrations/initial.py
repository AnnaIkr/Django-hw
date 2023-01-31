from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.CharField(max_length=15)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=70)),
            ],
        ),
    ]