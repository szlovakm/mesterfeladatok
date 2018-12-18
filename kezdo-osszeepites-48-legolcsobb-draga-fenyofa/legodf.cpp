#include <iostream>

using namespace std;

int main()
{
    int N, ar, uj;
    cin >> N >> ar;
    int ind = 0;
    int leg = 10000;
    for(int i=0; i<N; ++i){
        cin >> uj;
        if (uj > ar && uj < leg) {
            ind = i;
            leg = uj;
        }
    }
    if (ind > 0) {
        cout << ind+1 << " " <<leg;
    } else {
        cout << -1;
    }
    return 0;
}
