from django.urls import path
from . import views

#urlを指定するとき使用する　どのappに属するかを決める
app_name = 'player_app'

#nameは内部から呼び出されるときに使用する　urlが呼び出されたときviewsの関数を実行する
urlpatterns = [
    path("", views.search, name='search'),
    path("players", views.all_player, name="all_player"),
    path("result", views.result, name="result"),
    path("<int:uniform_number>_<str:player_name>", views.player_detail, name="player_info"),
    path("<int:uniform_number>_more_detail/", views.player_moreinfo, name="more_detail"),
    path("<int:uniform_number>/csv/", views.player_csv, name="player_csv"),
    path("register_user", views.register_user, name = "register_user"),
    path("login", views.login, name = "login"),
    path("register_original_batter/", views.register_original_batter, name = "register_original_batter"),
    path("register_original_pitcher/", views.register_original_pitcher, name = "register_original_pitcher"),
    path("original_player_result", views.user_all_player, name = "original_player_result"),
    path("original_player_detail", views.user_player_detail, name = "original_player_detail.html")
]