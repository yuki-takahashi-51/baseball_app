from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

#ユーザー登録のための関数 メールアドレスとパスワードで認証するためメールを必須にしている　ベースは既に用意してあるもの
class CustomUserManager(BaseUserManager):
    def create_user(this, email: str, password=None, username=None, first_name=None):
        if not email:
            raise ValueError("メールアドレスは必須です")
        email = this.normalize_email(email)

        user = this.model(
            email=email,
            username=username,
            first_name=first_name,
        )
        user.set_password(password)   #パスワードを受け取った後セキュリティのためハッシュ化
        user.save() #userを更新
        return user


#Auth_userに相当するもの　元あるものを基盤としつつ定義を追加　player_countは新しく追加したもの
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)  #認証に使うため重複不可とする
    first_name = models.CharField(max_length=150, blank=True, null=True) 
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    player_count = models.IntegerField(null=True)

    USERNAME_FIELD = "email"    #メールアドレスを認証に使いたいため認証のデフォをユーザ名から変更
    REQUIRED_FIELDS = ["username"]  #スーパーユーザー作成メソッドはないが念のため必要項目を定義
    
    objects = CustomUserManager() 

    class Meta:
        db_table = "user"   #テーブル名をuserとする
 
        

#ここからは自作テーブル　抽象クラスを使用し野球選手として必要な情報を基底側に定義し派生側で野手投手に分ける
#ORMだけを使用するためmodelsにも全く同じ定義を記述
class PlayerBase(models.Model):
    uniform_number = models.IntegerField(primary_key=True)  #これが全体を通して選手を識別する値となる
    player_name = models.CharField(max_length=50)   #背番号をつける人が変わったら意味がないが自動生成を主キーとしたら時間がとてもかかりそうだったため
    birthday = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=2)

    class Meta:
        abstract = True #   ここで抽象クラス宣言 テーブルは作成されない

class Batter(PlayerBase):
    batting_hand = models.CharField(max_length=1)
    throwing_hand = models.CharField(max_length=1)
    
    class Meta:
        db_table = "batter"
        managed = False #こうすることでmigrationは作成されない RunSQLで定義してあることが前提

#結局のところカラムは変わらないがテーブルが違うことがのちに大切なため必要
class Pitcher(PlayerBase):
    throwing_hand = models.CharField(max_length=1)
    batting_hand = models.CharField(max_length=1)
    
    class Meta:
        db_table = "pitcher"
        managed = False


class Batting_status(models.Model):  #batterだけがこのテーブルと背番号で接続　管理しやすいようにすべての
    uniform_number = models.OneToOneField(  #野球関連テーブルは背番号で管理　子の定義から消さねば勝手に親が消えないように定義
        Batter,
        db_column="uniform_number",
        on_delete=models.PROTECT,
        primary_key=True,
        related_name="battingstatus_player"
    )
    games = models.IntegerField(null=True, blank=True)
    numPlate = models.IntegerField(null=True, blank=True)
    numBat = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    hit2nd = models.IntegerField(null=True, blank=True)
    hit3rd = models.IntegerField(null=True, blank=True)
    homeruns = models.IntegerField(null=True, blank=True)
    baseHits = models.IntegerField(null=True, blank=True)
    getpoint = models.IntegerField(null=True, blank=True)
    steal = models.IntegerField(null=True, blank=True)
    missedSteal = models.IntegerField(null=True, blank=True)
    bants = models.IntegerField(null=True, blank=True)
    sacFry = models.IntegerField(null=True, blank=True)
    fourballs = models.IntegerField(null=True, blank=True)
    intWalk = models.IntegerField(null=True, blank=True)
    deadballs = models.IntegerField(null=True, blank=True)
    strikeOut = models.IntegerField(null=True, blank=True)
    doublePlay = models.IntegerField(null=True, blank=True)
    errors = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "batting_status"
        managed = False


class Pitching_status(models.Model):    
    uniform_number = models.OneToOneField(  #これも上と同様pitcherとだけ接続
        Pitcher,
        db_column="uniform_number",
        on_delete=models.PROTECT,
        primary_key=True,
        related_name="pitchingstatus_player"
    )
    games = models.IntegerField(null=True, blank=True)
    win = models.IntegerField(null=True, blank=True)
    lose = models.IntegerField(null=True, blank=True)
    saves = models.IntegerField(null=True, blank=True)
    hold = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    fullIning = models.IntegerField(null=True, blank=True)
    perfect = models.IntegerField(null=True, blank=True)
    noFour = models.IntegerField(null=True, blank=True)
    batter = models.IntegerField(null=True, blank=True)
    ining = models.IntegerField(null=True, blank=True)
    hit = models.IntegerField(null=True, blank=True)
    homerun = models.IntegerField(null=True, blank=True)
    fourball = models.IntegerField(null=True, blank=True)
    int_Walk = models.IntegerField(null=True, blank=True)
    deadBall = models.IntegerField(null=True, blank=True)
    strikeOut = models.IntegerField(null=True, blank=True)
    wildPitch = models.IntegerField(null=True, blank=True)
    balk = models.IntegerField(null=True, blank=True)
    lostScore = models.IntegerField(null=True, blank=True)
    earnedRun = models.IntegerField(null=True, blank=True)
    ERA = models.FloatField(null=True, blank=True)  
    QS = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "pitching_status"
        managed = False
        


#ユーザー用のオリジナル選手

class User_player(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="%(class)ss", 
    )
    uniform_number = models.IntegerField()
    player_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, help_text="他ユーザーに公開しますか")

    class Meta:
        abstract = True
        ordering = ["user", "uniform_number"]


class User_batter(User_player):
    batting_hand = models.CharField(max_length=1, blank=True, null=True)
    throwing_hand = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = "user_batter"
        #同一ユーザー内での背番号の一意性を保証
        unique_together = (("user", "uniform_number"),)
        indexes = [
            models.Index(fields=["user", "uniform_number"]),
            models.Index(fields=["player_name"]),
        ]
        managed = False

    @classmethod
    def create_batter(cls, user, uniform_number, player_name, 
                       games, numPlate, numBat, points, hits, hit2nd, hit3rd,
                       homeruns, baseHits, getpoint, steal, missedSteal, bants,
                       sacFry, fourballs, intWalk, deadballs, strikeOut, doublePlay, errors,
                       birthday=None, position=None, batting_hand=None, throwing_hand=None):
        #背番号の重複確認
        if cls.objects.filter(user=user, uniform_number=uniform_number).exists():
            raise ValidationError(f"背番号 {uniform_number} は既に使用されています。")
        #名前の重複確認
        if cls.objects.filter(user=user, player_name=player_name).exists():
            raise ValidationError(f"選手名 {player_name} は既に存在します。")

        return cls.objects.create(
            user=user,
            uniform_number=uniform_number,
            player_name=player_name,
            birthday=birthday,
            position=position,
            batting_hand=batting_hand,
            throwing_hand=throwing_hand,
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
            missedSteal=missedSteal ,
            bants=bants,
            sacFry=sacFry,
            fourballs=fourballs,
            intWalk=intWalk,
            deadballs=deadballs,
            strikeOut=strikeOut,
            doublePlay=doublePlay,
            errors=errors,
        )

class User_pitcher(User_player):
    throwing_hand = models.CharField(max_length=1, blank=True, null=True)
    batting_hand = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = "user_pitcher"
        unique_together = (("user", "uniform_number"),)
        indexes = [
            models.Index(fields=["user", "uniform_number"]),
            models.Index(fields=["player_name"]),
        ]
        managed = False

    @classmethod
    def create_pitcher(cls, user, uniform_number, player_name,
                   birthday, position, games, win, lose, saves, hold, hp,
                   fullIning, perfect, noFour, batter, ining,
                   hit, homerun, fourball, intWalk, deadBall,
                   strikeOut, wildPitch, balk, lostScore,
                   earnedRun, ERA, QS, batting_hand=None, throwing_hand=None,):
        if cls.objects.filter(user=user, uniform_number=uniform_number).exists():
            raise ValidationError(f"背番号 {uniform_number} は既に使用されています。")
        if cls.objects.filter(user=user, player_name=player_name).exists():
            raise ValidationError(f"選手名 {player_name} は既に存在します。")

        return cls.objects.create(
            user=user,
            uniform_number=uniform_number,
            player_name=player_name,
            birthday=birthday,
            position=position,
            batting_hand=batting_hand,
            throwing_hand=throwing_hand,
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
        
class User_batting_status(models.Model):
    player = models.OneToOneField(
        User_batter,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="batting_status"
    )

    games = models.IntegerField(null=True, blank=True)
    numPlate = models.IntegerField(null=True, blank=True)
    numBat = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    hit2nd = models.IntegerField(null=True, blank=True)
    hit3rd = models.IntegerField(null=True, blank=True)
    homeruns = models.IntegerField(null=True, blank=True)
    baseHits = models.IntegerField(null=True, blank=True)
    getpoint = models.IntegerField(null=True, blank=True)
    steal = models.IntegerField(null=True, blank=True)
    missedSteal = models.IntegerField(null=True, blank=True)
    bants = models.IntegerField(null=True, blank=True)
    sacFry = models.IntegerField(null=True, blank=True)
    fourballs = models.IntegerField(null=True, blank=True)
    intWalk = models.IntegerField(null=True, blank=True)
    deadballs = models.IntegerField(null=True, blank=True)
    strikeOut = models.IntegerField(null=True, blank=True)
    doublePlay = models.IntegerField(null=True, blank=True)
    errors = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "user_batting_status"
        managed = False


class User_pitching_status(models.Model):
    player = models.OneToOneField(
        User_pitcher,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="pitching_status"
    )

    games = models.IntegerField(null=True, blank=True)
    win = models.IntegerField(null=True, blank=True)
    lose = models.IntegerField(null=True, blank=True)
    saves = models.IntegerField(null=True, blank=True)
    hold = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    fullIning = models.IntegerField(null=True, blank=True)
    perfect = models.IntegerField(null=True, blank=True)
    noFour = models.IntegerField(null=True, blank=True)
    batter = models.IntegerField(null=True, blank=True)
    ining = models.IntegerField(null=True, blank=True)
    hit = models.IntegerField(null=True, blank=True)
    homerun = models.IntegerField(null=True, blank=True)
    fourball = models.IntegerField(null=True, blank=True)
    intWalk = models.IntegerField(null=True, blank=True)
    deadBall = models.IntegerField(null=True, blank=True)
    strikeOut = models.IntegerField(null=True, blank=True)
    wildPitch = models.IntegerField(null=True, blank=True)
    balk = models.IntegerField(null=True, blank=True)
    lostScore = models.IntegerField(null=True, blank=True)
    earnedRun = models.IntegerField(null=True, blank=True)
    ERA = models.FloatField(null=True, blank=True)
    QS = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "user_pitching_status"
        managed = False
