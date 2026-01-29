from .ORMdict import getter
from .player_metrics import batter_metrics, pitcher_metrics
 
def get_player_with_metrics(uniform_number):
    """
    背番号を基点に、選手情報・成績情報・指標情報をまとめて取得するサービス。

    - ORMs/Repository相当層から取得したデータを統合
    - 打者/投手の判定および指標計算は本サービス層で完結
    - viewsは本関数の戻り値をそのまま描画用途に利用することを想定
    - 該当選手が存在しない場合はNoneを返す
    """
    result = getter["player_by_uniform_number"](uniform_number)
    if not result:
        return None

    player, player_type = result
    batting = None
    pitching = None

    if player_type == "batter":
        batting = getter["player_batting"](player)
        metrics = batter_metrics(batting)
    elif player_type == "pitcher":
        pitching = getter["player_pitching"](player)
        metrics = pitcher_metrics(pitching)

    return {
        "player": player,
        "player_type": player_type,
        "batting": batting,
        "pitching": pitching,
        "metrics": metrics,
    }
