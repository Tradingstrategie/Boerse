# Tradeliste für eine Signalliste


def tradeliste(name, datum, open, high, low, close, signalL):

    # Variablen initialisieren
    tradeL = []

    tradeCount = 0
    einheitenC = 0
    einheitenP = 0
    intradayChanceC = 0
    intradayRisikoC = 0
    intradayChanceP = 0
    intradayRisikoP = 0

    for isignal in range(len(signalL)):

        # Signalliste wird Zeilenweise eingelesen
        tradeGesamt = signalL[isignal][0]
        tradeOpen = signalL[isignal][1]
        tradeOpenV = signalL[isignal][2]
        signalOpenV = signalL[isignal][3]
        wpOpenV = signalL[isignal][4]
        regelOpenV = signalL[isignal][5]
        tradeOpenK = signalL[isignal][6]
        signalOpenK = signalL[isignal][7]
        wpOpenK = signalL[isignal][8]
        regelOpenK = signalL[isignal][9]
        tradeClose = signalL[isignal][10]
        tradeCloseV = signalL[isignal][11]
        signalCloseV = signalL[isignal][12]
        wpCloseV = signalL[isignal][13]
        regelCloseV = signalL[isignal][14]
        tradeCloseK = signalL[isignal][15]
        signalCloseK = signalL[isignal][16]
        wpCloseK = signalL[isignal][17]
        regelCloseK = signalL[isignal][18]

        # intradayChance mit neuem Tag aktualisieren
        if einheitenC > 0 and high[isignal] > intradayChanceC:
            intradayChanceC = high[isignal]
        if einheitenC < 0 and low[isignal] < intradayChanceC:
            intradayChanceC = low[isignal]
        if einheitenP > 0 and high[isignal] > intradayChanceP:
            intradayChanceP = high[isignal]
        if einheitenP < 0 and low[isignal] < intradayChanceP:
            intradayChanceP = low[isignal]

        # intradayRisiko mit neuem Tag aktualisieren
        if einheitenC > 0 and low[isignal] < intradayRisikoC:
            intradayRisikoC = low[isignal]
        if einheitenC < 0 and high[isignal] > intradayRisikoC:
            intradayRisikoC = high[isignal]
        if einheitenP > 0 and low[isignal] < intradayRisikoP:
            intradayRisikoP = low[isignal]
        if einheitenP < 0 and high[isignal] > intradayRisikoP:
            intradayRisikoP = high[isignal]


        # ==================== Zeitpunkt Open ====================
        # ---------- Verkauf Call ----------
        # ---------- Kauf Call ----------
        # ---------- Verkauf Put ----------
        # ---------- Kauf Put ----------


        # ==================== Zeitpunkt Close ====================

        # ---------- Verkauf Call ----------
        if tradeCloseV < 0:
            verkaufZeitC = 'Close'
            haltedauerC = isignal - haltedauerC
            gewinn = close[isignal] - kaufKursC
            gewinnPro = gewinn / kaufKursC * 100

            if high[isignal] > intradayChanceC:
                intradayChanceC = high[isignal]
            intradayChanceC = (intradayChanceC - kaufKursC) / kaufKursC * 100

            if low[isignal] > intradayRisikoC:
                intradayRisikoC = low[isignal]
            intradayRisikoC = (intradayRisikoC - kaufKursC) / kaufKursC * 100

            tradeCount += 1
            trade = [tradeCount, 'Call', name, kaufDatumC, kaufZeitC, kaufEinheitenC, datum[isignal], verkaufZeitC, tradeCloseV, haltedauerC, kaufKursC, close[isignal], gewinn, gewinnPro, intradayChanceC, intradayRisikoC, kaufRegelC, regelCloseV]
            tradeL.append(trade)

            intradayChanceC = 0
            intradayRisikoC = 0
            einheitenC = einheitenC + tradeCloseV

        # ---------- Kauf Call ----------
        if tradeCloseK > 0:
            kaufDatumC = datum[isignal]
            kaufZeitC = 'Close'
            kaufEinheitenC = tradeCloseK
            kaufKursC = close[isignal]
            kaufRegelC = regelCloseK
            haltedauerC = isignal
            intradayChanceC = close[isignal]
            intradayRisikoC = close[isignal]
            einheitenC = einheitenC + tradeCloseK

        # ---------- Verkauf Put ----------
        if tradeCloseV > 0:
            verkaufZeitP = 'Close'
            haltedauerP = isignal - haltedauerP
            gewinn = kaufKursP - close[isignal]
            gewinnPro = gewinn / kaufKursP * 100

            if low[isignal] < intradayChanceP:
                intradayChanceP = low[isignal]
            intradayChanceP = (kaufKursP - intradayChanceP) / kaufKursP * 100

            if high[isignal] > intradayRisikoP:
                intradayRisikoP = high[isignal]
            intradayRisikoP = (kaufKursP - intradayRisikoP) / kaufKursP * 100

            tradeCount += 1
            trade = [tradeCount, 'Put', name, kaufDatumP, kaufZeitP, kaufEinheitenP, datum[isignal], verkaufZeitP, tradeCloseV, haltedauerP, kaufKursP, close[isignal], gewinn, gewinnPro, intradayChanceP, intradayRisikoP, kaufRegelP, regelCloseV]
            tradeL.append(trade)

            intradayChanceP = 0
            intradayRisikoP = 0
            einheitenP = einheitenP + tradeCloseV

        # ---------- Kauf Put ----------
        if tradeCloseK < 0:
            kaufDatumP = datum[isignal]
            kaufZeitP = 'Close'
            kaufEinheitenP = tradeCloseK
            kaufKursP = close[isignal]
            kaufRegelP = regelCloseK
            haltedauerP = isignal
            intradayChanceP = close[isignal]
            intradayRisikoP = close[isignal]
            einheitenP = einheitenP + tradeCloseK

    return tradeL
