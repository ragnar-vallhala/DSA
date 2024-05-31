function merge(nums1, nums2) 
{
    let result = [];
    let i = 0, j = 0;
    while(i<nums1.length && j<nums2.length )
    {
        if(nums1[i] < nums2[j])
        {
            result.push(nums1[i]);
            i++;
        }
        else
        {
            result.push(nums2[j]);
            j++;
        }
    }
    
    while(i<nums1.length)
    {
        result.push(nums1[i]);
        i++;    
    }

    while(j<nums2.length)
    {
        result.push(nums2[j]);
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