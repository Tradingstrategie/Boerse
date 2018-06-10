# Statistik


# Datumsfunktion
def date2int(date):
    xDay = int(date[0:2])
    xMonth = int(date[3:5])
    xYear = int(date[6:10])
    xTimeStamp = xYear*384 + xMonth*32 + xDay
    return xTimeStamp


def statistik(name, tradeliste, beginn='01.01.1991', ende='31.12.2018'):

    bTimeStamp = date2int(beginn)
    eTimeStamp = date2int(ende)
    bJahr = int(beginn[6:10])
    eJahr = int(ende[6:10])

    # Variablen initialisieren
    anzahl = 0
    anzahlC = 0
    anzahlP = 0
    anzahlPlus = 0
    anzahlPlusC = 0
    anzahlPlusP = 0
    anzahlMinus = 0
    anzahlMinusC = 0
    anzahlMinusP = 0

    ergebnis = 0
    ergebnisC = 0
    ergebnisP = 0
    ergebnisPlus = 0
    ergebnisPlusC = 0
    ergebnisPlusP = 0
    ergebnisMinus = 0
    ergebnisMinusC = 0
    ergebnisMinusP = 0

    durchschnitt = 0
    durchschnittC = 0
    durchschnittP = 0

    chanceMax = 0
    chanceMaxC = 0
    chanceMaxP = 0
    plusTrade = 0
    plusTradeC = 0
    plusTradeP = 0
    chanceMaxDatum = '-'
    chanceMaxDatumC = '-'
    chanceMaxDatumP = '-'
    plusTradeDatum = '-'
    plusTradeDatumC = '-'
    plusTradeDatumP = '-'

    risikoMax = 0
    risikoMaxC = 0
    risikoMaxP = 0
    minusTrade = 0
    minusTradeC = 0
    minusTradeP = 0
    risikoMaxDatum = '-'
    risikoMaxDatumC = '-'
    risikoMaxDatumP = '-'
    minusTradeDatum = '-'
    minusTradeDatumC = '-'
    minusTradeDatumP = '-'

    plusQuote = 0
    plusQuoteC = 0
    plusQuoteP = 0

    faktor = 0
    faktorC = 0
    faktorP = 0

    # Jahres-Variablen initialisieren
    anzahlJahr = []
    anzahlJahrC = []
    anzahlJahrP = []
    anzahlPlusJahr = []
    anzahlPlusJahrC = []
    anzahlPlusJahrP = []
    anzahlMinusJahr = []
    anzahlMinusJahrC = []
    anzahlMinusJahrP = []
    ergebnisJahr = []
    ergebnisJahrC = []
    ergebnisJahrP = []
    durchschnittJahr = []
    durchschnittJahrC = []
    durchschnittJahrP = []
    plusQuoteJahr = []
    plusQuoteJahrC = []
    plusQuoteJahrP = []

    for ijahr in range(eJahr-bJahr+1):
        anzahlJahr.append(0)
        anzahlJahrC.append(0)
        anzahlJahrP.append(0)
        anzahlPlusJahr.append(0)
        anzahlPlusJahrC.append(0)
        anzahlPlusJahrP.append(0)
        anzahlMinusJahr.append(0)
        anzahlMinusJahrC.append(0)
        anzahlMinusJahrP.append(0)
        ergebnisJahr.append(0)
        ergebnisJahrC.append(0)
        ergebnisJahrP.append(0)
        durchschnittJahr.append(0)
        durchschnittJahrC.append(0)
        durchschnittJahrP.append(0)
        plusQuoteJahr.append(0)
        plusQuoteJahrC.append(0)
        plusQuoteJahrP.append(0)

    # Tradeliste einlesen und Statistik berechnen
    for itrade in range(len(tradeliste)):

        # Tradeliste wird Zeilenweise eingelesen
        tradeCount = tradeliste[itrade][0]
        typ = tradeliste[itrade][1]
        nameWP = tradeliste[itrade][2]
        kaufDatum = tradeliste[itrade][3]
        kaufZeitpunkt = tradeliste[itrade][4]
        kaufEinheiten = tradeliste[itrade][5]
        verkaufDatum = tradeliste[itrade][6]
        verkaufZeitpunkt = tradeliste[itrade][7]
        verkaufEinheiten = tradeliste[itrade][8]
        haltedauer = tradeliste[itrade][9]
        kaufKurs = tradeliste[itrade][10]
        verkaufKurs = tradeliste[itrade][11]
        gewinn = tradeliste[itrade][12]
        gewinnPro = tradeliste[itrade][13]
        intradayChance = tradeliste[itrade][14]
        intradayRisiko = tradeliste[itrade][15]
        kaufRegel = tradeliste[itrade][16]
        verkaufRegel = tradeliste[itrade][17]

        # Statistik berechnen
        if date2int(kaufDatum) >= bTimeStamp and date2int(kaufDatum) <= eTimeStamp:

            # Auswertung Calls
            if typ == 'Call':
                anzahlC += 1
                ergebnisC = ergebnisC + gewinnPro
                durchschnittC = ergebnisC / anzahlC
                if chanceMaxC < intradayChance:
                    chanceMaxC = intradayChance
                    chanceMaxDatumC = kaufDatum
                if plusTradeC < gewinnPro:
                    plusTradeC = gewinnPro
                    plusTradeDatumC = kaufDatum
                if risikoMaxC > intradayRisiko:
                    risikoMaxC = intradayRisiko
                    risikoMaxDatumC = kaufDatum
                if minusTradeC > gewinnPro:
                    minusTradeC = gewinnPro
                    minusTradeDatumC = kaufDatum
                if gewinn >= 0:
                    anzahlPlusC += 1
                    ergebnisPlusC = ergebnisPlusC + gewinnPro
                else:
                    anzahlMinusC += 1
                    ergebnisMinusC = ergebnisMinusC + gewinnPro
                plusQuoteC = anzahlPlusC / anzahlC * 100
                if ergebnisMinusC > 0:
                    faktorC = ergebnisPlusC / ergebnisMinusC * (-1)

            # Auswertung Puts
            if typ == 'Put':
                anzahlP += 1
                ergebnisP = ergebnisP + gewinnPro
                durchschnittP = ergebnisP / anzahlP
                if chanceMaxP < intradayChance:
                    chanceMaxP = intradayChance
                    chanceMaxDatumP = kaufDatum
                if plusTradeP < gewinnPro:
                    plusTradeP = gewinnPro
                    plusTradeDatumP = kaufDatum
                if risikoMaxP > intradayRisiko:
                    risikoMaxP = intradayRisiko
                    risikoMaxDatumP = kaufDatum
                if minusTradeP > gewinnPro:
                    minusTradeP = gewinnPro
                    minusTradeDatumP = kaufDatum
                if gewinn >= 0:
                    anzahlPlusP += 1
                    ergebnisPlusP = ergebnisPlusP + gewinnPro
                else:
                    anzahlMinusP += 1
                    ergebnisMinusP = ergebnisMinusP + gewinnPro
                plusQuoteP = anzahlPlusP / anzahlP * 100
                if ergebnisMinusP > 0:
                    faktorP = ergebnisPlusP / ergebnisMinusP * (-1)

            # Auswertung alle Trades
            anzahl = anzahlC + anzahlP
            ergebnis = ergebnis + gewinnPro
            durchschnitt = ergebnis / anzahl
            if chanceMax < intradayChance:
                chanceMax = intradayChance
                chanceMaxDatum = kaufDatum
            if plusTrade < gewinnPro:
                plusTrade = gewinnPro
                plusTradeDatum = kaufDatum
            if risikoMax > intradayRisiko:
                risikoMax = intradayRisiko
                risikoMaxDatum = kaufDatum
            if minusTrade > gewinnPro:
                minusTrade = gewinnPro
                minusTradeDatum = kaufDatum
            anzahlPlus = anzahlPlusC + anzahlPlusP
            anzahlMinus = anzahlMinusC + anzahlMinusP
            ergebnisPlus = ergebnisPlusC + ergebnisPlusP
            ergebnisMinus = ergebnisMinusC + ergebnisMinusP
            plusQuote = anzahlPlus / anzahl * 100
            if ergebnisMinus > 0:
                faktor = ergebnisPlus / ergebnisMinus * (-1)

            # Berechnung Jahreswerte
            jahr = int(kaufDatum[6:10])

            if typ == 'Call':
                if gewinn >= 0:
                    anzahlPlusJahrC[jahr-bJahr] += 1
                else:
                    anzahlMinusJahrC[jahr-bJahr] += 1
                anzahlJahrC[jahr-bJahr] += 1
                ergebnisJahrC[jahr-bJahr] = ergebnisJahrC[jahr-bJahr] + gewinnPro

            if typ == 'Put':
                if gewinn >= 0:
                    anzahlPlusJahrP[jahr-bJahr] += 1
                else:
                    anzahlMinusJahrP[jahr-bJahr] += 1
                anzahlJahrP[jahr-bJahr] += 1
                ergebnisJahrP[jahr-bJahr] = ergebnisJahrP[jahr-bJahr] + gewinnPro

            anzahlPlusJahr[jahr-bJahr] = anzahlPlusJahrC[jahr-bJahr] + anzahlPlusJahrP[jahr-bJahr]
            anzahlMinusJahr[jahr-bJahr] = anzahlMinusJahrC[jahr-bJahr] + anzahlMinusJahrP[jahr-bJahr]
            anzahlJahr[jahr-bJahr] += 1
            ergebnisJahr[jahr-bJahr] = ergebnisJahr[jahr-bJahr] + gewinnPro

            if anzahlJahr[jahr-bJahr] > 0:
                durchschnittJahr[jahr-bJahr] = ergebnisJahr[jahr-bJahr] / anzahlJahr[jahr-bJahr]
                plusQuoteJahr[jahr-bJahr] = anzahlPlusJahr[jahr-bJahr] / anzahlJahr[jahr-bJahr] * 100
            if anzahlJahrC[jahr-bJahr] > 0:
                durchschnittJahrC[jahr-bJahr] = ergebnisJahrC[jahr-bJahr] / anzahlJahrC[jahr-bJahr]
                plusQuoteJahrC[jahr-bJahr] = anzahlPlusJahrC[jahr-bJahr] / anzahlJahrC[jahr-bJahr] * 100
            if anzahlJahrP[jahr-bJahr] > 0:
                durchschnittJahrP[jahr-bJahr] = ergebnisJahrP[jahr-bJahr] / anzahlJahrP[jahr-bJahr]
                plusQuoteJahrP[jahr-bJahr] = anzahlPlusJahrP[jahr-bJahr] / anzahlJahrP[jahr-bJahr] * 100

    # Ausgabe der Statistik
    print()
    print('Statistik für ' + str(name) + ' (' + str(beginn) + ' - ' + str(ende)+ ')')
    print()
    print('Gesamtstatistik:')
    print('  Anzahl Trades: ' + str("{:3.0f}".format(anzahl)) + ' (' + str(anzahlPlus) + '/' + str(anzahlMinus) + ') Trades, Ergebnis: ' + str("{:+.2f}".format(ergebnis)) + '%, Durchschnitt pro Trade: ' + str("{:+.2f}".format(durchschnitt)) + '%, Plusquote: ' + str("{:.2f}".format(plusQuote)) + '%, Faktor: ' + str("{:.2f}".format(faktor)))
    print('    Plustrades:  ' + str("{:3.0f}".format(anzahlPlus)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisPlus)) + '%')
    print('    Minustrades: ' + str("{:3.0f}".format(anzahlMinus)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisMinus)) + '%')
    print('  bester Trade:             ' + str("{:+7.2f}".format(plusTrade)) + '% (' + str(plusTradeDatum) + ')')
    print('  maximale Intradaychance:  ' + str("{:+7.2f}".format(chanceMax)) + '% (' + str(chanceMaxDatum) + ')')
    print('  schlechtester Trade:      ' + str("{:+7.2f}".format(minusTrade)) + '% (' + str(minusTradeDatum) + ')')
    print('  maximales Intradayrisiko: ' + str("{:+7.2f}".format(risikoMax)) + '% (' + str(risikoMaxDatum) + ')')
    print()
    print('Auswertung Calls:')
    print('  Anzahl Trades: ' + str("{:3.0f}".format(anzahlC)) + ' (' + str(anzahlPlusC) + '/' + str(anzahlMinusC) + ') Trades, Ergebnis: ' + str("{:+.2f}".format(ergebnisC)) + '%, Durchschnitt pro Trade: ' + str("{:+.2f}".format(durchschnittC)) + '%, Plusquote: ' + str("{:.2f}".format(plusQuoteC)) + '%, Faktor: ' + str("{:.2f}".format(faktorC)))
    print('    Plustrades:  ' + str("{:3.0f}".format(anzahlPlusC)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisPlusC)) + '%')
    print('    Minustrades: ' + str("{:3.0f}".format(anzahlMinusC)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisMinusC)) + '%')
    print('  bester Trade:             ' + str("{:+7.2f}".format(plusTradeC)) + '% (' + str(plusTradeDatumC) + ')')
    print('  maximale Intradaychance:  ' + str("{:+7.2f}".format(chanceMaxC)) + '% (' + str(chanceMaxDatumC) + ')')
    print('  schlechtester Trade:      ' + str("{:+7.2f}".format(minusTradeC)) + '% (' + str(minusTradeDatumC) + ')')
    print('  maximales Intradayrisiko: ' + str("{:+7.2f}".format(risikoMaxC)) + '% (' + str(risikoMaxDatumC) + ')')
    print()
    print('Auswertung Puts:')
    print('  Anzahl Trades: ' + str("{:3.0f}".format(anzahlP)) + ' (' + str(anzahlPlusP) + '/' + str(anzahlMinusP) + ') Trades, Ergebnis: ' + str("{:+.2f}".format(ergebnisP)) + '%, Durchschnitt pro Trade: ' + str("{:+.2f}".format(durchschnittP)) + '%, Plusquote: ' + str("{:.2f}".format(plusQuoteP)) + '%, Faktor: ' + str("{:.2f}".format(faktorP)))
    print('    Plustrades:  ' + str("{:3.0f}".format(anzahlPlusP)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisPlusP)) + '%')
    print('    Minustrades: ' + str("{:3.0f}".format(anzahlMinusP)) + ' Trades, Ergebnis: ' + str("{:+7.2f}".format(ergebnisMinusP)) + '%')
    print('  bester Trade:             ' + str("{:+7.2f}".format(plusTradeP)) + '% (' + str(plusTradeDatumP) + ')')
    print('  maximale Intradaychance:  ' + str("{:+7.2f}".format(chanceMaxP)) + '% (' + str(chanceMaxDatumP) + ')')
    print('  schlechtester Trade:      ' + str("{:+7.2f}".format(minusTradeP)) + '% (' + str(minusTradeDatumP) + ')')
    print('  maximales Intradayrisiko: ' + str("{:+7.2f}".format(risikoMaxP)) + '% (' + str(risikoMaxDatumP) + ')')
    print()
    print()
    print('Jahreswerte:')
    print('  Jahr    Gesamt                              Call                                Put')
    print('       Trades(+/-) Gewinn proTrade +Quote  Trades(+/-) Gewinn proTrade +Quote  Trades(+/-) Gewinn proTrade +Quote')
    # Ausgabe Jahreswerte
    for ijahr in range(eJahr-bJahr+1):
        print('  ' + str(bJahr+ijahr) + ': ' + str("{:3.0f}".format(anzahlJahr[ijahr])) + '(' + str("{:2.0f}".format(anzahlPlusJahr[ijahr])) + '/' + str("{:2.0f}".format(anzahlMinusJahr[ijahr])) + ')' + str("{:+7.2f}".format(ergebnisJahr[ijahr])) + '%' + str("{:+6.2f}".format(durchschnittJahr[ijahr])) + '%' + str("{:+8.2f}".format(plusQuoteJahr[ijahr])) + '%  '
               + str("{:3.0f}".format(anzahlJahrC[ijahr])) + '(' + str("{:2.0f}".format(anzahlPlusJahrC[ijahr])) + '/' + str("{:2.0f}".format(anzahlMinusJahrC[ijahr])) + ')' + str("{:+7.2f}".format(ergebnisJahrC[ijahr])) + '%' + str("{:+6.2f}".format(durchschnittJahrC[ijahr])) + '%' + str("{:+8.2f}".format(plusQuoteJahrC[ijahr])) + '%  '
               + str("{:3.0f}".format(anzahlJahrP[ijahr])) + '(' + str("{:2.0f}".format(anzahlPlusJahrP[ijahr])) + '/' + str("{:2.0f}".format(anzahlMinusJahrP[ijahr])) + ')' + str("{:+7.2f}".format(ergebnisJahrP[ijahr])) + '%' + str("{:+6.2f}".format(durchschnittJahrP[ijahr])) + '%' + str("{:+8.2f}".format(plusQuoteJahrP[ijahr])) + '%')
    print()
    print()
    print('Statistik Ende.')
    print()
