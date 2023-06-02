def mergeSubintervals(intervals):
    intervals.sort(key=lambda x: x[0])
    ans = []
    i = 0
    print(intervals) 
    for i in range(len(intervals)):
        if len(ans) <= 0 or ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        elif ans[-1][1] > intervals[i][0] :
            end = max(ans[-1][1],intervals[i][1])
            ans[-1][1] = end
            
    return ans



intervals=[[1,3],[2,6],[8,10],[15,18]]
print(mergeSubintervals(intervals=intervals))