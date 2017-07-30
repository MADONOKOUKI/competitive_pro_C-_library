#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
/*
//#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
*/

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
/*
//#if __cplusplus >= 201103L
#include <array>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
*/
using namespace std;
#define fi first
#define se second
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb(s) push_back(s)
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define mp(a,b) make_pair(a,b)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl

#define uni(x) x.erase(unique(all(x)),x.end())
template<class T,class U>inline void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>inline void chmax(T &t,U f){if(t<f)t=f;}
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) > (b) ? (b) : (a))

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;
typedef pair<P, int> PPI;

#define INF INT_MAX/3
#define MAX_N 1000
#define M_INF 1000000000
int n,m,v,i,k;

long long int extgcd(long long int a,long long int b,long long int &x,long long int &y) {
    long long int g = a;
    if (b) {
        g = extgcd(b, a % b, y, x);
        y -= x * (a / b);
    } else {
        x = 1;
        y = 0;
    }
    return g;
}

long long int inverse(long long int a,long long int p){
    long long int x,y;
    extgcd(a,p,x,y);
    return(x+p)%p;
}
 
int MAX_N = 100001;
 
long long int factorial[100001+1];
//階乗
//factorial をメイン関数内で初期化
void set_fact(int a,int p){
    long long int ans=1;
    factorial[0]=1;
    for(int i=1;i<=a;i++){
        ans=(ans*i%p+p)%p;
        factorial[i]=ans;
    }
}
 
//nCk mod p
//
long long int combination(int n,int k,int p){
    //set_factを呼んでから
    return factorial[n]*(inverse(factorial[k]*factorial[n-k]%p,p))%p;
}

int main(){
    int n;
    cin>>n;
    int a[n+1];
    //一度入れたかどうかを確認する
    bool used[n+1];
    fill_n(used,n+1,false);
    int M,N;
    reps(i,n+1){
        cin>>a[i];
        if(!used[a[i]]){
            used[a[i]]=true;
        }else{
            M=n-i;
            REP(j,i){
                if(a[j]==a[i]){
                    N=j;
                }
            }
        }
    }
    
    int p=INF;
    fill_n(factorial,MAX_N+1,0);
    set_fact(n+1,p);
 
    repl(i,1,n+2){
        if(i-1<=N+M){
            cout<<(combination(n+1,i,p)-combination(N+M,i-1,p)+p)%p<<endl;
        }else{
            cout<<combination(n+1,i,p)<<endl;
        }
 
    }
 
 
    return 0;
}