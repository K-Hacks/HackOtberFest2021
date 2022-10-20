#include <iostream>
using namespace std;
void main()
{
	char name[10];
	char reg_no[10];
	cout <<"Enter name:\n";
	gets(name);
	cout<<"Enter Register No.:\n";
	gets(reg_no);
	cout<<"Name:\t";
	puts(name);
	cout<<"\nRegister No.:\t";
	puts(reg_no);
}
