

n, m, l = map(int, raw_input().split())
bottom_left = [map(int, raw_input().split()) for i in range(n)]
point = [map(int, raw_input().split()) for i in range(m)]
num_pts = 0
for pt in point :
    num_pt = 0
    for sq in bottom_left :
        if sq[0] <= pt[0] <= sq[0] + l \
           and sq[1] <= pt[1] <= sq[1] + l :
            num_pt += 1
    num_pts = max(num_pt, num_pts)
print num_pts
