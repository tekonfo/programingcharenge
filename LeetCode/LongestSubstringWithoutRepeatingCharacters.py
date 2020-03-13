class Solution:
  """
  最長から検索を初めてウィンドウサイズを狭めていく
  文字が重複しない部分文字列が出てきたらそれが答え
  """
  # def lengthOfLongestSubstring(self, s: str) -> int:
  #   if s == "":
  #     return 0
  #   # 最長→1まで
  #   for length in reversed(range(1, len(s)+1)):
  #     for i in range(len(s) - length + 1):
  #       sub_str = s[i:i+length]
  #       # setに変換して、長さが変化しないかをチェックする
  #       if len(sub_str) == len(set(list(sub_str))):
  #         return length
  def lengthOfLongestSubstring(self, s: str) -> int:
    if s == "":
      return 0
    # 最長→1まで
    length = len(s)
    ans = 0
    start = 0
    end = 0
    # 文字達が重複無しで入っていく
    hash_set = set()

    while start < length and end < length:
      if s[end] not in hash_set:
        # 追加
        hash_set.add(s[end])
        end += 1
        ans = max(ans, len(hash_set))
      else:
        # 削除
        hash_set.remove(s[start])
        start += 1
    
    return ans

sol = Solution()
all_str = "pwwkew"
print(sol.lengthOfLongestSubstring(all_str))