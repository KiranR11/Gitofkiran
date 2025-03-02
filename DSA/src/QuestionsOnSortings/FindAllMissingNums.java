package QuestionsOnSortings;

import java.util.ArrayList;
import java.util.List;

/*
 *Google
 * find all missing nums
 * if range = 0,n then index = value
 * if range = 1,n then index = value-1
 */

public class FindAllMissingNums {

	public static void main(String[] args) {
		int[] arr = {1,3,4,5,3,4,3};
		System.out.println(findDisappearedNumbers(arr));
	}
	
	public static List<Integer> findDisappearedNumbers(int[] arr){
		int i = 0;
		while(i < arr.length) {
			int correct = arr[i] - 1;
			if(arr[i] != arr[correct]) {
				swap(arr, i , correct);
			}else {
				i++;
			}
		}
		//just find missing numbers
		List<Integer> ans = new ArrayList<>();
		for(int index=0; index<arr.length; index++) {
			if(arr[index] != index+1) {
				ans.add(index +1);
			}
		}
		return ans;
	}
	

	static void swap(int[] arr, int first, int second) {
		int temp =arr[first];
		arr[first] = arr[second];
		arr[second] = temp;
	}
}
