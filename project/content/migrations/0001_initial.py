# Generated by Django 3.2.9 on 2021-11-06 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decision', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Счетчик')),
                ('link', models.URLField(verbose_name='Ссылка на аудио')),
                ('bitrate', models.PositiveBigIntegerField(default=0, help_text='Зависит от максимального битрейта, который попытаться добавить в бд. На вскидку: 1,4 Гбит - для 1080р несжатого, как говорит вики (а это 1400000000 бит). ', verbose_name='Битрейт')),
                ('bit_in_second', models.IntegerField(default=0, verbose_name='Бит в секунду')),
            ],
            options={
                'verbose_name': 'Аудио',
                'verbose_name_plural': 'Аудио',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Счетчик')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Текст',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Счетчик')),
                ('link', models.URLField(verbose_name='Ссылка на видео')),
                ('link_subtitles', models.URLField(verbose_name='Ссылка на субтитры')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.PositiveIntegerField(default=0)),
                ('content_audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.audio', verbose_name='Аудио')),
                ('content_text', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.text', verbose_name='Текст')),
                ('content_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.video', verbose_name='Видео')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='decision.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'ordering': ['custom_id'],
            },
        ),
    ]