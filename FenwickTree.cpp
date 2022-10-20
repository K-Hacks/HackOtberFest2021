#include<iostream>
#include<vector>

using namespace std;

class FenwickTree {
    private:
        //int *binaryIndexedTree
        int *tree;
        int tree_size;

        /*
         * To get next
         * 1) 2's complement of get minus of index
         * 2) AND this with index
         * 3) Add it to index
         */
        int getNext(int index) {
            return index + (index & (-index) );
        }

        /*
         * To get parent
         * 1) 2's complement to get minus of index
         * 2) AND this with index
         * 3) Subtract that from index
         */
        int getParent(int index) {
            return index - (index & (-index));
        }


        void updateBinaryIndexedTree(int val,int index) {
            while(index < tree_size) {
                tree[index] += val;
                index = getNext(index);
            }
        }

    public:

        // constructor------------------
        FenwickTree(int *arr, int n) {
            tree = new int[n+1]{0};
            tree_size = n;

            for(int i=1; i<=n; ++i) {
                updateBinaryIndexedTree(arr[i-1],i);
            }
        }




        void updateTree(int *arr, int newval, int index) {
            updateBinaryIndexedTree(newval-arr[index],index+1);
            arr[index] = newval;
        }

        // this returns the sum from 0th index to given index.
        int getSum(int index) {
            index++; // since index starts from 1 for the tree. And 0 is considered as root of the tree.
            int ans = 0;
            while(index>0) {
                ans += tree[index];
                index = getParent(index);
            }
            return ans;
        }


};

int main() {

    int input_arr[] = {1,2,3,4,5,6,7};
    FenwickTree mytree(input_arr, 7);
    cout<<mytree.getSum(2)<<"\n";
    mytree.updateTree(input_arr,5,2);
    cout<<mytree.getSum(2)<<"\n";

    return 0;
}
/*

*/


