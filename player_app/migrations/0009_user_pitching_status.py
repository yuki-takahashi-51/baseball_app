
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0008_user_batting_status'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
        CREATE TABLE `user_pitching_status` (
                `player_id` INT PRIMARY KEY,
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
                `ining` INT NULL,
                `hit` INT NULL,
                `homerun` INT NULL,
                `fourball` INT NULL,
                `intWalk` INT NULL,
                `deadBall` INT NULL,
                `strikeOut` INT NULL,
                `wildPitch` INT NULL,
                `balk` INT NULL,
                `lostScore` INT NULL,
                `earnedRun` INT NULL,
                `ERA` FLOAT NULL,
                `QS` INT NULL,

                CONSTRAINT `userpitchingstatus_player_fk`
                    FOREIGN KEY (`player_id`)
                    REFERENCES `user_pitcher` (`id`)
                    ON DELETE CASCADE
                );
        """,
        reverse_sql=
        """
        DROP TABLE user_pitching_status;
        """
    )
    ]
