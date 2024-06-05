package Java.Sorting;
import java.util.*;

public class QuickSort {
    
    public static void main(String[] args)
    {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(2,5,9,0,5,6,8,85,12,8,10));
        System.out.println(arr);
        quickSort(arr,0,arr.size()-1);
        System.out.println(arr);
    }
    
    public static void quickSort(ArrayList<Integer> arr, int l, int h)
    {
        if(h-l<=1)
            return;
        int key = partition(arr,l,h);
        quickSort(arr,l,key-1);
        quickSort(arr,key+1,h);
    }
    public static int partition(ArrayList<Integer> arr, int l, int h)
    {
        int i = l;
        int j = h;
        while(i<j)
        {
            int key = arr.get(i);
            while(arr.get(i)<=key) i++;
            while(arr.get(j)>key) j--;
            if(i<j)
            {
                int temp = arr.get(i);
                arr.set(i,arr.get(j));
                arr.set(j,temp);
            }
        }
        int temp = arr.get(l);
        arr.set(l,arr.get(j));
        arr.set(j,temp);
        return j;
    }
}
