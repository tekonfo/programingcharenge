MAX_BIT = 2**31 -1
MIN_BIT = -2**31

class Solution:
  def isfloat(self, parameter):
    if not parameter.isdecimal():
        try:
            float(parameter)
            return True
        except ValueError:
            return False
    else:
        return False

  def is_num(self, s):
    return s.replace('.', '').isnumeric()

  def toi(self, parameter):
    if parameter.isdecimal():  
      return int(parameter)
    else:
      return int(float(parameter))


  def myAtoi(self, st: str) -> int:
    # 一つ以上のwhitespaceで区切る
    st_list = st.split()

    if len(st_list) == 0:
      return 0

    if st_list[0] == "":
      st_list.pop(0)
    
    target = st_list[0]

    op_num = 1
    # 一文字目が+または-なら、それで正負を決定する
    if target[0] == '+' or target[0] == '-':
      op_num = -1 if target[0] == '-' else 1
      target = target[1:]
    print(op_num)
    
    # 数字である最長インデックスを取得
    t_f_list = [True if t.isnumeric() else False for t in target]
    print(t_f_list)
    if all(t_f_list):
      num_index = len(t_f_list)
    else:  
      num_index = t_f_list.index(False)
    print(num_index)
    if num_index <= 0:
      val = 0
    else:
      val = self.toi(target[0:num_index])
    
    val = val * op_num

    # 数字が2**31bitの範囲なのかをチェック
    if val > MAX_BIT:
      val = MAX_BIT

    if val < MIN_BIT:
      val = MIN_BIT

    return val

string = "words and 987"
sol = Solution()
print(sol.myAtoi(string))