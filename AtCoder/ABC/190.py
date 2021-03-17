
def A():
    Takahashi, Aoki, C = map(int, input().split())

    if Takahashi == Aoki:
        # 先手が負ける
        if C == 0:
            print("Aoki")
        else:
            print("Takahashi")
        exit()

    # アメの数が少ないほうが負ける
    if Takahashi > Aoki:
        print("Takahashi")
    else:
        print("Aoki")

def B():
    n, s, d = map(int, input().split())

    for i in range(n):
        x, y = map(int, input().split())
        # S秒未満かつDより上の威力を持つ呪文かどうか
        if x < s and y > d:
            print("Yes")
            exit()
    print("No")
