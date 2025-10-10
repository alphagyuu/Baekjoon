def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0  # 이 위치까지 남은 배달 상자 수(누적)
    p = 0  # 이 위치까지 남은 수거 상자 수(누적)

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        # 이 위치까지 처리하려면 cap짜리 트럭이 몇 번 다녀와야 하는가?
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2  # 왕복 거리
    return answer
