def deletion_distance(str1, str2):
  if len(str1) > len(str2):
    str1, str2 = str2, str1
  l, r = len(str1), len(str2)
  dp = [0] * l
  if r == 0:
    return 0
  if l == 0:
    return r
  for i in range(r):
    previous = 0
    for j in range(l):
      if str1[j] == str2[i]:
        dp[j], previous = previous + 1, dp[j]
      else:
        previous = dp[j]
        dp[j] = max(dp[j], dp[j-1]) if j > 0 else dp[j]
  return l + r - 2*dp[-1]


def deletion_distance(str1, str2):
  l1, l2 = len(str1), len(str2)
  if l1 == 0:
    return l2
  if l2 == 0:
    return l1

  dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
  for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
      if str1[i - 1] == str2[j - 1]:
        dp[j][i] = dp[j - 1][i - 1] + 1
      else:
        dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
  return l1 + l2 - 2 * dp[-1][-1]


print(deletion_distance("some", "thing"))
