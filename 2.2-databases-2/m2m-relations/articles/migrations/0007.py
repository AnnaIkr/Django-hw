# Generated by Django 3.1.2 on 2023-02-08 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
    ]