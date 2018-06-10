# Modul TagesTrade mit RSL_EMA-Indikator

from Indikatoren.RSL_EMA import *


def tt_rsl_ema(data, n=9, thresNc=105, thresNp=95):

    rsl_emaL = rsl_ema(data, n)

    # Signalgenerierung

    i = 0
    investmentC = 0
    investmentP = 0
    wpClose = 'n'
    regelClose = 'n'
    wpCloseV = 'n'
    regelCloseV = 'n'
    signalL = []

    for idata in data:

        # Signal und Trade ermitteln (Zeitpunkt Close)
        oldinvestmentC = investmentC
        oldinvestmentP = investmentP
        signalClose = 'n'
        signalCloseV = 'n'
        wpCloseV = 'n'
        tradeCloseK = 0
        tradeCloseV = 0

        # Verkauf Tagestrade
        investmentC = 0
        investmentP = 0
        regelClose = 'n'
        regelCloseV = 'n'

        # Call
        # Kaufsignale
        if rsl_emaL[i] >= thresNc:
            investmentC = 1
            signalClose = 'call'
            wpClose = 'call'
            regelClose = 'tagestradeRSL_EMA.'+str(n)+'.'+str(thresNc)
        # Verkaufsignale
        if oldinvestmentC > investmentC:
            signalCloseV = 'verkaufCall'
            wpClose = 'n'
            wpCloseV = 'call'
            regelCloseV = 'tagestradeRSL_EMA.'+str(n)+'.'+str(thresNc)+'.V'

        # Put
        # Kaufsignale
        if rsl_emaL[i] <= thresNp:
            investmentP = -1
            signalClose = 'put'
            wpClose = 'put'
            regelClose = 'tagestradeRSL_EMA.'+str(n)+'.'+str(thresNp)
        # Verkaufsignale
        if oldinvestmentP < investmentP:
            signalCloseV = 'verkaufPut'
            wpClose = 'n'
            wpCloseV = 'put'
            regelCloseV = 'tagestradeRSL_EMA.'+str(n)+'.'+str(thresNp)+'.V'

        # Trade zum Close festlegen (Depot +/- 1)
        tradeCloseC = investmentC - oldinvestmentC
        tradeCloseP = investmentP - oldinvestmentP
        tradeClose = tradeCloseC + tradeCloseP

        if tradeCloseC > 0:
            tradeCloseK = tradeCloseC
        else:
            if tradeCloseC < 0:
                tradeCloseV = tradeCloseC

        if tradeCloseP < 0:
            tradeCloseK = tradeCloseP
        else:
            if tradeCloseP > 0:
                tradeCloseV = tradeCloseP

        # Signal und Trade ermitteln (Zeitpunkt Open)
        tradeOpen = 0

        tradeOpenK = 0
        signalOpen = 'n'
        wpOpen = 'n'
        regelOpen = 'n'

        tradeOpenV = 0
        signalOpenV = 'n'
        wpOpenV = 'n'
        regelOpenV = 'n'

        # TradeGesamt festlegen (Depot +/- 1)
        tradeGesamt = tradeOpen + tradeClose

        signal = [tradeGesamt, tradeOpen, tradeOpenV, signalOpenV, wpOpenV, regelOpenV, tradeOpenK, signalOpen, wpOpen, regelOpen, tradeClose, tradeCloseV, signalCloseV, wpCloseV, regelCloseV, tradeCloseK, signalClose, wpClose, regelClose]
        signalL.append(signal)

        i += 1

    return signalL
