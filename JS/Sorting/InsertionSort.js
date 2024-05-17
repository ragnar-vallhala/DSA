function sort(arr) {
    for(let i=0;i<arr.length;i++)
    {
        let key = arr[i];
        let j = i-1;
        while(j>=0 && arr[j]>key)
        {
            let p = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = p;
            j--;
        }
    }    
    return arr;
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

