from django.shortcuts import render,redirect
from. import forms
from.ORMdict import getter,setter
from.models import Batting_status, Pitching_status, User_batter, User_pitcher, User_batting_status, User_pitching_status
from.player_metrics import batter_metrics, pitcher_metrics
import csv
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def search(request):    #search.htmlを展開しformで定義したクラスを利用する
    form_search = forms.Search_player()
    return render(request, "search.html", {"form":form_search})

def result(request):    #POSTデータが送信されてきたらORMSで定義したゲッターを実行する
    #取得した選手情報(背番号)をresult.htmlに渡しながら展開する　POSTがなかった時に空値を返すのは何も送信されなかった時の処理を実行するため
    name = ""
    players = []
    if request.method == "POST":
        name = request.POST.get("player_name", "") 
        players = getter["players"](name)
        text = {"name": name, "players": players}
    return render(request, "result.html", text)

#背番号をもとに情報を入手し打者であったら打撃成績を、投手であったら投球成績を取得する　
# 最初デフォルトで空にしているのはどちらも片方のデータしか持っておらず両方取得するのは不可能だから
def player_detail(request, uniform_number, player_name):
    player, player_type = getter["player"](uniform_number)
    batting = None
    pitching = None
    
    if player_type == "batter":
        try:
            batting = getter["player_batting"](player)
        except Batting_status.DoesNotExist:
            batting = None
            pitching = None
    else:
        try:
            pitching = getter["player_pitching"](player)
        except Pitching_status.DoesNotExist:
            pitching = None
            batting = None

    text = {"player": player, "batting": batting, "pitching": pitching}
    return render(request, "player.html", text)

#ほぼ先ほどと一緒
def player_moreinfo(request, uniform_number):
    player, player_type = getter["player"](uniform_number)
    batting = None
    pitching = None
    
    if player_type == "batter":
        try:
            batting = getter["player_batting"](player)
        except Batting_status.DoesNotExist:
            batting = None
            pitching = None
    else:
        try:
            pitching = getter["player_pitching"](player)
        except Pitching_status.DoesNotExist:
            pitching = None
            batting = None
    #打撃成績があれば打者の指標計算用関数を取得する　そうでない、つまり投球成績を持っていれば投手用の関数を取得
    metrics = batter_metrics(batting) if batting else pitcher_metrics(pitching)      
    
    text = {"player": player, "batting": batting, "pitching": pitching, "metrics":metrics}
    return render(request, "player_detail.html", text)

def player_csv(request, uniform_number):
    player, player_type = getter["player"](uniform_number)
    batting = None
    pitching = None
    
    if player_type == "batter":
        try:
            batting = getter["player_batting"](player)
        except Batting_status.DoesNotExist:
            batting = None
            pitching = None
    else:
        try:
            pitching = getter["player_pitching"](player)
        except Pitching_status.DoesNotExist:
            pitching = None
            batting = None
            #ここまではほぼ一緒

    response = HttpResponse(content_type="text/csv")
    #csv形式のテキストを返す
    response["Content-Disposition"] = f'attachment; filename="{player.player_name}_stats.csv"'
    #ダウンロード用だと明示し選手ごとにファイルに名前を付ける

    response.write('\ufeff')
    #このファイルがutf8であると指定する　ない場合文字化けの可能性がある
    writer = csv.writer(response)
    #これまでの定義をもとにcsvのモジュールで記述するため変数に格納する

    #基本情報は全員持っているためここで順に並べる
    writer.writerow(["背番号", "氏名", "生年月日", "ポジション", "利き手"])
    writer.writerow([
        player.uniform_number,
        player.player_name,
        player.birthday.strftime("%Y-%m-%d") if player.birthday else "",
        player.position,
        f"{player.throwing_hand}投げ{player.batting_hand}打ち"
    ])
    writer.writerow([])

    #打撃成績があるか投球成績があるか判断し打撃成績と打撃指標、または投球成績と投球指標を記述
    if batting:
        metrics_bat = batter_metrics(batting)
        writer.writerow(["打撃成績"])
        writer.writerow(["試合数","打席","打数","安打","二塁打","三塁打","本塁打","得点","打点","犠打","犠飛","四球","死球","三振","併殺"])
        writer.writerow([
            batting.games, batting.numPlate, batting.numBat, batting.hits,
            batting.hit2nd, batting.hit3rd, batting.homeruns, batting.points,
            batting.getpoint, batting.bants, batting.sacFry,
            batting.fourballs, batting.deadballs, batting.strikeOut, batting.doublePlay
        ])
        writer.writerow([])
        writer.writerow(["打撃指標"])
        for key, value in metrics_bat.items():
            writer.writerow([key, value])
        writer.writerow([])

    if pitching:
        metrics_pitch = pitcher_metrics(pitching)
        writer.writerow(["投球成績"])
        writer.writerow(["登板数","投球回","勝","敗","ホールド","HP","セーブ","防御率",
                         "完投","完封","QS","対戦打者数","奪三振","被安打","被本塁打",
                         "与四球","与死球","敬遠","無四球","暴投","ボーク","失点","自責点"])
        writer.writerow([
        pitching.games, pitching.ining, pitching.win, pitching.lose,
        pitching.hold, pitching.hp, pitching.saves, pitching.ERA,
        pitching.fullIning, pitching.perfect, pitching.QS, pitching.batter,
        pitching.strikeOut, pitching.hit, pitching.homerun,
        pitching.fourball, pitching.deadBall, pitching.int_Walk, pitching.noFour,
        pitching.wildPitch, pitching.balk, pitching.lostScore, pitching.earnedRun
    ])

        writer.writerow([])
        writer.writerow(["投手指標"])
        for key, value in metrics_pitch.items():
            writer.writerow([key, value])
        writer.writerow([])
    #記述が住んだものを代入　送信
    return response

#全選手情報取得
def all_player(request):
    player = getter["all_player"]()
    return render(request, "all_player.html", {"player":player})

#ユーザー登録
def register_user(request):
    form_register_user = forms.Register_user()

    if request.method == "POST":
        form_post_register = forms.Register_user(request.POST)
        print(form_post_register.is_valid())
        if form_post_register.is_valid():
            cd = form_post_register.cleaned_data
            user = setter["create_user"](
                email=cd["email"],
                password=cd["password"],
                username=cd["username"],
                first_name=cd["first_name"],

            )
            auth_login(request, user)
            messages.success(request, "登録してログインしました。")
            return redirect("player_app:search")
        else:
            print(form_post_register.errors)
        form_register_user = form_post_register

    return render(
        request,
        "register_user.html",
        {"form_register_user": form_register_user}
    )

#ログイン
def login(request):
    if request.method == "POST":
        form_login = forms.Login(request.POST)
        if form_login.is_valid():
            cd = form_login.cleaned_data
            user = authenticate(
                request, 
                username=cd["email"], 
                password=cd["password"]
            )
            if user:
                auth_login(request, user)
                return redirect("player_app:search")
            else:
                form_login.add_error(None, "メールアドレスまたはパスワードが違います。")
    else: #GETだった場合
        form_login = forms.Login()

    return render(request, "login.html", {"form_login": form_login})


@login_required
def register_original_batter(request):
    if request.method == "POST":
        form_register_batter = forms.Register_original_batter(request.POST)
        if  form_register_batter.is_valid():
            cd = form_register_batter.cleaned_data
            setter["create_batter"](
                user=request.user,
                uniform_number=cd["uniform_number"],
                player_name=cd["player_name"],
                position=cd["position"],
                birthday=cd.get("birthday",0),
                batting_hand=cd.get("batting_hand",0),
                throwing_hand=cd.get("throwing_hand",0),
                games=cd.get("games",0),
                numPlate=cd.get("numPlate",0),
                numBat=cd.get("numBat",0),
                points=cd.get("points",0),
                hits=cd.get("hits",0),
                hit2nd=cd.get("hit2nd",0),
                hit3rd=cd.get("hit3rd",0),
                homeruns=cd.get("homeruns",0),
                baseHits=cd.get("baseHits",0),
                getpoint=cd.get("getpoint",0),
                steal=cd.get("steal",0),
                missedSteal=cd.get("missedSteal",0),
                bants=cd.get("bants",0),
                sacFry=cd.get("sacFry",0),
                fourballs=cd.get("fourballs",0),
                intWalk=cd.get("intWalk",0),
                deadballs=cd.get("deadballs",0),
                strikeOut=cd.get("strikeOut",0),
                doublePlay=cd.get("doublePlay",0),
                errors=cd.get("errors",0)
            )
            messages.success(request, "打者を登録しました。")
            return redirect("player_app:search") #遷移先は適宜変更
    else:
        form_register_batter = forms.Register_original_batter()
    return render(request, "register_original_batter.html", {"form": form_register_batter})

@login_required
def register_original_pitcher(request):
    if request.method == "POST":
        form_register_pitcher = forms.Register_original_pitcher(request.POST)
        if form_register_pitcher.is_valid():
            cd = form_register_pitcher.cleaned_data
            setter["create_pitcher"](
                user=request.user,
                uniform_number=cd["uniform_number"],
                player_name=cd["player_name"],
                position=cd["position"],
                birthday=cd.get("birthday",0),
                batting_hand=cd.get("batting_hand",0),
                throwing_hand=cd.get("throwing_hand",0),
                games=cd.get("games",0),
                win=cd.get("win",0),
                lose=cd.get("lose",0),
                saves=cd.get("saves",0),
                hold=cd.get("hold",0),
                hp=cd.get("hp",0),
                fullIning=cd.get("fullIning",0),
                perfect=cd.get("perfect",0),
                noFour=cd.get("noFour",0),
                batter=cd.get("batter",0),
                ining=cd.get("ining",0),
                hit=cd.get("hit",0),
                homerun=cd.get("homerun",0),
                fourball=cd.get("fourball",0),
                int_Walk=cd.get("int_Walk",0),
                deadBall=cd.get("deadBall",0),
                strikeOut=cd.get("strikeOut",0),
                wildPitch=cd.get("wildPitch",0),
                balk=cd.get("balk",0),
                lostScore=cd.get("lostScore",0),
                earnedRun=cd.get("earnedRun",0),
                ERA=cd.get("ERA",0),
                QS=cd.get("QS",0)
            )
            messages.success(request, "投手を登録しました。")
            return redirect("player_app:search") 
    else:
        form_register_pitcher = forms.Register_original_pitcher()
    return render(request, "register_original_pitcher.html", {"form": form_register_pitcher})

@login_required
def original_all_player(request):
    batters = getter["user_batter"](request.user)
    pitchers = getter["user_pitcher"](request.user)
    players = list(batters) + list(pitchers)
    return render(request, "original_player_result.html", {"players": players})

@login_required
def original_player_detail(request, uniform_number):
    player, player_type = getter["user_player"](uniform_number, request.user)
    batting = None
    pitching = None

    if player_type == "batter":
        try:
            batting = getter["user_batting"](player)
        except User_batting_status.DoesNotExist:
            batting = None
    else:
        try:
            pitching = getter["user_pitchin"](player)
        except User_pitching_status.DoesNotExist:
            pitching = None

    #計算関数を利用
    metrics = batter_metrics(batting) if batting else pitcher_metrics(pitching)

    context = {
        "player": player,
        "batting": batting,
        "pitching": pitching,
        "metrics": metrics
    }
    return render(request, "original_player_detail.html", context)
