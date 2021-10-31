#include<iostream>
using namespace std;
int main(){
	int n,m,i,j,k;
	cout<<"Enter number of processes: ";
	cin>>n;
	cout<<"\nEnter number of resources: ";
	cin>>m;
	int max[n][m],alloc[n][m],avail[m],need[n][m],ans[n],ind=0,f[n];
	int id,p[m];
	for(k=0;k<n;k++)
	    f[k]=0;
	for(i=0;i<n;i++){
		cout<<"\nEnter details for P"<<i;
		cout<<"\nEnter allocation: ";
		for(j=0;j<m;j++){
			cin>>alloc[i][j];
		}
		cout<<"Enter max: ";
		for(j=0;j<m;j++){
			cin>>max[i][j];
		}
	}
	cout<<"\nEnter available resource: ";
	for(i=0;i<m;i++)
		cin>>avail[i];
	for(i=0;i<n;i++){
		for(j=0;j<m;j++)
			need[i][j]=max[i][j]-alloc[i][j];
	}
	cout<<"\nEnter new request details";
	cout<<"\nEnter process id: ";
	cin>>id;
	cout<<"\nEnter request for resources: ";
	for(i=0;i<m;i++){
		cin>>p[i];
		if(p[i]<=need[id][i]){
			if(p[i]<=avail[i]){
				avail[i]=avail[i]-p[i];
				alloc[id][i]=alloc[id][i]+p[i];
				need[id][i]=need[id][i]-p[i];
			}
		}
	}
	for(k=0;k<n;k++){
		for(i=0;i<n;i++){
			if(f[i]==0){
				int flag=0;
				for(j=0;j<m;j++){
					if(need[i][j]>avail[j]){
						flag=1;
						break;
					}
				}
				if(flag==0){
					ans[ind++]=i;
					cout<<"\nP"<<i<<" is visited  ";
					for(int y=0;y<m;y++){
						avail[y]+=alloc[i][y];
						cout<<avail[y]<<" ";
					}
					f[i]=1;
				}
			}
		}
	}
	cout<<"\nThe Safe Sequence is ";
	for(i=0;i<n-1;i++)
	    cout<<"P"<<ans[i]<<" ";
	cout<<"P"<<ans[n-1]<<"\n";
	cout<<"\nProcess\tAllocation\tMax\tNeed\n";
	for(i=0;i<n;i++){
	    cout<<"P"<<i<<"\t";
		for(j=0;j<m;j++)
			cout<<alloc[i][j]<<" ";
		cout<<"\t\t";
		for(j=0;j<m;j++)
		    cout<<max[i][j]<<" ";
		cout<<"\t";
		for(j=0;j<m;j++)
		    cout<<need[i][j]<<" ";
		cout<<"\n";
	}
	return 0;
}