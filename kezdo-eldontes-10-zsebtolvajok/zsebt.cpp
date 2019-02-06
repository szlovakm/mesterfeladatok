#include <iostream>

using namespace std;

class zsebtolvaj
{
public:
    int mag;
    string szem;
    string haj;
    int bunt;
};
bool fgv (zsebtolvaj zsebi, zsebtolvaj zsebes)
{
    int has=0;
    has+=(zsebi.mag==zsebes.mag)?1:0;
    has+=(zsebi.szem==zsebes.szem)?1:0;
    has+=(zsebi.haj==zsebes.haj)?1:0;
    has+=(zsebi.bunt==zsebes.bunt)?1:0;
    return(has>=2);
}
int main()
{
    int N;
    cin >> N;
    zsebtolvaj tomb [N];
    for (int i = 0; i < N; ++i)
    {
        cin >> tomb[i].mag >> tomb[i].szem >> tomb[i].haj >> tomb[i].bunt;
    }

    bool egyezik=false;
    for (int i=0; (i<N-1 && !egyezik); i++)
        {
        for (int j=i+1; (j<N && !egyezik); j++)
            {
            egyezik=fgv(tomb[i],tomb[j]);
            }
        }
    if (egyezik) cout <<"IGEN" << endl;
        else cout <<"NEM" << endl;
    return 0;

}
