#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, M, x;
    cin >> N >> M;

    // olvashatobb definialasa egy 2-dim vektornak:
    typedef vector<int> sor;
    typedef vector<sor> matrix;
    matrix madarak(N, sor(M));

    // tomorebb definialas
    // vector<vector<int> > madarak(N, vector<int>(M));

    // adatok feltoltese
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> x;
            madarak[i][j] = x;
        }
    }

    // szamolas
    int db = 0;
    for (int j=0; j<M; j++) {
        int oszlop = 0;
        for (int i=0; i<N; i++) {
            if (madarak[i][j] > 0) {
                oszlop++;
            }
        }
        if (oszlop >= 0.9*(double)N) {
            db++;
        }
    }
    cout << db;
    return 0;
}
