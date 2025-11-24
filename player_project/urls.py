from django.urls import path,include

#立ち上げたアプリのurlパターンを有効にするため追加する
urlpatterns = [
    path('', include('player_app.urls'))
]
