
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0007_user_pitcher'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
        CREATE TABLE `user_batting_status` (
                `player_id` INT PRIMARY KEY,
                `games` INT NULL,
                `numPlate` INT NULL,
                `numBat` INT NULL,
                `points` INT NULL,
                `hits` INT NULL,
                `hit2nd` INT NULL,
                `hit3rd` INT NULL,
                `homeruns` INT NULL,
                `baseHits` INT NULL,
                `getpoint` INT NULL,
                `steal` INT NULL,
                `missedSteal` INT NULL,
                `bants` INT NULL,
                `sacFry` INT NULL,
                `fourballs` INT NULL,
                `intWalk` INT NULL,
                `deadballs` INT NULL,
                `strikeOut` INT NULL,
                `doublePlay` INT NULL,
                `errors` INT NULL,

                CONSTRAINT `userbattingstatus_player_fk`
                    FOREIGN KEY (`player_id`)
                    REFERENCES `user_batter` (`id`)
                    ON DELETE CASCADE
                );
        """,
        reverse_sql=
        """
        DROP TABLE user_batting_status;
        """
    )
    ]
