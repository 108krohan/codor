"""
The task can be done by brute force solution. You can easily prove that
it is never needed to remove more than two bags
so the sum of apples in the rest of bags would be
divisible by 3. So we have three options:
don't remove anything, remove one bag,
or remove two bags; then sell everything left.
This can be simply brute forced by trying to
remove every possible combination of bags (zero, one, or two).
Maximum number of combinations is O(n2),
which is the time complexity of solution.
"""
####my solution in python :


###include <cstdio>
###include <algorithm>
##
##using namespace std;
##
##const int N = 1010;
##int n, s, m, a[N];
##
##int main()
##{
##    scanf("%d", &n);
##    for (int i = 1; i <= n; i++) scanf("%d", &a[i]), s += a[i];
##    if (!(s % 3)) m = s;
##    for (int i = 1; i <= n; i++) if (!((s - a[i]) % 3)) m = max(m, s - a[i]);
##    for (int i = 1; i < n; i++)
##        for (int j = i + 1; j <= n; j++) if (!((s - a[i] - a[j]) % 3)) m = max(m, s - a[i] - a[j]);
##    printf("%d", m);
##    return 0;
##}


###include <cmath>
###include <cstdio>
###include <vector>
###include <iostream>
###include <algorithm>
##using namespace std;
##
##
##int main() {
##    int n;
##    int a[1002];
##    cin>>n;
##    for(int i=0;i<n;i++)
##    {
##        cin>>a[i];
##    }
##    sort(a,a+n);
##    int ans=0;
##    vector<int>v1,v2;
##    for(int i=0;i<n;i++)
##    {
##        ans+=a[i];
##        if(a[i]%3==1)v1.push_back(a[i]);
##        if(a[i]%3==2)v2.push_back(a[i]);
##    }
##    if(ans%3==1)
##    {
##        int baad=1<<28;
##        if(v1.size())baad=v1[0];
##        if(v2.size()>=2)baad=min(baad,v2[0]+v2[1]);
##        ans-=baad;
##    }
##    else if(ans%3==2)
##    {
##        int baad=1<<28;
##        if(v2.size())baad=v2[0];
##        if(v1.size()>=2)baad=min(baad,v1[0]+v1[1]);
##        ans-=baad;
##    }
##    cout<<ans<<endl;
##    return 0;
##}





