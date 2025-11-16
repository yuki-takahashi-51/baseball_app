
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0009_user_pitching_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batting_status',
            fields=[
                ('uniform_number', models.OneToOneField(db_column='uniform_number', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='battingstatus_player', serialize=False, to='player_app.batter')),
                ('games', models.IntegerField(blank=True, null=True)),
                ('numPlate', models.IntegerField(blank=True, null=True)),
                ('numBat', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('hits', models.IntegerField(blank=True, null=True)),
                ('hit2nd', models.IntegerField(blank=True, null=True)),
                ('hit3rd', models.IntegerField(blank=True, null=True)),
                ('homeruns', models.IntegerField(blank=True, null=True)),
                ('baseHits', models.IntegerField(blank=True, null=True)),
                ('getpoint', models.IntegerField(blank=True, null=True)),
                ('steal', models.IntegerField(blank=True, null=True)),
                ('missedSteal', models.IntegerField(blank=True, null=True)),
                ('bants', models.IntegerField(blank=True, null=True)),
                ('sacFry', models.IntegerField(blank=True, null=True)),
                ('fourballs', models.IntegerField(blank=True, null=True)),
                ('intWalk', models.IntegerField(blank=True, null=True)),
                ('deadballs', models.IntegerField(blank=True, null=True)),
                ('strikeOut', models.IntegerField(blank=True, null=True)),
                ('doublePlay', models.IntegerField(blank=True, null=True)),
                ('errors', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batting_status',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='BattingStatus',
        ),
    ]
