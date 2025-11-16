from .ORMs import getter,setter

#ORMsで定義した関数を辞書にまとめて見やすくする
getter = {
    "players":getter.get_playersresult,
    "player":getter.get_player,
    "all_player":getter.get_allplayer,
    "player_batting":getter.get_player_batting,
    "player_pitching":getter.get_player_pitching,
    "user_batter":getter.get_user_batters,
    "user_pitcher":getter.get_user_pitchers,
    "user_player":getter.get_user_player,
    "user_batting":getter.get_user_player_batting,
    "user_pitching":getter.get_user_player_pitching
}

setter = {
    "create_user":setter.creata_user,
    "create_batter":setter.create_batter,
    "create_pitcher":setter.create_pitcher
}