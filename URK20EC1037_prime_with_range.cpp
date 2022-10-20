#include <iostream>
using namespace std;
int main()
{
    int numf,numl,flag,i,temp;
    cout<<"Enter first number of the range:\n";
    cin>>numf;
    cout<<"Enter last number of the range:\n";
    cin>>numl;
    cout<<"Prime Numbers:\n";
    for(temp=numf;temp<=numl;temp++)
    {flag=0;
     i=2;
     while(flag==0)
      {
       if(temp%i==0)
       {
         flag=1;
       }
       else
       {
        flag=0;
        i++;
       }
      }
      if(i==temp&&flag==1)
      {
        cout<<temp<<endl;
      }
    }
}
