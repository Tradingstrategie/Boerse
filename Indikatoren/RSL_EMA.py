# Indikator RSL_EMA


def rsl_ema(data, n=9):

    i = 0
    #ema = 0
    rsl_emaL = []

    for idata in data:
        if i > 0:
            ema = ema + 2/(n+1)*(idata - ema)
        else:
            ema = idata
        rsl_ema = ema / idata * 100
        rsl_emaL.append(rsl_ema)
        i += 1

    return rsl_emaL
