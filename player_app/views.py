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


def search(request):    #検索画面
    form_search = forms.Search_player()
    return render(request, "search.html", {"form":form_search})

def result(request):    #検索結果表示　
    name = ""
    players = []
    if request.method == "POST":
        name = request.POST.get("player_name", "") 
        players = getter["players"](name)
        text = {"name": name, "players": players}
    return render(request, "result.html", text)

#背番号から選手個人の情報を引き出す　nameはバーに表示するのに必要だったため
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

#詳細情報取得
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
    #指標計算用の関数を取得
    metrics = batter_metrics(batting) if batting else pitcher_metrics(pitching)      
    
    text = {"player": player, "batting": batting, "pitching": pitching, "metrics":metrics}
    return render(request, "player_detail.html", text)

#選手データをCSVでダウンロード
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
        pitching.fourball, pitching.deadBall, pitching.intWalk, pitching.noFour,
        pitching.wildPitch, pitching.balk, pitching.lostScore, pitching.earnedRun
    ])

        writer.writerow([])
        writer.writerow(["投手指標"])
        for key, value in metrics_pitch.items():
            writer.writerow([key, value])
        writer.writerow([])
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
    print("create_pitcher called with:", locals())
    if request.method == "POST":
        form_register_pitcher = forms.Register_original_pitcher(request.POST)
        print(request.POST)
        if form_register_pitcher.is_valid():
            print("create_pitcher called with:", locals())
            print("Form is valid!", form_register_pitcher.cleaned_data)
            cd = form_register_pitcher.cleaned_data
            def safe_int(val):
                try:
                    return int(val)
                except (TypeError, ValueError):
                    return 0
            def safe_float(val):
                try:
                    return float(val)
                except (TypeError, ValueError):
                    return 0.0
            try:
                pitcher = setter["create_pitcher"](
                    user=request.user,
                    uniform_number=cd["uniform_number"],
                    player_name=cd["player_name"],
                    position=cd["position"],
                    birthday=cd.get("birthday") or None,
                    batting_hand=cd.get("batting_hand") or None,
                    throwing_hand=cd.get("throwing_hand") or None,
                    games=safe_int(cd.get("games")),
                    ERA=safe_float(cd.get("ERA")),
                    win=safe_int(cd.get("win")),
                    lose=safe_int(cd.get("lose")),
                    saves=safe_int(cd.get("saves")),
                    hold=safe_int(cd.get("hold")),
                    hp=safe_int(cd.get("hp")),
                    fullIning=safe_int(cd.get("fullIning")),
                    perfect=safe_int(cd.get("perfect")),
                    noFour=safe_int(cd.get("noFour")),
                    batter=safe_int(cd.get("batter")),
                    ining=safe_int(cd.get("ining")),
                    hit=safe_int(cd.get("hit")),
                    homerun=safe_int(cd.get("homerun")),
                    fourball=safe_int(cd.get("fourball")),
                    intWalk=safe_int(cd.get("intWalk")),
                    deadBall=safe_int(cd.get("deadBall")),
                    strikeOut=safe_int(cd.get("strikeOut")),
                    wildPitch=safe_int(cd.get("wildPitch")),
                    balk=safe_int(cd.get("balk")),
                    lostScore=safe_int(cd.get("lostScore")),
                    earnedRun=safe_int(cd.get("earnedRun")),
                    QS=safe_int(cd.get("QS"))
                )
                print("pitcher created:", pitcher.id)
                print(User_pitching_status.objects.filter(player=pitcher).exists())
                messages.success(request, "投手を登録しました。")
                return redirect("player_app:search") 
            except Exception as e:
                    print("pitcher creation failed:", e)
                    traceback.print_exc()
                    messages.error(request, f"登録に失敗しました: {e}")
        else:
            print("Form errors:", form_register_pitcher.errors)
    else:
        form_register_pitcher = forms.Register_original_pitcher()
    print("Saved successfully")
    return render(request, "register_original_pitcher.html", {"form": form_register_pitcher})

#オリジナル選手全件取得
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
            pitching = getter["user_pitching"](player)
        except User_pitching_status.DoesNotExist:
            pitching = None

    metrics = batter_metrics(batting) if batting else pitcher_metrics(pitching)

    context = {
        "player": player,
        "batting": batting,
        "pitching": pitching,
        "metrics": metrics
    }
    return render(request, "original_player_detail.html", context)

