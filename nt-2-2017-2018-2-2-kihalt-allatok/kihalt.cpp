#include <iostream>

using namespace std;

int main()
{
    int M, N;
    cin >> M >> N;
    int elt[M] = {0};
    int r, u;
    for(int i=0; i<N; ++i) {
        cin >> r >> u;
        for(int j=u; j<=r; ++j) {
            ++elt[j];
        }
    }
    // maximum es index-kereses hatulrol
    int m = elt[M-1];
    int ind = M-1;
    for (int i=M-1; i>0; --i) {
        if (elt[i] > m){
            m = elt[i];
            ind = i;
        }
    }
    cout << m << endl << ind;
    return 0;
}
