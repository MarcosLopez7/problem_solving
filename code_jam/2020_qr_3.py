t = int(input())

for test_case in range(t):
    n = int(input())

    time_intervals = []

    for i in range(n):
        line = input().split()
        time_intervals.append({'start': int(line[0]), 'end': int(line[1]), 'index': i})

    calendar = sorted(time_intervals, key=lambda k: k['start']) 

    result = []
    start_c = 0
    end_c = 0
    start_j = 0
    end_j = 0

    for activity in calendar:
        if activity['start'] >= end_c:
            start_c = activity['start']
            end_c = activity['end']
            result.append({'p':'C', 'index': activity['index']})
        elif activity['start'] >= end_j:
            start_j = activity['start']
            end_j = activity['end']
            result.append({'p':'J', 'index': activity['index']})
        else:
            result = "IMPOSSIBLE"
            break
    
    if result != "IMPOSSIBLE":
        final_calendar = sorted(result, key=lambda k: k['index'])
        result = ""
        for act in final_calendar:
            result += act['p'] 

    print("Case #{}: {}".format(test_case + 1, result))
