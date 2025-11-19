import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0010_batting_status_delete_battingstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitching_status',
            fields=[
                ('uniform_number', models.OneToOneField(db_column='uniform_number', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='pitchingstatus_player', serialize=False, to='player_app.pitcher')),
                ('games', models.IntegerField(null=True, blank=True)),
                ('win', models.IntegerField(null=True, blank=True)),
                ('lose', models.IntegerField(null=True, blank=True)),
                ('saves', models.IntegerField(null=True, blank=True)),
                ('hold', models.IntegerField(null=True, blank=True)),
                ('hp', models.IntegerField(null=True, blank=True)),
                ('fullIning', models.IntegerField(null=True, blank=True)),
                ('perfect', models.IntegerField(null=True, blank=True)),
                ('noFour', models.IntegerField(null=True, blank=True)),
                ('batter', models.IntegerField(null=True, blank=True)),
                ('ining', models.IntegerField(null=True, blank=True)),
                ('hit', models.IntegerField(null=True, blank=True)),
                ('homerun', models.IntegerField(null=True, blank=True)),
                ('fourball', models.IntegerField(null=True, blank=True)),
                ('intWalk', models.IntegerField(null=True, blank=True)),
                ('deadBall', models.IntegerField(null=True, blank=True)),
                ('strikeOut', models.IntegerField(null=True, blank=True)),
                ('wildPitch', models.IntegerField(null=True, blank=True)),
                ('balk', models.IntegerField(null=True, blank=True)),
                ('lostScore', models.IntegerField(null=True, blank=True)),
                ('earnedRun', models.IntegerField(null=True, blank=True)),
                ('ERA', models.FloatField(null=True, blank=True)),
                ('QS', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'pitching_status',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Pitching_Status',
        ),
    ]
