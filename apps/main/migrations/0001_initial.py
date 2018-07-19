# Generated by Django 2.0.1 on 2018-07-18 11:56

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
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=50, verbose_name='蛋糕名')),
                ('cake_img', models.CharField(max_length=256, verbose_name='列表图')),
                ('cake_price', models.CharField(default=10000, max_length=10, verbose_name='原价')),
                ('cake_number', models.CharField(default=1, max_length=10, verbose_name='库存')),
                ('cake_discount', models.CharField(default=10000, max_length=10, verbose_name='现价')),
                ('cake_detail', models.TextField(verbose_name='详情')),
            ],
            options={
                'verbose_name': '添加蛋糕',
                'verbose_name_plural': '添加蛋糕',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_type', models.CharField(max_length=20, verbose_name='类别')),
                ('is_active', models.BooleanField(default=False, verbose_name='筛选')),
            ],
            options={
                'verbose_name': '添加类别',
                'verbose_name_plural': '添加类别',
            },
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(max_length=20, verbose_name='口味')),
                ('is_active', models.BooleanField(default=False, verbose_name='筛选')),
            ],
            options={
                'verbose_name': '添加口味',
                'verbose_name_plural': '添加口味',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=20, verbose_name='关系')),
                ('is_active', models.BooleanField(default=False, verbose_name='筛选')),
            ],
            options={
                'verbose_name': '添加关系类型',
                'verbose_name_plural': '添加关系类型',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=20, verbose_name='主题')),
                ('is_active', models.BooleanField(default=False, verbose_name='筛选')),
            ],
            options={
                'verbose_name': '添加主题',
                'verbose_name_plural': '添加主题',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=20, verbose_name='重量')),
                ('is_active', models.BooleanField(default=False, verbose_name='筛选')),
            ],
            options={
                'verbose_name': '添加重量',
                'verbose_name_plural': '添加重量',
            },
        ),
        migrations.AddField(
            model_name='cake',
            name='cake_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Categories', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='cake',
            name='cake_flavour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Flavour', verbose_name='口味'),
        ),
        migrations.AddField(
            model_name='cake',
            name='cake_relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Relation', verbose_name='关系'),
        ),
        migrations.AddField(
            model_name='cake',
            name='cake_theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Theme', verbose_name='主题'),
        ),
        migrations.AddField(
            model_name='cake',
            name='cake_weight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Weight', verbose_name='重量'),
        ),
    ]