from .ORMdict import getter
from .player_metrics import batter_metrics, pitcher_metrics
from .player_metrics import batter_metrics, pitcher_metrics

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

def collect_player_csv_data(uniform_number):
    """
    CSV出力用のデータを収集するサービス
    書き込み処理はviewsに委ねる
    """
    result = get_player_with_stats(uniform_number)

    player = result["player"]
    batting = result["batting"]
    pitching = result["pitching"]

    metrics = None
    if batting:
        metrics = batter_metrics(batting)
    elif pitching:
        metrics = pitcher_metrics(pitching)

    return {
        "player": player,
        "batting": batting,
        "pitching": pitching,
        "metrics": metrics,
    }
    
def get_player_with_metrics(uniform_number):
    """
    選手情報取得処理に「指標計算」を付与するサービス
    None判定のみを行い、例外処理や分岐制御はViewに持ち込まない
    """
    data = get_player_with_stats(uniform_number)
    if not data:
        return None

    batting = data["batting"]
    pitching = data["pitching"]

    if batting:
        data["metrics"] = batter_metrics(batting)
    elif pitching:
        data["metrics"] = pitcher_metrics(pitching)
    else:
        data["metrics"] = {}
