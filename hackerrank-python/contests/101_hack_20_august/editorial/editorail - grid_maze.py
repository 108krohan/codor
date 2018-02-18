"""
Let's denote the maze border as B. Cost to move to a cell containing wall is one and cost to move to an empty cell is zero.

Now look at the optimal S−P−B path. First, we destroyed some walls to get from S to P. We want to get to B not necessarily from P but from any cell in path S−P, because every cell on this path is empty and we can move through the path without making extra cost. On this path there must exist some "crossing cell" (let's denote it as C) that is optimal to move from it to some cell located at B.

Now, what is the solution? When the cell C is found, the solution is equal to cost(S,C)+cost(P,C)+cost(B,C), where cost(x,y) denotes the cost of moving from x to y (be careful, it is important whether the cell C is containing a wall or not). Each of cost values can be easily calculated using Dijkstra algorithm by starting Dijkstra from S, P, and B (put all the cells of B in Dijkstra priority queue). Total time complexity is O(nmlognm). 

"""

####Problem setter's code /djikstra algorithm
###include <cstdio>
###include <queue>
###include <vector>
##
##using namespace std;
##
##typedef pair<int, int> ii;
##
##const int N = 1010, D = 1000010;
##int n, m, ss, sp, ans = D, d[3][D];
##char s[N][N];
##bool f[D];
##vector<ii> v[D];
##
##void dijkstra(int be, int* d)
##{
##    priority_queue<ii> q;
##    fill(f, f + n * m + 1, 0);
##    q.push({0, be});
##    while (!q.empty())
##    {
##        int di = q.top().first, c = q.top().second; q.pop();
##        if (f[c]) continue;
##        f[c] = true; d[c] = -di;
##        for (auto i : v[c]) q.push({di - i.second, i.first});
##    }
##}
##
##int main()
##{
##    scanf("%d %d", &n, &m);
##    for (int i = 1; i <= n; i++) scanf("%s", s[i] + 1);
##    for (int i = 1, k = 1; i <= n; i++)
##        for (int j = 1; j <= m; j++, k++)
##        {
##            ii pa = {k, s[i][j] == '#'};
##            if (i > 1) v[k - m].push_back(pa); else
##            if (!f[k]) v[0].push_back(pa), f[k] = true;
##            if (i < n) v[k + m].push_back(pa); else
##            if (!f[k]) v[0].push_back(pa), f[k] = true;
##            if (j > 1) v[k - 1].push_back(pa); else
##            if (!f[k]) v[0].push_back(pa), f[k] = true;
##            if (j < m) v[k + 1].push_back(pa); else
##            if (!f[k]) v[0].push_back(pa), f[k] = true;
##            if (s[i][j] == 'S') ss = k;
##            if (s[i][j] == 'P') sp = k;
##        }
##    dijkstra(0, d[0]);
##    dijkstra(ss, d[1]);
##    dijkstra(sp, d[2]);
##    for (int i = 1, k = 1; i <= n; i++)
##        for (int j = 1; j <= m; j++, k++)
##        {
##            int ke = d[0][k] + d[1][k] + d[2][k];
##            if (s[i][j] == '#') ke -= 2;
##            ans = min(ans, ke);
##        }
##    printf("%d", ans);
##    return 0;
##}
