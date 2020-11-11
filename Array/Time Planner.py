def meeting_planner(slotsA, slotsB, dur):
    l_a, l_b = 0, 0

    while l_a < len(slotsA) and l_b < len(slotsB):
        sa, ea = slotsA[l_a]
        sb, eb = slotsB[l_b]
        cur_dur = max(sa, sb) + dur
        if cur_dur <= min(ea, eb):
            return [max(sa, sb), max(sa, sb) + dur]
        else:
            if ea <= eb:
                l_a += 1
            else:
                l_b += 1
    return []


print(meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))



def meeting_planner(a, b, dur):
  i = j = 0
  while i < len(a) and j < len(b):
    if min(a[i][1], b[j][1]) - max(a[i][0], b[j][0]) >= dur:
      return [max(a[i][0], b[j][0]), max(a[i][0], b[j][0])+dur]
    if a[i][1] < b[j][1]:
      i += 1
    else:
      j += 1
  return []


print(meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))