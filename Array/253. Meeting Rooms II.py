class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time, end_time = [], []
        for s, e in intervals:
            start_time.append(s)
            end_time.append(e)
        start_time.sort()
        end_time.sort()

        total_room, ava_room = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start_time[s] < end_time[e]:
                if ava_room == 0:
                    total_room += 1
                else:
                    ava_room -= 1
                s += 1
            else:
                e += 1
                ava_room += 1
        return total_room
