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
import traceback
from .services import get_player_with_metrics, get_original_player_with_metrics


def search(request):    #検索画面
    form_search = forms.Search_player()
    return render(request, "search.html", {"form":form_search})

def result(request):    #検索結果表示　
    text = {"name": "", "players": []}
    
    if request.method == "POST":
        name = request.POST.get("player_name", "") 
        players = getter["player_by_name"](name)
        text = {"name": name, "players": players}
    return render(request, "result.html", text)

#背番号から選手個人の情報を引き出す　nameはバーに表示するのに必要だったため
def player_detail(request, uniform_number, player_name):
    text = get_player_with_metrics(uniform_number)
    if not text:
        return render(request, "404.html")
    return render(request, "player.html", text)

#詳細情報取得
def player_moreinfo(request, uniform_number):
    text = get_player_with_metrics(uniform_number)
    if not text:
        return render(request, "404.html")

    return render(request, "player_detail.html", text)

#選手データをCSVでダウンロード
def player_csv(request, uniform_number):
    text = get_player_with_metrics(uniform_number)
    if not text:
        return render(request, "404.html")
    
    player = text["player"]
    batting = text["batting"]
    pitching = text["pitching"]
    metrics = text["metrics"]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{player.player_name}_stats.csv"'

    response.write('\ufeff')
    #utf8指定　保険
    writer = csv.writer(response)
   
    #基本情報
    writer.writerow(["背番号", "氏名", "生年月日", "ポジション", "利き手"])
    writer.writerow([
        player.uniform_number,
        player.player_name,
        player.birthday.strftime("%Y-%m-%d") if player.birthday else "",
        player.position,
        f"{player.throwing_hand}投げ{player.batting_hand}打ち"
    ])
    writer.writerow([])

    if batting:
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
        for key, value in metrics.items():
            writer.writerow([key, value])

    if pitching:
        writer.writerow(["投球成績"])
        writer.writerow(["登板数","投球回","勝","敗","ホールド","HP","セーブ","防御率",
                         "完投","完封","QS","対戦打者数","奪三振","被安打","被本塁打",
                         "与四球","与死球","敬遠","無四球","暴投","ボーク","失点","自責点"])
        writer.writerow([
        pitching.games, pitching.ining, pitching.win, pitching.lose,
        pitching.hold, pitching.hp, pitching.saves, pitching.ERA,
        pitching.fullIning, pitching.perfect, pitching.QS, pitching.batter,
        pitching.strikeOut, pitching.hit, pitching.homerun,
        pitching.fourball, pitching.deadBall, pitching.intWalk, pitching.noFour,
        pitching.wildPitch, pitching.balk, pitching.lostScore, pitching.earnedRun
    ])
        writer.writerow([])
        writer.writerow(["投手指標"])
        for key, value in metrics.items():
            writer.writerow([key, value])
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
    else: 
        form_login = forms.Login()

    return render(request, "login.html", {"form_login": form_login})

#オリジナル打者登録
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
                birthday=cd.get("birthday") or None,
                batting_hand=cd.get("batting_hand") or None,
                throwing_hand=cd.get("throwing_hand") or None,
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
            return redirect("player_app:search") 
    else:
        form_register_batter = forms.Register_original_batter()
    return render(request, "register_original_batter.html", {"form": form_register_batter})

#オリジナル投手登録　デバックの跡は見返しのため残す
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
                birthday=cd.get("birthday") or None,
                batting_hand=cd.get("batting_hand") or None,
                throwing_hand=cd.get("throwing_hand") or None,
                games=cd.get("games", 0),
                ERA=cd.get("ERA", 0),
                win=cd.get("win", 0),
                lose=cd.get("lose", 0),
                saves=cd.get("saves", 0),
                hold=cd.get("hold", 0),
                hp=cd.get("hp", 0),
                fullIning=cd.get("fullIning", 0),
                perfect=cd.get("perfect", 0),
                noFour=cd.get("noFour", 0),
                batter=cd.get("batter", 0),
                ining=cd.get("ining", 0),
                hit=cd.get("hit", 0),
                homerun=cd.get("homerun", 0),
                fourball=cd.get("fourball", 0),
                intWalk=cd.get("intWalk", 0),
                deadBall=cd.get("deadBall", 0),
                strikeOut=cd.get("strikeOut", 0),
                wildPitch=cd.get("wildPitch", 0),
                balk=cd.get("balk", 0),
                lostScore=cd.get("lostScore", 0),
                earnedRun=cd.get("earnedRun", 0),
                QS=cd.get("QS", 0),
            )
            messages.success(request, "投手を登録しました。")
            return redirect("player_app:search")
    else:
        form_register_pitcher = forms.Register_original_pitcher()

    return render(
        request,
        "register_original_pitcher.html",
        {"form": form_register_pitcher},
    )
    
#オリジナル選手全件取得
@login_required
def original_all_player(request):
    batters = getter["user_batter"](request.user)
    pitchers = getter["user_pitcher"](request.user)
    players = list(batters) + list(pitchers)
    return render(request, "original_player_result.html", {"players": players})


@login_required
def original_player_detail(request, uniform_number):
    text = get_original_player_with_metrics(uniform_number, request.user)
    if not text:
        return render(request, "404.html")
    return render(request, "original_player_detail.html", text)
