# Generated by Django 3.2.13 on 2022-12-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='tag',
            field=models.CharField(choices=[('BODO', '보도자료'), ('RECOMMEND', '추천·리뷰'), ('ECT', '기타'), ('BASIC', '기초상식'), ('YEAR', '연말정산'), ('NEWS', '뉴스')], default='ECT', max_length=20, verbose_name='태그명'),
        ),
    ]
