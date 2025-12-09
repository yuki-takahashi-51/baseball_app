from django.urls import path,include

urlpatterns = [
    path('', include('player_app.urls'))
]

