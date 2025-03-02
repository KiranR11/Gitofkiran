package Sorting;

import java.util.Arrays;

/**
 * Why? its adaptive steps get reduced,no of swaps reduced as compared to bubble sort
 * used for smaller values of n works good when partial sorted array
 * 
 * starting with i = 0,j = i + 1 pass1 i will run 0 to n - 2(length)
 * when element j is not smaller than element j-1 break the loop
 * i will be n - 2
 */
public class InsertionSort {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {3, 1, 5, 4, 2};
		insertionSort(arr);
		System.out.println(Arrays.toString(arr));
	}
	
	static void insertionSort(int[] arr) {
		for(int i=0; i < arr.length - 1; i++) {
			for(int j =i+1; j > 0;j-- ) {
				if(arr[j] < arr[j-1]) {
					swap(arr, j , j-1);
				}else {
					break;
				}
			}
		}
	}
	
	static void swap(int[] arr, int first, int second) {
		int temp =arr[first];
		arr[first] = arr[second];
		arr[second] = temp;
	}

}
