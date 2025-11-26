#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
using namespace __gnu_pbds;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(long long x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    long long x;
    cin >> n >> x;
    
    long long cnt = 0;
    long long ps = 0;
    gp_hash_table<long long, long long, custom_hash> mp;
    mp[0] = 1;
    
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        ps += a;
        cnt += mp[ps - x];
        mp[ps]++;
    }
    
    cout << cnt << "\n";
    
    return 0;
}