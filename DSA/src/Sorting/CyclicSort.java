package Sorting;

import java.util.Arrays;

/*
 * question is 3,5,2,1,4 sort this array in one for loop
 * when given no from range 1 to n use cyclic sort
 * index = element - 1 because index starts from 0
 * 
 */
public class CyclicSort {
	public static void main(String[] args) {
		int[] arr = {3, 5, 2, 1 ,4};
		sort(arr);
		System.out.println(Arrays.toString(arr));
	}
	static void sort(int[] arr) {
		int i = 0;
		while(i < arr.length) {
			int correct = arr[i] - 1;
			if(arr[i] != arr[correct]) {
				swap(arr, i , correct);
			}else {
				i++;
			}
		}
	}

	static void swap(int[] arr, int first, int second) {
		int temp =arr[first];
		arr[first] = arr[second];
		arr[second] = temp;
	}
}
