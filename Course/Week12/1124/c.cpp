#include <iostream>
using namespace std;

int main() {
    int n = 100000;
    cout << n << endl;
    for (int i = 0; i < n; i++) {
        if (i > 0) cout << " ";
        cout << (i + 1);
    }
    cout << endl;

    return 0;
}