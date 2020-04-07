import sys
import json
import urllib.request

args = sys.argv

points = 20
count = 0
url = ' https://tanaka-server.herokuapp.com/'

for i in range(3): 
    if points <= 0:
        print("pointsが0以下のため、ゲームを続けることができません。ゲームを終了します。")
        sys.exit()

    print("{}回目の勝負です。".format(i+1))
    print("あなたは今{}ポイント持っています。".format(points))

    bet = input("bet: odd か even を入力してください:")
    point = input("point: 賭けるポイントを整数で入力してください:")

    # バリデーション
    if bet not in ['odd', 'even']:
        print("betにodd, even以外の文字が入力されました。ゲームを終了します")
        sys.exit()

    if not point.isnumeric():
        print("pointsに不正な文字が入力されました。ゲームを終了します。")
        sys.exit()
    
    point = int(point)

    if  not 1 <= point <= points:
        print("pointsに賭けられない数字が賭けられました。ゲームを終了します。")
        sys.exit()

    data = {
        'bet': bet,
        'points': points,
    }

    points -= point

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        res = json.loads(res.read())
    dices = res['dice']
    points += res['points']
    if res['result'] == bet:
        count += 1
        print("当たりました！！！出た目は{}と{}でした。そのため{}ポイント加算されます。\n".format(dices[0], dices[1], res['points']))
    else:
        print("ハズレです、、、出た目は{}と{}でした。\n".format(dices[0],dices[1]))
    
print("~~~~~~~~~~~~~~~~~")
print("\n終了です！あなたは{}回当てており、合計得点は{}です。".format(count, points))

    


    
    