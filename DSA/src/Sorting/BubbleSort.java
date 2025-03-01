package Sorting;

import java.util.Arrays;

/*step 1 : in every step comparing adjacent numbers.
 *if first element is > than second swap it.
 *Why? with first parse through entire array,
 *first largest element is at end.
 *also known as sinking sort or exchanging sort.inplace sorting algorithm
 *i = 0 ; j = 1; is j > j - 1 ==swap then j = +1 ; continue until 
 *j will out of bound do until n-1 times.i is a counter.
 *then i = 1 second pass. j will go until length - i; or <= length - i - 1
*/

public class BubbleSort {
	public static void main(String[] args) {
		  int[] arr= {5, 4, 3, 2, 1};
		  bubble(arr);
		  System.out.println(Arrays.toString(arr));
	}
	static void bubble(int[] arr) {
		boolean swapped;
		
		//run the steps n-1 times
		for(int i = 0; i < arr.length; i++) {
			swapped = false;
			//for each step max will come at last respective index
			for(int j = 1; j<arr.length - i; j++) {
				//swap if the number is smaller then the previous item
				if(arr[j] < arr[j - 1]) {
					//swap
					int temp = arr[j];
					arr[j] = arr[j - 1];
					arr[j - 1] = temp;
					swapped=true;
				}
			}
			//if you did not swap for a particular value of i;
			if(!swapped) {
				break;
			}
		}
	}
}
