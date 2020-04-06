# Generated by Django 3.0.4 on 2020-03-18 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NatureBien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SousFamille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sous_famille', models.CharField(max_length=200)),
                ('dexcription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PostSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('etat_actuel', models.CharField(choices=[('NEUF', 'NEUF'), ('BON ETAT', 'BON ETAT'), ('MOYEN', 'MOYEN'), ('MEDIOCRE', 'MEDIOCRE'), ('TRES DEGRADE', 'TRES DEGRADE')], max_length=200)),
                ('nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.NatureBien')),
                ('sous_famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SousFamille')),
            ],
        ),
        migrations.CreateModel(
            name='PostProp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('etat_achat', models.CharField(choices=[('NEUF', 'NEUF'), ('DEUXIEME MAIN', 'DEUXIEME MAIN'), ('OCCASION', 'OCCASION'), ('INCONU', 'INCONU')], max_length=200)),
                ('etat_actuel', models.CharField(choices=[('NEUF', 'NEUF'), ('BON ETAT', 'BON ETAT'), ('MOYEN', 'MOYEN'), ('MEDIOCRE', 'MEDIOCRE'), ('TRES DEGRADE', 'TRES DEGRADE')], max_length=200)),
                ('nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.NatureBien')),
                ('sous_famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SousFamille')),
            ],
        ),
    ]
