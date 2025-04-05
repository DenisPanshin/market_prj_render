# Generated by Django 3.2.25 on 2025-04-05 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_auto_20250328_2023'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлён')),
                ('status', models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PRD', 'оплачен'), ('PD', 'обрабатывается'), ('RDY', 'подтверждён размещением'), ('CNL', 'отменён')], default='FM', max_length=3, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nights', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.accommodation', verbose_name='размещение')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='ordersapp.order')),
            ],
        ),
    ]
