# Indikator EMA


def ema(data, n=9):

    i = 0
    #ema = 0
    emaL = []

    for idata in data:
        if i > 0:
            ema = ema + 2/(n+1)*(idata - ema)
        else:
            ema = idata
        emaL.append(ema)
        i += 1

    return emaL
