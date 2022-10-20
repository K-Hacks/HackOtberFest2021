#include <iostream>
using namespace std;
int main()
{
    int no,on=0;
    cout<<"Enter A Number:\n";
    cin>>no;
    while(no>0)
    {
        on=on*10+no%10;
        no=no/10;
    }
    cout<<"Output:"<<on;
}
