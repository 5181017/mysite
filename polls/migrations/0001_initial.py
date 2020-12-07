<<<<<<< HEAD
# Generated by Django 3.1 on 2020-09-30 04:56

from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 3.1 on 2020-11-02 05:22

from django.db import migrations, models
import django.db.models.deletion
import polls.models
>>>>>>> 7cd6b08949c25a3e14c1aed64599daa3a9f79349


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='PollsCharginghistory',
            fields=[
                ('chargeid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(db_column='userID', max_length=15, verbose_name=polls.models.User)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('addmoney', models.IntegerField(blank=True, db_column='addMoney', null=True)),
                ('summoney', models.IntegerField(blank=True, db_column='sumMoney', null=True)),
            ],
            options={
                'db_table': 'polls_charginghistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
>>>>>>> 7cd6b08949c25a3e14c1aed64599daa3a9f79349
            name='Category',
            fields=[
                ('categoryID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('imageURL', models.CharField(max_length=2048)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
                ('money', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('reviewStar', models.IntegerField()),
                ('title', models.CharField(max_length=50, null=True)),
                ('comment', models.TextField()),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.products')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('paymentID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.products')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='ChargingHistory',
            fields=[
                ('chargeID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('addMoney', models.IntegerField()),
                ('sumMoney', models.IntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 7cd6b08949c25a3e14c1aed64599daa3a9f79349
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.products')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='cart',
            constraint=models.UniqueConstraint(fields=('userID', 'productID'), name='unique_booking'),
        ),
    ]
