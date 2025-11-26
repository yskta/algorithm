#include <bits/stdc++.h>
using namespace std;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<long long> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }
    
    sort(coins.begin(), coins.end());
    
    long long reachable = 0;
    
    for (int i = 0; i < n; i++) {
        if (coins[i] > reachable + 1) {
            break;
        }
        reachable += coins[i];
    }
    
    cout << reachable + 1 << endl;
    
    return 0;
}