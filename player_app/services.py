from .ORMdict import getter

def get_player_with_stats(uniform_number):
    """
    選手情報・成績情報をまとめて取得する
    viewsからの条件分岐を減らすためのサービス関数
    """
    result = getter["player_by_uniform_number"](uniform_number)
    if not result:
        return None

    player, player_type = result
    batting = None
    pitching = None

    if player_type == "batter":
        batting = getter["player_batting"](player)
    elif player_type == "pitcher":
        pitching = getter["player_pitching"](player)

    return {"player": player, "player_type": player_type, "batting": batting, "pitching": pitching}
