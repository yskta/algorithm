#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int maxBits = 0;
    long long bestI = 0, bestJ = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            long long product = a[i] * a[j];
            int bits = __builtin_popcountll(product);
            
            if (bits > maxBits) {
                maxBits = bits;
                bestI = a[i];
                bestJ = a[j];
            }
        }
    }
    
    cout << maxBits << "\n";
    cout << bestI << " " << bestJ << "\n";
    
    return 0;
}