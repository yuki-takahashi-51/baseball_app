from .models import User, Batter, Pitcher, Batting_status, Pitching_status, User_batter, User_pitcher, User_batting_status, User_pitching_status
from django.shortcuts import get_object_or_404

#ORMを使用する関数をすべてここに格納　機能に合わせてクラス分け
class getter:
    
    @staticmethod
    def get_allplayer():    #選手情報を全件取得
        batters = Batter.objects.all()
        pitchers = Pitcher.objects.all()
        return list(batters)+list(pitchers)
    
    @staticmethod
    def get_playersresult(name: str):    #batterもしくはpitcherに格納されている、名前が入力された値を含んでいる選手を取得する
        batters = Batter.objects.filter(player_name__contains=name) if name else []
        pitchers = Pitcher.objects.filter(player_name__contains=name) if name else []
        return list(batters)+list(pitchers)
        
    @staticmethod
    def get_player(uniform_number: int):
        try:    #batterテーブルから引数で渡された背番号と一致する選手を取得する
            return Batter.objects.get(uniform_number=uniform_number), "batter"
        except Batter.DoesNotExist:
            return get_object_or_404(Pitcher, uniform_number=uniform_number), "pitcher"
     #存在しなければpitcherテーブルに同様の処理をし見つからなければ404を返す
     
    @staticmethod   
    def get_player_batting(uniform_number: int):
        return Batting_status.objects.get(uniform_number=uniform_number)
    
    @staticmethod    
    def get_player_pitching(uniformnumber: int):
        return Pitching_status.objects.get(uniform_number=uniformnumber)

    @staticmethod
    def get_user_batters(user: User):
        return User_batter.objects.filter(user=user)

    @staticmethod
    def get_user_pitchers(user: User):
        return User_pitcher.objects.filter(user=user)

    @staticmethod #背番号取得
    def get_user_player(uniform_number: int, user: User):
        try:
            return User_batter.objects.get(user=user, uniform_number=uniform_number), "batter"
        except User_batter.DoesNotExist:
            return get_object_or_404(User_pitcher, user=user, uniform_number=uniform_number), "pitcher"

    @staticmethod
    def get_user_player_batting(player: User_batter):
        return get_object_or_404(User_batting_status, player=player)

    @staticmethod
    def get_user_player_pitching(player: User_pitcher):
        return get_object_or_404(User_pitching_status, player=player)
    
class setter:
    #ユーザー登録
    @staticmethod
    def creata_user(email: str, password: str, username: str, first_name: str):
        User.objects.create_user(
            email=email,
            password=password,
            username=username,
            first_name=first_name
        )
    
    #打者登録
    @staticmethod
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

        if any(v is not None for v in [
            games, numPlate, numBat, points, hits, hit2nd, hit3rd,
            homeruns, baseHits, getpoint, steal, missedSteal, bants,
            sacFry, fourballs, intWalk, deadballs, strikeOut, doublePlay, errors
        ]):
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
    @staticmethod
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

        if any(v is not None for v in [
            games, win, lose, saves, hold, hp,
            fullIning, perfect, noFour, batter, ining,
            hit, homerun, fourball, intWalk, deadBall,
            strikeOut, wildPitch, balk, lostScore,
            earnedRun, ERA, QS
        ]):
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
