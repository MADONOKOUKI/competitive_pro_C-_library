//巡回セールスマン問題
//グラフが与えられた時、すべての頂点を一度ずつ通る巡回路では、経路長が最短のものを求めるもの
//この問題はNP完全であることが知られているので多項式時間の解法は期待できない
//単純にすべての経路を試すアルゴリズムはO(V!)程度の計算量がかかるが、
//動的計画法に基づくアルゴリズムではO（V2^V)程度の計算量に軽減できる
//X[j][S+{j}] = E[j][i] + X[i][S]
//ここでX[i][S]は始点からiに至るSのすべての頂点を通る最小重み巡回路である
//状態Sをビットで管理することによってプログラムが簡潔になる。



void rec(vector<vector<int> >& E, int s,vector<int>& path){
  if (S != 0) rec(Y,Y[i][S],S&~(1<<i),result);
  path.push_back(i);
} 

int TSP(vector< vector<int> >& E, int s, vector<int>& result){
  const int n = E.size();
  N = 1 << n;
  vector < vector < int > > X(n,vector<int>(N,inf));
  vector < vector < int > > Y(n,vector<int>(N,-1));
  for(int i = 0; i < n; i++){
    X[i][1<<i] = E[s][i];
    Y[i][1<<i] = s;
  }

  for(int S = 1; S < N; S++){
    for(int i = 0; i < n; ++i){
      if(!(S&(1<<i))) continue;
      for(int j = 0; j < n; ++j){
        if(X[j][S|(1<<j)] > X[i][S] + E[i][j]){
          X[j][S|(1<<j)] = X[i][S] + E[i][j];
          Y[j][S|(1<<j)] = i;
        }
      }
    }
  }
  result.clear();
  rec(Y,s,(1<<n)-1,result);
  return X[s].back();
}