#include <iostream>
using namespace std;

void merge(int arr[], int left, int mid_point, int right){
	
}

void merge_sort(int arr[], int left, int right){
	if ((right-left)<=1){
		return;
	}
	int mid_point = left + (left+right)/2;
	merge_sort(arr,left,mid_point);
	merge_sort(arr,mid_point+1,right);
	merge(arr,left,mid_point,right);
}

int main(){
	int n;
	cin>>n;

	int arr[n];
	for (int i=0; i<n; i++){
		cin>>arr[i];
	}
	merge_sort(arr, 0, n-1);
	for (int j=0; j<n; j++){
		cout<<arr[j];
	}
	return 0;
}
