def change_time(T,matrix):
    time = list(T.split(' '))
    h =  float(time[1][0:2]) * 3600
    m = float(time[1][3:5])*60
    s = float(time[1][6:])
    etime = h + m + s
    pt = float(time[2][:-1])
    stime = round(etime - pt + 0.001,3)
    matrix.append([stime,etime])
    return


def solution(lines):
    answer = 0
    matrix = []
    for i in range(len(lines)):
        change_time(lines[i],matrix)
    for i in range(len(matrix)):
        s,e = matrix[i][1],matrix[i][1] + 1
        cnt = 1
        for j in range(len(matrix)):
            if i != j and s <= matrix[j][0] < e:
                cnt += 1
            elif i != j and s <= matrix[j][1] < e:
                cnt += 1
            elif i != j and s >= matrix[j][0] and matrix[j][1] >= e:
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer


ex1 = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
ex2 = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
ex3 = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(ex1))