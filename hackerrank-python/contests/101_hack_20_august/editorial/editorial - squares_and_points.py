"""
The square with bottom left corner T(xs,ys) and
side of length ls contains point P(xp,yp) if the following
conditions are fulfilled:

1.xs≤xp≤xs+ls

2.ys≤yp≤ys+ls

First sort all the squares and points by x coordinates.
Now for each point we can find set of squares which
satisfies the first condition. It must be contiguous
segment of squares in the sorted array,
so it can be iterated using two pointers.
The second condition is now equivalent to adding and removing
y coordinates and finding the number
of y coordinates located in some interval. 

Solve this using BIT (Fenwick Tree) with mapped
values of y coordinates because they are too large
to be stored in the array. Total time
complexity of this solution is O(nlogn).

"""

###my python code


##problem setter's solution

###include <cstdio>
###include <algorithm>
###include <map>
##
##using namespace std;
##
##const int N = 100010, K = 300010;
##int n, m, l, d, k, s, a[K], t[K];
##pair<int, int> p[N], q[N];
##map<int, int> ma;
##
##void upd(int i, int x)
##{
##    for (; i <= k; i += i & -i) t[i] += x;
##}
##
##int get(int i)
##{
##    int s = 0;
##    for (; i; i -= i & -i) s += t[i];
##    return s;
##}
##
##int main()
##{
##    scanf("%d %d %d", &n, &m, &l);
##    for (int i = 1; i <= n; i++) scanf("%d %d", &p[i].first, &p[i].second), a[++d] = p[i].second;
##    for (int i = 1; i <= m; i++) scanf("%d %d", &q[i].first, &q[i].second), a[++d] = q[i].second, a[++d] = q[i].second - l - 1;
##    sort(a + 1, a + d + 1);
##    ma[a[1]] = k = 1;
##    for (int i = 2; i <= d; i++) ma[a[i]] = a[i] != a[i - 1] ? ++k : k;
##    sort(p + 1, p + n + 1);
##    sort(q + 1, q + m + 1);
##    for (int i = 1, x = 1, y = 1; i <= m; i++)
##    {
##        while (x <= n && p[x].first <= q[i].first) upd(ma[p[x].second], 1), x++;
##        while (y <= n && p[y].first < q[i].first - l) upd(ma[p[y].second], -1), y++;
##        s = max(s, get(ma[q[i].second]) - get(ma[q[i].second - l - 1]));
##    }
##    printf("%d", s);
##    return 0;
##}
