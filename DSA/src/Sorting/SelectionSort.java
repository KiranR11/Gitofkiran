package Sorting;

import java.util.Arrays;

/*
 * selecting an element and putting at its right position(index)
 * swapped with correct index
 * (n-1),,,,0
 * find largest or smallest one and swap
 * not stable
 * number of comparison (n-i-1)
 */
public class SelectionSort {
	public static void main(String[] args) {
		int[] arr = {3, 1, 5, 4, 2};
		selection(arr);
		System.out.println(Arrays.toString(arr));
	}
	static void selection(int[] arr) {
		for(int i = 0; i < arr.length; i++) {
			//find the max item in the remaining array and swap with correct index\
			int last = arr.length - i - 1;
			int maxIndex = getMaxindex(arr, 0, last);
			swap(arr , maxIndex, last);
			
		}
	}
	private static int getMaxindex(int[] arr, int start, int end) {
		// TODO Auto-generated method stub
		int max = start;
		for(int i = start; i <= end; i++) {
			if(arr[max] < arr[i]) {
				max = i ;
			}
		}
		
		return max;
	}
	
	static void swap(int[] arr, int first, int second) {
		int temp =arr[first];
		arr[first] = arr[second];
		arr[second] = temp;
	}
}
