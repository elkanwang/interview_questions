#include <iostream>
using namespace std;

int partition(int arr[], int left, int right) {
	int p = left;
	int pivot = arr[left];
	for (int i=left+1; i<=right; i++){
		if(arr[i] < pivot){
			arr[p] = arr[i];
			arr[i] = arr[p+1];
			arr[p+1] = pivot;
			p++;
		}
	}
	return p;
}

void quick_sort(int arr[], int left, int right) {
	if(left>right) return;
	int p = partition(arr, left, right);
	quick_sort(arr,left, p-1);
	quick_sort(arr,p+1, right);
}


int main(){
	int n;
	cin>>n;

	int arr[n];
	for (int i=0; i<n; i++){
		cin>>arr[i];
	}
	quick_sort(arr, 0, n-1);
	for (int j=0; j<n; j++){
		cout<<arr[j];
	}
	return 0;
}
