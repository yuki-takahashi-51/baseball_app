from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0003_pitcher'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
        CREATE TABLE `batting_status` (
                `uniform_number` INT PRIMARY KEY,
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
                CONSTRAINT `battingstatus_batter` 
                FOREIGN KEY (`uniform_number`) 
                REFERENCES `batter` (`uniform_number`)
            );
        """,
        reverse_sql=
        """
        DROP TABLE batting_status;
        """
    )
    ]