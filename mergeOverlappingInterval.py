def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x:x[0])
    mergedInterval = []
    currentInterval = sortedIntervals[0]
    mergedInterval.append(currentInterval)
    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart , nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd,nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedInterval.append(currentInterval)
    return mergedInterval

print(mergeOverlappingIntervals([
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]))