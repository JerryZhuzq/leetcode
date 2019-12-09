def maxHeight(tablePositions, tableHeights):
    # Write your code here
    if len(tablePositions) == 1:
        return 0

    maxh = 0

    for i in range(1, len(tableHeights)):
        if tablePositions[i] - tablePositions[i-1] > 1:
            roof = max(tableHeights[i-1],tableHeights[i])
            root = min(tableHeights[i-1],tableHeights[i])
            gap = tablePositions[i] - tablePositions[i-1] - 1
            if roof - root + 1 >= gap:
                maxh = max(maxh, root + gap)
            else:
                maxh = max(maxh, roof + round((gap - (roof - root)) / 2))

    return maxh
