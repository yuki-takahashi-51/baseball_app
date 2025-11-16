from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0004_batting_status'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
        CREATE TABLE `pitching_status` (
                `uniform_number` INT PRIMARY KEY,
                `games` INT NULL,
                `win` INT NULL,
                `lose` INT NULL,
                `saves` INT NULL,
                `hold` INT NULL,
                `hp` INT NULL,
                `fullIning` INT NULL,
                `perfect` INT NULL,
                `noFour` INT NULL,
                `batter` INT NULL,
                `ining` FLOAT NULL,
                `hit` INT NULL,
                `homerun` INT NULL,
                `fourball` INT NULL,
                `deadBall` INT NULL,
                `strikeOut` INT NULL,
                `wildPitch` INT NULL,
                `balk` INT NULL,
                `lostScore` INT NULL,
                `earnedRun` INT NULL,
                `ERA` FLOAT NULL,
                `QS` INT NULL,
                `int_walk` INT NULL,
                CONSTRAINT `pitchingstatus_pitcher` 
                FOREIGN KEY (`uniform_number`) 
                REFERENCES `pitcher` (`uniform_number`)
            );
        """,
        reverse_sql=
        """
        DROP TABLE pitching_status;
        """
    )
    ]
