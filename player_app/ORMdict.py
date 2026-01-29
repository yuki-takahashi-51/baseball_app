from . import ORMs

getter = {
    "all_player": ORMs.get_allplayer,
    "player_by_name": ORMs.get_player_by_name,
    "player_by_uniform_number": ORMs.get_player_by_uniform_number,
    "player_batting": ORMs.get_player_batting,
    "player_pitching": ORMs.get_player_pitching,
    "user_batter": ORMs.get_user_batter,
    "user_pitcher": ORMs.get_user_pitcher,
    "user_player_by_uniform_number": ORMs.get_user_player_by_uniform_number,
    "user_batting": ORMs.get_user_player_batting,
    "user_pitching": ORMs.get_user_player_pitching,
}

setter = {
    "create_user": ORMs.create_user,
    "create_batter": ORMs.create_batter,
    "create_pitcher": ORMs.create_pitcher,
}
