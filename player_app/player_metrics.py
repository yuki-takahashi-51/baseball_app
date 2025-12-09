#指標計算のための関数


DOUBLE = 2
TRIPLE = 3
HOMERUN = 4
NINE_INNINGS = 9
DECIMAL_PLACES = 3


def batter_metrics(batting):
    if not batting:
        return {}
#成績
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

    #長打関係
    singles = H - double - triple - HR
    total_bases = (
        singles * 1 +
        double * DOUBLE +
        triple * TRIPLE +
        HR * HOMERUN
    )

    #指標計算
    AVG = round(H / bat, DECIMAL_PLACES) if bat else 0
    OBP = round((H + four + dead) / plate, DECIMAL_PLACES) if plate else 0
    SLG = round(total_bases / bat, DECIMAL_PLACES) if bat else 0
    OPS = round(OBP + SLG, DECIMAL_PLACES) if bat else 0
    IsoP = round(SLG - AVG, DECIMAL_PLACES) if bat else 0

    return {
        "AVG": AVG,
        "OBP": OBP,
        "SLG": SLG,
        "OPS": OPS,
        "IsoP": IsoP,
        "SO_percent": round(K / plate, DECIMAL_PLACES) if plate else 0,
        "BB_percent": round(four / plate, DECIMAL_PLACES) if plate else 0,
        "BB_per_SO": round(four / K, DECIMAL_PLACES) if four else 0,
        "R_per_PA": round(point / plate, DECIMAL_PLACES) if plate else 0,
        "RBI_per_PA": round(RBI / plate, DECIMAL_PLACES) if plate else 0,
    }


def pitcher_metrics(pitching):
    if not pitching:
        return {}

    #成績
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
        "win_percent": round(win / (win + lose), DECIMAL_PLACES) if (win + lose) else 0,
        "K_per_9": round(K * NINE_INNINGS / ining, DECIMAL_PLACES) if ining else 0,
        "BB_per_9": round(four * NINE_INNINGS / ining, DECIMAL_PLACES) if ining else 0,
        "K_per_BB": round(K / four, DECIMAL_PLACES) if four else 0,
        "BB_plus_HBP_per_9": round((four + dead) * NINE_INNINGS / ining, DECIMAL_PLACES) if ining else 0,
        "BAA": round(H / batter, DECIMAL_PLACES) if batter else 0,
        "HR_per_9": round(HR * NINE_INNINGS / ining, DECIMAL_PLACES) if ining else 0,
        "H_per_9": round(H * NINE_INNINGS / ining, DECIMAL_PLACES) if ining else 0,
        "WHIP": round((four + H) / ining, DECIMAL_PLACES) if ining else 0,
    }
