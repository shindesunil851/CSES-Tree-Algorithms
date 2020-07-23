#include<bits/stdc++.h>
using namespace std;
 
const int mxN = 2e5;
vector<int>adj[mxN];
int dp0[mxN], dp1[mxN];
 
void dfs(int u, int pu) {
	for (auto v : adj[u] ) {
		if (v == pu)continue;
		dfs(v, u);
		dp1[u] = max(dp1[u] + max(dp0[v], dp1[v]), 1 + dp0[u] + dp0[v]);
		dp0[u] += max(dp0[v], dp1[v]);
	}
}
 
 
int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
 
	int n;
	cin >> n;
	for (int i = 1, a, b; i < n; i++) {
		cin >> a >> b; a--, b--;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
 
	dfs(0, -1);
 
	cout << max(dp0[0], dp1[0]) << '\n';
 
	return 0;
}