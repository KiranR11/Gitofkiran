package dsa.Heaps;

import java.util.ArrayList;

import dsa.Heap;

public class Main {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		Heap<Integer> heap = new Heap<>();
		
		heap.insert(34);
		heap.insert(45);
		heap.insert(22);
		heap.insert(89);
		heap.insert(76);
		heap.insert(75);
		
//		System.out.println(heap.remove());
		
		
		ArrayList list = heap.heapSort();
		System.out.println(list);
	}

}
