#include <iostream>
using namespace std;

void bubble_sort(int arr[], int len) {
	for (int i= 0; i<len; i++) {
		for (int j = i+1; j<len; j++) {
			if(arr[j]<arr[i]){
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
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
	bubble_sort(arr, i);
	return 0;
}


