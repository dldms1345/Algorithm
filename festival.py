T = int(input())
for _ in range(T):
    days, min_teams = map(int, input().split())
    day_costs = list(map(int, input().split()))
    
    min_avg = 987654321
    for i in range(days - min_teams + 1):
        cost_sum = sum(day_costs[i:i + min_teams])
        crr_team = min_teams
        if cost_sum / crr_team < min_avg:
            min_avg = cost_sum / crr_team
        for j in range(i+min_teams, days):
            cost_sum += day_costs[j]
            crr_team += 1
            if cost_sum / crr_team < min_avg:
                min_avg = cost_sum / crr_team
    print("%.11f" % min_avg)