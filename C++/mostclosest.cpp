//最近点対
//嘘平行走査アルゴリズム
//正しい平面走査アルゴリズムを書いたほうが速度が向上しなかったのでこっちを作成
//O(nlogn) 点が縦一列に並んでいる場合最悪(n^2)



pair <P,P> closestPair(vector<P> p){
  int n=p.size(),s = 0,t = 1,m = 2,S[n],S[0] = 0,S[i] = 1;
  sort(ALL(p)) //"p < q" <=> "p.x < q.x";
  double d = norm(p[s]-p[t]);
  for (int i = 2; i < n; S[m++] = i++)REP(j,m){
    if(norm(p[S[j]]-p[i]) < d ) d = norm(p[s = S[j]] - p[t = i]);
    if(real(p[S[j]]) < real(p[i] - d)) S[j--] = S[--m];
  }
  return make_pair(p[s],p[t]);
}