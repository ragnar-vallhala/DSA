function partition(arr,l,h)
{
    var i=l
    var j=h

    while(i<j)
    {
        var key = arr[i];
        while(arr[i]<=key) i++;
        while(arr[j]>key) j--;
        if (i<j)
        {
            var temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    var temp = arr[l];
    arr[l] = arr[j];
    arr[j] = temp;
    return [arr,j]
}

function quickSort(arr,l,h)
{
    if(h-l<=1)
    {
        return arr;
    }
    res = partition(arr,l,h);
    arr = res[0];
    key = res[1];
    arr = quickSort(arr,key+1,h)
    arr = quickSort(arr,l,key-1)
    return arr
}

arr = [2,5,9,0,5,6,8,85,12,8,10]
console.log(quickSort(arr,0, arr.length-1));