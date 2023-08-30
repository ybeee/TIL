# def solution(wallpaper):
#     answer = []
#     for w in wa
#     return answer

# wallp = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
# wallp = [".#...", "..#..", "...#."]
# ans = []
# for i, w in enumerate(wallp):
#     for j, v in enumerate(w):
#         if v == '#':
#             ans.append([i,j])
#         print(v)
# ld = [a[0] for a in ans]
# rd = [a[1] for a in ans]
# print(ans)
# answer = [min(ld), min(rd), max(ld)+1, max(rd)+1]
# print(ld, rd)
# print(answer)



left, right = 13, 17
answer=0 
buc=[]
for v in range(left, right+1):
    buc=[]
    for i in range(1,v+1):
        if v % i == 0:
            buc.append(i)
        # else:
            # buc.append(i)
    if len(buc)%2 == 0:
        print(buc)
        answer += v
    else:
        print(buc)
        answer -= v
print(answer)