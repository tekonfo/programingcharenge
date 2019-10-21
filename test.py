import sys

def main(argv):
    # 引数の取得
    daysInYear = int(argv[0])
    daysInMonth = int(argv[1])
    daysInWeek = int(argv[2])
    date = argv[3]

    # カレンダー不正のチェック
    # 日が２桁以下
    if(daysInMonth > 99):
      print(-1)
      return -1

    # 月が２桁以下
    last_month_number = daysInYear / daysInMonth
    if(last_month_number > 99):
      print(-1)
      return -1

    # 日付がカレンダーに含まれるかチェック
    year, month, day = map(lambda x: int(x), date.split("-"))
    if(month > last_month_number or day > daysInMonth):
      print(-1)
      return -1

    # 曜日の計算



if __name__ == '__main__':
    main(sys.argv[1:])
