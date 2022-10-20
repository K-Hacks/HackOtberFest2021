/* Program Statement
* Merge N arrays and print the final sorted array.
* 
* Input:
    3
    194 544 2 5
    67 32 22 1
    65 43 13 23
*
* Output:
    1 2 5 13 22 23 32 43 65 67 194 544
*/

#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    vector<int> a;
    vector<int>::iterator it;
    int e;
    
    while(t--) {
        while(cin >> e) {
            a.push_back(e);   
            
            sort(a.begin(), a.end());
            it = unique(a.begin(), a.end());
            a.resize(distance(a.begin(), it));
            
            if(cin.get() == '\n')
                break;
        }    
    }
    for(int i = 0; i < a.size(); i++) {
        cout << a.at(i) << " ";
    }    
    
    return 0;
}