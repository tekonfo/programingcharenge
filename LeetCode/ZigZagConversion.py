class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s

    count = 0
    arr = []
    while s is not "":
      tmp = []
      pat = count % (numRows - 1)
      if pat == 0:
        tmp = list(s[:numRows])
        s = s[numRows:]
      else:
        tmp = ["" for _ in range(numRows - 1)]
        tmp.insert(numRows - pat - 1, s[0])
        s = s[1:]
      
      if len(tmp) is not numRows:
        for t in range(numRows - len(tmp)):
          tmp.append("")
        
      arr.append(tmp)
      count += 1

    rets = ''
    for i in range(numRows):
      tmp = ''.join([a[i] for a in arr])
      rets += tmp
    
    return rets

word = "A"
row_num = 1
sol = Solution()
print(sol.convert(word, row_num))