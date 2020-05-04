"""
初乗り運賃　1km 400円
走行距離 10kmまでは 400m 40円
走行距離　10km以降は 350m 40円
10km/h 以下の走行時間 低速運賃として 45秒 40円
深夜12~朝6時までは初乗り運賃、加算金額が5割マシ
朝6時〜9時半、夕方6時〜深夜12時の間はピークタイムとして3割マシ

三つのメーターを作成する
距離メーター
低速走行距離時間メーター
運賃メーター

レコードには時刻と走行距離を記録したものがある
二種類あり、初乗りレコードと走行レコードである。

"""

import datetime

FIRST_PRICE = 400
LOW_SPEED_PRICE = 40
LOW_SPPED = 10
LOW_DIS_SECOND = 45
DIS_PRICE = 40
SHORT_DIS_TMP = 400
SHORT_DIS = 1000
LONG_DIS_TMP = 350
LONG_DIS = 10200

year = 2020
month = 1


class DistanceMeter():
    def __init__(self):
        self.distance = 0.0
        self.tmpDis = 0.0
        self.isLongDis = False

    def add(self, dis):
        self.distance += dis
        self.tmpDis += dis
        if self.distance >= LONG_DIS:
            self.isLongDis = True

class PriceMeter():
    def __init__(self):
        self.price = 400.0
        # 普通の時は1 
        # 深夜時は2
        # ピーク時間は3
        self.timeType = 0
        self.ExPrice = [1, 1.3, 1.5]
    
    def add(self, price):
        self.price += price
    
    def addLowDis(self, count):
        self.price += count*DIS_PRICE*self.ExPrice[self.timeType]
    
    def setType(self, now):
        hour = now.hour
        minute = now.minute
        if 0 <= hour <= 6:
            self.timeType = 1
        elif (6 <= hour and (hour <= 9 and minute <= 30)) or 18 <= hour <= 24:
            self.timeType = 2
    
    def addDis(self, count):
        self.price += count*DIS_PRICE*self.ExPrice[self.timeType]

class LowSpeedMeter():
    def __init__(self):
        self.time = 0.0
        self.tmpTime = 0.0
        self.edge = LOW_SPPED
    
    def isLow(self, time, dis):
        speed = (dis * 0.001) / (time * 3600)
        return speed <= self.edge
        
    def add(self, time):
        self.time += time
        self.tmpTime += time

### エラー処理をしないといけない

import datetime
import sys

records = []

# 時刻と走行距離を持った配列を作成
with open('./sample.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        if line == '':
            print("エラー：空行です")
            sys.exit(1)
        lint = line.split()
        distance = float(lint[1])
        hour, minute, second = lint[0].split(':')
        second, microsecond = second.split('.')
        day, hour = divmod(int(hour), 24)
        day += 1
        dat = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=int(minute), second=int(second), microsecond=int(microsecond))
        # エラー処理
        if len(records) > 0:
            prevTime = records[-1][0]
            if prevTime > dat:
                print("エラー：行が時間でソートされていません")
                sys.exit(1)
            diff = dat - prevTime
            if diff.total_seconds() > 45:
                print("エラー：時間が45秒以上のレコードが存在します。")
                sys.exit(1)
        elif len(records) == 0 and distance != 0.0:
            # 初乗りレコードが距離0.0であることを確認
            print('エラー：初乗りレコードの距離が0.0ではありません')
            sys.exit(1)
        
        prevTime = dat

        records.append([dat, distance])

# エラー処理
if len(records) <= 1:
    print("エラー：行数が2未満です")
    sys.exit(1)

low_meter = LowSpeedMeter()
dis_meter = DistanceMeter()
price_meter = PriceMeter()

# 三つのメーターを実装する
# まず、距離メーターだけ考える
prev = records[0][0]
for record in records[1:]:
    now, distance = record
    price_meter.setType(now)
    diff = now - prev
    diff_time = diff.total_seconds()

    time, distance = record
    # 距離メーターに加算
    dis_meter.add(distance)

    # 低距離メーターに加算
    if low_meter.isLow(diff_time, distance):
        low_meter.add(diff_time)

    # 運賃メーターに加算
    # 低距離メーターチェック
    if low_meter.tmpTime >= LOW_DIS_SECOND:
        count, div = divmod(low_meter.tmpTime, LOW_DIS_SECOND)
        price_meter.addLowDis(count)
        low_meter.tmpTime = div
    
    # 距離メーターチェック
    if dis_meter.isLongDis and dis_meter.tmpDis > LONG_DIS_TMP:
        count, div = divmod(dis_meter.tmpDis, LONG_DIS_TMP)
        price_meter.addDis(count)
        dis_meter.tmpDis = div
    # 長い場合
    elif not dis_meter.isLongDis and dis_meter.tmpDis > SHORT_DIS_TMP:
        count, div = divmod(dis_meter.tmpDis, SHORT_DIS_TMP)
        price_meter.addDis(count)
        dis_meter.tmpDis = div
    prev = now

if dis_meter.distance == 0:
    print("エラー：全体の走行距離が0です。")
    sys.exit(1)

print(price_meter.price)

        




