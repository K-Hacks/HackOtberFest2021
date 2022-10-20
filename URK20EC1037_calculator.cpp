#include <iostream>
using namespace std;
int main ()
{
    cout<<"My Name is NOEL GEORGE.\nMy Reg.No. is URK20EC1037.\n";
    int choice,a,b;
    char op;
    do{
    choice=0;
    cout<<"Choose the operation to be done:\n";
    cout<<"1.Add\n";
    cout<<"2.Subtract\n";
    cout<<"3.Multiply\n";
    cout<<"4.Divide\n";
    cout<<"Press:\n";
    cin>>choice;
    system("cls");
    switch(choice)
        {
      case 1:
             cout<<"Enter a First Number:\n";
             cin>>a;
             cout<<"Enter a Second Number:\n";
             cin>>b;
             cout<<"The addition of "<<a<<" and "<<b<<" is "<<a+b<<".\n";
             break;
      case 2:
             cout<<"Enter a First Number:\n";
             cin>>a;
             cout<<"Enter a Second Number:\n";
             cin>>b;
             cout<<"The subtraction of "<<a<<" and "<<b<<" is "<<a-b<<".\n";
             break;
      case 3:
             cout<<"Enter a First Number:\n";
             cin>>a;
             cout<<"Enter a Second Number:\n";
             cin>>b;
             cout<<"The product of "<<a<<" and "<<b<<" is "<<a*b<<".\n";
             break;
      case 4:
             cout<<"Enter a First Number:\n";
             cin>>a;
             cout<<"Enter a Second Number:\n";
             cin>>b;
             cout<<"The quotient of "<<a<<" and "<<b<<" is "<<a/b<<".\n";
             break;
      default:
             cout<<"ERROR\n";
        }
        cout<<"Do you want to continue (Y/N): ";
        cin>>op;
        }while (op=='y'||op=='Y');

}
