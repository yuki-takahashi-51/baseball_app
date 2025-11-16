#打者と投手の指標計算のための関数をまとめたもの

def batter_metrics(batting):
    if not batting:
        return {}
    
    plate = batting.numPlate
    bat = batting.numBat
    H = batting.hits
    double = batting.hit2nd
    triple = batting.hit3rd
    HR = batting.homeruns
    point = batting.points
    RBI = batting.getpoint
    four = batting.fourballs
    dead = batting.deadballs
    K = batting.strikeOut
    
    return {
        "AVG":round(H/bat,3)if bat else 0,#打率
        "OBP":round((H+four+dead)/plate,3)if plate else 0,#出塁率
        "SLG":round(((H-double-triple-HR)+double*2+triple*3+HR*4)/bat,3)if bat else 0,#長打率
        "OPS":round(((H+four+dead)/plate)+(((H-double-triple-HR)+double*2+triple*3+HR*4)/bat),3)if bat else 0,#OPS
        "IsoP":round((((H-double-triple-HR)+double*2+triple*3+HR*4)/bat)-(H/bat),3)if bat else 0,#純長打率
        "SO_percent":round(K/plate,3)if plate else 0,#三振率
        "BB_percent":round(four/plate,3)if plate else 0,#四球率
        "BB_per_SO":round(four/K,3)if four else 0,#四球/三振比
        "R_per_PA":round(point/plate,3)if plate else 0,#打席あたりの得点
        "RBI_per_PA":round(RBI/plate,3)if plate else 0 #打席あたりの打点
    }
    
def pitcher_metrics(pitching):
    if not pitching:
        return{}
    
    win = pitching.win
    lose = pitching.lose
    QS = pitching.QS
    games = pitching.games
    ining = pitching.ining
    K = pitching.strikeOut
    four = pitching.fourball
    dead = pitching.deadBall
    H = pitching.hit
    HR = pitching.homerun
    batter = pitching.batter
    ERA = pitching.ERA
    
    return {
        "win_percent":round(win/(win+lose),3)if (win+lose) else 0,#勝率
        "K_per_9":round(K*9/ining,3)if ining else 0,#9回あたりの奪三振数
        "BB_per_9":round(four*9/ining,3)if ining else 0,#9回あたりの与四球数
        "K_per_BB":round(K/four,3)if four else 0,#三振/四球比
        "BB_plus_HBP_per_9":round((four+dead)*9/ining,3)if ining else 0,#9回あたりの与死四球
        "BAA":round(H/batter,3)if batter else 0,#打者に安打を許した確率
        "HR_per_9":round(HR*9/ining,3)if ining else 0,#9回ごとの被本塁打
        "H_per_9":round(H*9/ining,3)if ining else 0,#9回ごとの被安打
        "WHIP":round((four+H)/ining,3)if ining else 0,#1イニングあたりの平均走者数
    }