function merge(arr1, arr2) 
{
    let result = [];
    let i = 0, j = 0;
    while(i<arr1.length && j<arr2.length )
    {
        if(arr1[i] < arr2[j])
        {
            result.push(arr1[i]);
            i++;
        }
        else
        {
            result.push(arr2[j]);
            j++;
        }
    }
    
    while(i<arr1.length)
    {
        result.push(arr1[i]);
        i++;    
    }

    while(j<arr2.length)
    {
        result.push(arr2[j]);
        j++;    
    }

    return result;
}

function sort(arr)
{
    if(arr.length <= 1)
    {
        return arr;
    }

    let left = sort(arr.slice(0,arr.length/2))
    let right = sort(arr.slice(arr.length/2, arr.length))
    return merge(left, right);
}

function print(arr)
{
    let s = "";
    for(let i=0;i<arr.length;i++)
    {
        s+=String(arr[i]) + " ";
    }
    console.log(s);
}

let arr = [2,5,9,0,5,6,8,85,12,8,10];
print(arr);
arr = sort(arr);
print(arr); 