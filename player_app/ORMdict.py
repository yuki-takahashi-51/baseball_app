"""
本構成は、学習初期段階においてviewsの肥大化を防ぐ目的で、
ORMsで定義された関数群を「辞書」として集約するための層である。

- ORMs への単純なルーティングのみを責務とする
- ロジック・条件分岐・例外処理は一切持たない
- views → ORMs の間に噛ませることで、依存関係を緩める意図がある
- DjangoにDIコンテナが存在しないため、その代替表現として辞書を採用している

処理内容の詳細はORMsを参照すること
"""

from . import ORMs

# 参照系
getter = {
  # 選手取得
    "all_player": ORMs.get_allplayer,
    "player_by_name": ORMs.get_player_by_name,
    "player_by_uniform_number": ORMs.get_player_by_uniform_number,
    
    # 成績取得
    "player_batting": ORMs.get_player_batting,
    "player_pitching": ORMs.get_player_pitching,
    
    # ユーザー作成選手取得
    "user_batter": ORMs.get_user_batter,
    "user_pitcher": ORMs.get_user_pitcher,
    "user_player_by_uniform_number": ORMs.get_user_player_by_uniform_number,
    
    # ユーザー作成選手の成績取得
    "user_batting": ORMs.get_user_player_batting,
    "user_pitching": ORMs.get_user_player_pitching,
}

# 更新・作成系
# ユーザー登録など、viewsから直接ORMsを呼びたくない処理も含めている
setter = {
    "create_user": ORMs.create_user,
    "create_batter": ORMs.create_batter,
    "create_pitcher": ORMs.create_pitcher,
}
