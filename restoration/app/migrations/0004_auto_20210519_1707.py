# Generated by Django 3.1.7 on 2021-05-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210519_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Save the name of the input image.', max_length=200)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('input_img', models.ImageField(upload_to='input_image')),
                ('output_img', models.ImageField(blank=True, null=True, upload_to='output_image')),
            ],
        ),
        migrations.DeleteModel(
            name='InputImage',
        ),
        migrations.DeleteModel(
            name='RestoredImage',
        ),
    ]
