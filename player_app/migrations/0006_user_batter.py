from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0005_pitching_status'),
    ]

    operations = [migrations.RunSQL(
        sql=
        """
       CREATE TABLE `user_batter` (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `user_id` INT NOT NULL,
                `uniform_number` INT NOT NULL,
                `player_name` VARCHAR(50) NOT NULL,
                `birthday` DATE NULL,
                `position` VARCHAR(2) NOT NULL,
                `batting_hand` VARCHAR(1) NULL,
                `throwing_hand` VARCHAR(1) NULL,
                `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                `is_public` BOOLEAN NOT NULL DEFAULT FALSE,

                CONSTRAINT `userbatter_user_uniform_unique`
                    UNIQUE (`user_id`, `uniform_number`),

                CONSTRAINT `userbatter_user_fk`
                    FOREIGN KEY (`user_id`)
                    REFERENCES `user` (`user_id`)
                    ON DELETE CASCADE
                    );

            CREATE INDEX `userbatter_user_uniform_idx`
                ON `user_batter` (`user_id`, `uniform_number`);

            CREATE INDEX `userbatter_playername_idx`
                ON `user_batter` (`player_name`);
        """,
        reverse_sql=
        """
        DROP TABLE user_batter;
        """
    )
    ]
