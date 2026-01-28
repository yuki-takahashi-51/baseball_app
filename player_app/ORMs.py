from .models import User, Batter, Pitcher, Batting_status, Pitching_status, User_batter, User_pitcher, User_batting_status, User_pitching_status

def get_allplayer():    #選手全件取得
    batters = Batter.objects.all()
    pitchers = Pitcher.objects.all()
    return list(batters)+list(pitchers)

def get_player_by_name(name: str):    #名前で選手取得
    batters = Batter.objects.filter(player_name__contains=name) if name else []
    pitchers = Pitcher.objects.filter(player_name__contains=name) if name else []
    return list(batters)+list(pitchers)
    
def get_player_by_unform_number(uniform_number: int):    #背番号で選手取得
    batter = Batter.objects.filter(uniform_number=uniform_number).first()
    if batter:
        return batter, "batter"

    pitcher = Pitcher.objects.filter(uniform_number=uniform_number).first()
    if pitcher:
        return pitcher, "pitcher"

    return None, None

def get_player_batting(uniform_number: int):    #打撃成績取得
    return Batting_status.objects.filter(uniform_number=uniform_number)

def get_player_pitching(uniform_number: int):    #投球成績取得
    return Pitching_status.objects.filter(uniform_number=uniformnumber)

def get_user_batters(user: User):    #オリジナル打者取得
    return User_batter.objects.filter(user=user)

def get_user_pitchers(user: User):    #オリジナル投手取得
    return User_pitcher.objects.filter(user=user)

def get_user_player_by_uniform_number(uniform_number: int, user: User):    #オリジナル選手全取得
    batter = User_batter.objects.filter(uniform_number=uniform_number, user=user).first()
    if batter:
        return batter, "batter"

    pitcher = User_pitcher.objects.filter(uniform_number=uniform_number, user=user).first()
    if pitcher:
        return pitcher, "pitcher"

    return None, None

def get_user_player_batting(player: User_batter):    #オリジナル打撃成績取得
    return User_batting_status.objects.filter(player=player).first()

def get_user_player_pitching(player: User_pitcher):    #オリジナル投球成績取得
    return User_pitching_status.objects.filter(player=player).first()

#ユーザー登録
def create_user(email: str, password: str, username: str, first_name: str):
    return User.objects.create_user(
        email=email,
        password=password,
        username=username,
        first_name=first_name
    )

#打者登録
def create_batter(
    user,
    uniform_number,
    player_name,
    games=0,
    numPlate=0,
    numBat=0,
    points=0,
    hits=0,
    hit2nd=0,
    hit3rd=0,
    homeruns=0,
    baseHits=0,
    getpoint=0,
    steal=0,
    missedSteal=0,
    bants=0,
    sacFry=0,
    fourballs=0,
    intWalk=0,
    deadballs=0,
    strikeOut=0,
    doublePlay=0,
    errors=0,
    birthday=None,
    position=None,
    batting_hand=None,
    throwing_hand=None
):
    batter = User_batter.objects.create(
        user=user,
        uniform_number=uniform_number,
        player_name=player_name,
        position=position,
        birthday=birthday,
        batting_hand=batting_hand,
        throwing_hand=throwing_hand
    )
    User_batting_status.objects.create(
        player=batter,
        games=games,
        numPlate=numPlate,
        numBat=numBat,
        points=points,
        hits=hits,
        hit2nd=hit2nd,
        hit3rd=hit3rd,
        homeruns=homeruns,
        baseHits=baseHits,
        getpoint=getpoint,
        steal=steal,
        missedSteal=missedSteal,
        bants=bants,
        sacFry=sacFry,
        fourballs=fourballs,
        intWalk=intWalk,
        deadballs=deadballs,
        strikeOut=strikeOut,
        doublePlay=doublePlay,
        errors=errors
    )
    return batter

#投手登録
def create_pitcher(
    user,
    uniform_number,
    player_name,
    birthday=None,
    position=None,
    batting_hand=None,
    throwing_hand=None,
    games=0,
    win=0,
    lose=0,
    saves=0,
    hold=0,
    hp=0,
    fullIning=0,
    perfect=0,
    noFour=0,
    batter=0,
    ining=0,
    hit=0,
    homerun=0,
    fourball=0,
    intWalk=0,
    deadBall=0,
    strikeOut=0,
    wildPitch=0,
    balk=0,
    lostScore=0,
    earnedRun=0,
    ERA=0,
    QS=0
):
    pitcher = User_pitcher.objects.create(
        user=user,
        uniform_number=uniform_number,
        player_name=player_name,
        birthday=birthday,
        position=position,
        batting_hand=batting_hand,
        throwing_hand=throwing_hand,
    )
    User_pitching_status.objects.create(
        player=pitcher,
        games=games,
        win=win,
        lose=lose,
        saves=saves,
        hold=hold,
        hp=hp,
        fullIning=fullIning,
        perfect=perfect,
        noFour=noFour,
        batter=batter,
        ining=ining,
        hit=hit,
        homerun=homerun,
        fourball=fourball,
        intWalk=intWalk,
        deadBall=deadBall,
        strikeOut=strikeOut,
        wildPitch=wildPitch,
        balk=balk,
        lostScore=lostScore,
        earnedRun=earnedRun,
        ERA=ERA,
        QS=QS
    )
    return pitcher
