package Java.Sorting;

public class InsertionSort {

    private static void PrintArray(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");

        }
        System.out.print("\n");
    }
    private static int[] Sorting(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            int key = arr[i];
            int j = i-1;
            while(j>=0 && arr[j]>key)
            {
                int p = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = p;
                j--;
            }
        }
        return arr;
    }
    public static void main(String[] args)
    {
        int[] arr = {2,5,9,0,5,6,8,85,12,8,10};
        PrintArray(arr);
        arr = Sorting(arr);
        PrintArray(arr);
    }
}
