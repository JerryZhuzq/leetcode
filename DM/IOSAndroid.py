'''
Given a set of (IOS and Android) mobile devices and a number of push notifications to send each of them, generate an
ordering of send events such that the events are distributed fairly and as fast as possible.

Input: The input is a string in the format of repeating ids and respective notification counts with no spaces.

ID format: A device id is composed of a random combination of alphanumeric characters.
- Android ids are 4 characters long and start with the letter A
- IOS ids are 3 characters long and start with the letter I

You can assume input will always be valid and counts will always be non-negative. However it worth noting A and I can
appears in device IDs, and device IDs can repeat multiple times.

Ids can appear more than once in the same input. In that case, take the sum of their counts.
Sample in/out:
IA32Aab74Apq22IA31
Aab7IA3Apq2Aab7IA3Apq2Aab7IA3Aab7

'''
from collections import defaultdict
from heapq import *

def process_notifications(input):

    if not input:
        return ""

    device = defaultdict(int)

    i = 0
    while i < len(input):
        if input[i] == 'I':
            device[input[i:i+3]] += int(input[i+3])
            i += 4
        elif input[i] == 'A':
            device[input[i:i + 4]] += int(input[i + 4])
            i += 5

    hp = []
    for d in device:
        hp.append((0, -device[d], d))

    heapify(hp)

    res = ''
    while hp:
        fre, time, id = heappop(hp)
        res += id
        if time < -1:
            heappush(hp, (fre+1, time+1, id))
    return res

print(process_notifications('IA32Aab74Apq22IA31'))









