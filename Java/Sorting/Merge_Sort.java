package Java.Sorting;
import java.util.*;

public class Merge_Sort {
    
    public static int[] merge(int[] word1, int[] word2)
    {
        int arr[]=new int[word1.length + word2.length];
        int i=0,j=0,k=0;
        while(i<word1.length && j<word2.length)
        {
            if(word1[i]<word2[j])
            {
                arr[k] = word1[i];
                i++;
            }
            else
            {
                arr[k] = word2[j];
                j++;
            }
            k++;
        }
        
        while(i<word1.length)
        {
            arr[k] = word1[i];
            i++;
            k++;
        }

        while(j<word2.length)
        {
            arr[k] = word2[j];
            j++;
            k++;
        }

        return arr;
    }

    public static void print(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.print("\n");
    }

    public static int[] sort(int[] arr)
    {
        if(arr.length<=1)
            return arr;
        
        int[] left = sort(Arrays.copyOfRange(arr,0,arr.length/2));        
        int[] right = sort(Arrays.copyOfRange(arr,arr.length/2, arr.length));
        
        return merge(left,right);
    }

    public static void main(String[] args) 
    {
        int[] a = {2,5,1,0,9,10};
        int[] b = sort(a);
        print(a);
        print(b);
    }
}

