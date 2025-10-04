# #include<bits/stdc++.h>

# using namespace std;

# int main(){
#   int n,q;
#   cin >> n >> q;
#   vector<int> pc(n+1,1);
#   pc[0]=0;
#   int o=1;
#   while(q--){
#     int x,y;
#     cin >> x >> y;
#     int res=0;
#     while(o<=x){
#       res+=pc[o];
#       pc[y]+=pc[o];
#       o++;
#     }
#     cout << res << "\n";
#   }
#   return 0;
# }


def c():
    N, Q = map(int, input().split())
    # 1~Nの配列
    versions = [i for i in range(1, N + 1)]
    for _ in range(Q):
        upgrade_count = 0
        X, Y = map(int, input().split())
        for i in range(len(versions)):
            if X >= versions[i]:
                versions[i] = Y
                upgrade_count += 1
        print(upgrade_count)

if __name__ == "__main__":
    c()