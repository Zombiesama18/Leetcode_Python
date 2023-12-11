"""
780. 到达终点
给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。
从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
"""


def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    while sx < tx != ty and sy < ty:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx
    if tx == sx and ty == sy:
        return True
    elif ty == sy:
        return tx > sx and (tx - sx) % ty == 0
    elif tx == sx:
        return ty > sy and (ty - sy) % tx == 0
    else:
        return False
