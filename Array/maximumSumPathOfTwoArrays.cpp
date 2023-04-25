#include<iostream>
using namespace std;

// problem link: https://practice.geeksforgeeks.org/batch/Amazon-Test-Series/track/amazon-arrays/problem/max-sum-path-in-two-arrays

int max_path_sum(int A[], int B[], int n, int m)
    {
        int sum1=0,sum2=0,sum=0;

        int i=0,j=0;

        while(i<n&&j<m){

            if(A[i]==B[j]){
                sum+=max(sum1,sum2);
                sum+=A[i];
                i++;
                j++;
                sum1=0;sum2=0;

            }else if(A[i]<B[j]){

                sum1+=A[i++];
            }else{
                sum2+=B[j++];
            }

        }
        while(i<n){
        sum1+=A[i++];
        }

        while(j<m){
        sum2+=B[j++];
        }

        sum+=max(sum1,sum2);

        return sum;
    }

int main(){

    int n,m; 

    cin >> n >> m;

    int A[n], B[n];

    for(int i = 0; i < n; i++){
        cin >> A[i];
    }
    for(int i = 0; i < m; i++){
        cin >> B[i];
    }

    cout << max_path_sum(A,B,n,m) << endl; 




    return 0;
}