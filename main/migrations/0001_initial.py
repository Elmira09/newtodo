

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('published_at', models.DateField(auto_now_add=True)),

        
            ],
        ),
    ]
