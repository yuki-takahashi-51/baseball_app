from django import forms

#ここで検索用の名前入力を受け取る　自動バリデーションのため定義も最低限合わせる
class Search_player:
    name = forms.CharField()
    
#ユーザー登録用フォーム
class Register_user(forms.Form):
    username = forms.CharField(label="ユーザー名")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
    email = forms.EmailField(label="メールアドレス")
    first_name = forms.CharField(required=False, label="ニックネーム")
    
#ログイン用フォーム
class Login(forms.Form):
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

#オリジナル打者登録
class Register_original_batter(forms.Form):
    uniform_number = forms.IntegerField(label="背番号")
    player_name = forms.CharField(label="選手名")
    games = forms.IntegerField(label="試合数")
    numPlate = forms.IntegerField(label="打席数")
    numBat = forms.IntegerField(label="打数")
    points = forms.IntegerField(label="得点")
    hits = forms.IntegerField(label="安打数")
    hit2nd = forms.IntegerField(label="二塁打")
    hit3rd = forms.IntegerField(label="三塁打")
    homeruns = forms.IntegerField(label="本塁打")
    baseHits = forms.IntegerField(label="塁打数")
    getpoint = forms.IntegerField(label="打点")
    steal = forms.IntegerField(label="盗塁")
    missedSteal = forms.IntegerField(label="盗塁死")
    bants = forms.IntegerField(label="犠打")
    sacFry = forms.IntegerField(label="犠飛")
    fourballs = forms.IntegerField(label="四球")
    intWalk = forms.IntegerField(label="敬遠")
    deadballs = forms.IntegerField(label="死球")
    strikeOut = forms.IntegerField(label="三振")
    doublePlay = forms.IntegerField(label="併殺打")
    errors = forms.IntegerField(label="失策")
    birthday = forms.DateField(required=False, label="生年月日", widget=forms.DateInput(attrs={'type': 'date'}))
    position = forms.CharField(label="守備位置", max_length=1)
    batting_hand = forms.CharField(required=False, label="打ち手", max_length=1)
    throwing_hand = forms.CharField(required=False, label="投げ手", max_length=1)
        
#オリジナル投手登録
class Register_original_pitcher(forms.Form):
    uniform_number = forms.IntegerField(label="背番号")
    player_name = forms.CharField(label="選手名")
    birthday = forms.DateField(required=False, label="生年月日", widget=forms.DateInput(attrs={'type': 'date'}))
    position = forms.CharField(label="守備位置", max_length=1)
    games = forms.IntegerField(label="試合数")
    win = forms.IntegerField(label="勝利")
    lose = forms.IntegerField(label="敗北")
    saves = forms.IntegerField(label="セーブ")
    hold = forms.IntegerField(label="ホールド")
    hp = forms.IntegerField(label="HP")
    fullIning = forms.IntegerField(label="完投")
    perfect = forms.IntegerField(label="完封")
    noFour = forms.IntegerField(label="無四死球")
    batter = forms.IntegerField(label="対戦打者数")
    ining = forms.IntegerField(label="投球回")
    hit = forms.IntegerField(label="被安打")
    homerun = forms.IntegerField(label="被本塁打")
    fourball = forms.IntegerField(label="与四球")
    intWalk = forms.IntegerField(label="敬遠")
    deadBall = forms.IntegerField(label="与死球")
    strikeOut = forms.IntegerField(label="奪三振")
    wildPitch = forms.IntegerField(label="暴投")
    balk = forms.IntegerField(label="ボーク")
    lostScore = forms.IntegerField(label="失点")
    earnedRun = forms.IntegerField(label="自責点")
    ERA = forms.FloatField(label="防御率")
    QS = forms.IntegerField(label="QS")
    batting_hand = forms.CharField(required=False, label="打ち手", max_length=1)
    throwing_hand = forms.CharField(required=False, label="投げ手", max_length=1)
