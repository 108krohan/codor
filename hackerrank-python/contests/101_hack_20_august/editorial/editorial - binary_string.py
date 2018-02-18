"""
This problem can be solved using greedy algorithm.
Iterating through string from begin to end,
every time when 0 is found, try to
swap it with the first next position
with same remainder modulo k which
contains 1. If such positions i and j are
found (si=0, sj=1), then exchange these values
if (j−i)/k≤t, and decrease t for (j−i)/k.
Implementation can be done with array of
queues - qi will contain all positions with remainder
i modulo k where si=1. Time complexity is O(n)
"""



####my solution in python


####problem setter's code
###include <cstdio>
###include <queue>
##
##using namespace std;
##
##const int N = 100010;
##int n, k, t;
##char s[N];
##queue<int> p[N];
##
##int main()
##{
##    scanf("%d %d %d %s", &n, &k, &t, s);
##    for (int i = 0; i < n; i++) if (s[i] == '1') p[i % k].push(i);
##    for (int i = 0; i < n; i++) if (s[i] == '1') p[i % k].pop(); else
##    if (!p[i % k].empty() && t >= (p[i % k].front() - i) / k)
##    {
##        swap(s[i], s[p[i % k].front()]);
##        t -= (p[i % k].front() - i) / k;
##        p[i % k].pop();
##    }
##    printf("%s", s);
##    return 0;
##}

####problem tester's code
##//Programming Contest Template
##//Shafaet Ashraf 
###include <algorithm>
###include <bitset>
###include <cctype>
###include <cmath>
###include <cstdio>
###include <cstdlib>
###include <cstring>
###include <ctime>
###include <deque>
###include <fstream>
###include <iostream>
###include <list>
###include <map>
###include <queue>
###include <set>
###include <sstream>
###include <stack>
###include <string>
###include <utility>
###include <vector>
###include <assert.h>
##
###define stream istringstream
###define rep(i,n) for(int i=0; i<(int)n; i++)
###define repv(i,n) for(int i=n-1; i>=0; i--)
###define repl(i,n) for(int i=1; i<=(int)n; i++)
###define replv(i,n) for(int i=n; i>=1; i--)
###define FOR(i,a,b) for(int i=(int)a;i<=(int)b;i++)
###define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
###define sz(x) (int)x.size()
###define inf (1061109567)
###define pb(x) push_back(x)
###define ppb pop_back
###define all(x) x.begin(),x.end()
###define mem(x,y) memset(x,y,sizeof(x));
###define eps 1e-9
###define rev reverse
###define pii pair<i64,i64>
###define pll pair<i64,i64>
###define pmp make_pair
###define sdi(x) scanf("%d",&x)
###define sdii(x,y) scanf("%d%d",&x,&y)
###define sds(x) scanf("%s",x)
###define pfi(x) printf("%d\n",x);
###define uu first
###define vv second
##using namespace std;
##template<class T> inline T sqr(T x){return x*x;}
##template<class T> inline T lcm(T a,T b) {if(a<0)return
##lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/__gcd(a,b));}
##template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }
##template<class T> string itoa(T a){if(!a) return "0";string ret;for(T i=a; i>0; i=i/10) ret.pb((i%10)+48);reverse(all(ret));return ret;}
##typedef  long long i64;
##typedef unsigned long long ui64;
##double log(double N,double B){  return (log10l(N))/(log10l(B)); }
##vector< string > token( string a, string b ) {const char *q = a.c_str();while( count( b.begin(), b.end(), *q ) ) q++;vector< string >
##    oot;while( *q ) {const char *e = q;while( *e && !count( b.begin(), b.end(), *e ) ) e++;oot.push_back( string( q, e ) );q = e;while( count( b.begin(),
##    b.end(), *q ) ) q++;}return oot;
##}
##//bool operator < ( const node& p ) const {      return w < p.w;   }
###define on(n,pos) (n | (1LL<<(pos)))
###define off(n,pos)  n & ~(1LL<<pos)
###define ison(n,pos) (bool)(n & (1LL<<(pos)))
##string toBin(int n){ string s; repv(i,10)s+=(ison(n,i)+'0');return s;}
##bool eq(long double a,long double b){return fabs(a-b)<eps;}
###define READ(f) freopen(f, "r", stdin)
###define WRITE(f) freopen(f, "w", stdout)
###define pks printf("Case %d: ",++ks);
##
##void ensure(int x,int b,int e)
##{
##    assert(x>=b);
##    assert(x<=e);
##}
##int main() {   
##
##  //READ("in");
##  //WRITE("out");
##  int n,k,t;
##  cin>>n>>k>>t;
##  ensure(n,1,100000);
##  ensure(k,1,n);
##  ensure(t,1,1000000000);
##  string s;
##  cin>>s;
##  ensure(sz(s),1,100000);
##
##  queue<int>q[100002];
##  for(int i=0;i<sz(s);i++)
##  {
##      if(s[i]=='1')
##      {
##          q[i%k].push(i);
##
##      }
##  }
##  for(int i=0;i<sz(s);i++)
##  {
##      if(s[i]=='0')
##      {
##          if(q[i%k].size()==0) continue;
##          int p=-1,found=0;
##          while(q[i%k].size())
##          {
##            p=q[i%k].front();
##            if(p>i) {found=1;break;}
##            q[i%k].pop();
##            //cout<<i<<">>>>"<<p<<endl;
##          }
##          if(found==0) continue;
##          int stp=p/k-i/k;
##          if(stp<=t)
##          {
##
##              t-=stp;
##              swap(s[i],s[p]);
##              q[i%k].pop();
##            //  cout<<i<<" "<<p<<" "<<s<<endl;  
##          }
##      }
##  }
##  cout<<s<<endl;
##}

