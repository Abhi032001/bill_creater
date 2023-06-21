# Generated by Django 4.2 on 2023-05-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('fil', models.TextField()),
                ('heading', models.TextField()),
                ('album', models.ImageField(upload_to='images/albump/')),
            ],
        ),
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('fil', models.TextField()),
                ('heading', models.TextField()),
                ('boy', models.ImageField(upload_to='images/boyp/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Budget', models.CharField(max_length=50)),
                ('Service', models.CharField(max_length=50)),
                ('Day', models.CharField(max_length=50)),
                ('Date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Girls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('fil', models.TextField()),
                ('heading', models.TextField()),
                ('girls', models.ImageField(upload_to='images/girlsp/')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('fil', models.TextField()),
                ('heading', models.TextField()),
                ('baby', models.ImageField(upload_to='images/kidsp/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Profession', models.TextField()),
                ('Instagram_id', models.TextField()),
                ('Photo', models.ImageField(upload_to='images/Team/')),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('fil', models.TextField()),
                ('heading', models.TextField()),
                ('wedding', models.ImageField(upload_to='images/weddingp/')),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rk_photo.invoice')),
            ],
        ),
    ]
