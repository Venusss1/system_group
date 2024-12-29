# Generated by Django 3.0.4 on 2020-10-31 07:37

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(default='未命名课程', max_length=30)),
                ('courseNumber', models.CharField(default='000000', max_length=30)),
                ('status', models.CharField(choices=[('Y', '开启'), ('N', '关闭')], default='Y', max_length=10, verbose_name='开设状态')),
            ],
            options={
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='未知', max_length=20, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=2, verbose_name='姓别')),
                ('type', models.CharField(choices=[('T', '老师'), ('S', '学生')], default='S', max_length=2, verbose_name='类型')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '教学用户',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='未命名作业', max_length=100, unique=True)),
                ('content', models.TextField(default='请修改作业正文~')),
                ('display', models.CharField(choices=[('Y', 'on'), ('N', 'off')], default='Y', max_length=2, verbose_name='显示')),
                ('uploadFileType', models.CharField(default='*', max_length=30)),
                ('courseBelongTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Course')),
            ],
            options={
                'verbose_name': '作业',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('filePath', models.CharField(default='/file', max_length=100)),
                ('task', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Task')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.UserProfile')),
            ],
            options={
                'verbose_name': '提交记录',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(to='app01.UserProfile'),
        ),
    ]
