#RunSQLで直接書き込む　これ以降のmigrationsも同じ
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0001_initial'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
        CREATE TABLE `batter` (
                `uniform_number` INT PRIMARY KEY,
                `player_name` VARCHAR(50) NOT NULL,
                `birthday` DATE NULL,
                `position` VARCHAR(2) NOT NULL,
                `batting_hand` CHAR(1) NOT NULL,
                `throwing_hand` CHAR(1) NOT NULL
            );
        """,
        reverse_sql=
        """
        DROP TABLE batter;
        """
    )
    ]

