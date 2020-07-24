#include<bits/stdc++.h>
using namespace std;
#define SZ 200005
 
int n, m, k, x;
int L[SZ]; //level-array
vector<int> adj[SZ]; 
int jump[21][SZ];
 
void dfs(int u, int p, int l) {
    jump[0][u] = p;
    L[u] = l;
	
	for (int v: adj[u]) 
		if(v != p) 
		dfs(v, u, l+1);
}
 
void preprocess_LCA() {	
	dfs(1, -1, 0);
		
	for (int i = 1; 1<<i <= n ; i++) 
	for (int j = 0; j <= n ; j++)
	jump[i][j] = jump[i-1][jump[i-1][j]];
}
 
int LCA(int p,int q) {
	if(L[p] < L[q])
	swap(p, q);
	
	int diff = L[p] - L[q];
	
	for(int i = 20; i >= 0; i--) 
		if(diff & (1<<i)) 
		p = jump[i][p];
		
	if(p == q) return p;
 
	for (int i = 20; i >= 0; i--) {
		if (jump[i][p] != jump[i][q]) {
			p = jump[i][p];
			q = jump[i][q];
		}
	}
	return jump[0][p];
}
 
int main() {
	int u, v, q, a, b;
	cin >> n >> q;
	for(int i = 0; i < n-1; i++) {
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	preprocess_LCA();
 
	while(q--) {
		cin >> a >> b;
		int lca = LCA(a,b);
		cout << L[a] + L[b] - 2*L[lca] << endl;
	}
}