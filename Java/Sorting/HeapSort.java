package Java.Sorting;
import java.util.*;

public class HeapSort
{
    
    static ArrayList<Integer> insert(ArrayList<Integer> heap, int num)
    {
        heap.add(num);
        int i = heap.size()-1;
        while(i>0)
        {
            int parent = (i-1)/2;
            if(heap.get(parent)<heap.get(i))
            {
                int temp = heap.get(parent);
                heap.set(parent, heap.get(i));
                heap.set(i,temp);
                i=parent;
            }
            else
            {
                break;
            }
        }
        return heap;
    }

    static ArrayList<Integer> makeHeap(ArrayList<Integer> arr)
    {
        ArrayList<Integer> heap = new ArrayList<Integer>();
        for(int i=0;i<arr.size();i++)
        {
            heap = insert(heap,arr.get(i));
        }
        return heap;
    }

    static ArrayList<Integer> heapify(ArrayList<Integer> heap, int index, int size)
    {
        if(index>=size)
        {
            return heap;
        }
        while(index<size)
        {
            int left = 2*index + 1;
            int right = 2*index + 2;
            int largest = index;
            if(left<size && heap.get(left)>heap.get(largest))
            {
                largest = left;
            }
            if(right<size && heap.get(right)>heap.get(largest))
            {
                largest = right;
            }
            if(largest!=index)
            {
                int temp = heap.get(index);
                heap.set(index,heap.get(largest));
                heap.set(largest,temp);
                index=largest;
            }
            else
            {
                break;
            }

        }
        return heap;
    }

    static ArrayList<Integer> heapSort(ArrayList<Integer> arr)
    {
        ArrayList<Integer> heap = makeHeap(arr);
        for(int i = heap.size()-1;i>0;i--)
        {
            int temp = heap.get(0);
            heap.set(0,heap.get(i));
            heap.set(i,temp);
            heap = heapify(heap,0,i);
        }
        return heap;
    }


    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<Integer>(); 
        int n = scanner.nextInt();
        while(n>0)
        {
            int num = scanner.nextInt();
            arr.add(num);
            n--;
        }
        System.out.println(arr);
        arr = heapSort(arr);
        System.out.println(arr);
        scanner.close();      
    }
};