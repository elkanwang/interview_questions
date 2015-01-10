#include <iostream>
using namespace std;

void selection_sort(int arr[], int len) {
	for (int i= 0; i<len; i++) {
		int min_index = i;
		for (int j = i+1; j<len; j++) {
			if(arr[j] < arr[min_index]){
				min_index = j;
			}
		}
		if(min_index != i){
			int temp = arr[i];
			arr[i] = arr[min_index];
			arr[min_index] = temp;
		}
	}
	for (int i=0; i<len; i++){
		cout<<arr[i]<<endl;
	}
}


int main(){
	int arr[100];
	int i = 0;
	while(cin) {
		cin >> arr[i];
		i++;
	}
	selection_sort(arr, i);
	return 0;
}


