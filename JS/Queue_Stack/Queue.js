class Queue
{

    constructor()
    {
        this.items = [];
    }
    enqueue(element)
    {
        this.items.push(element);
    }
    dequeue()
    {
        return this.items.shift();
    }
    peek()
    {
        return this.items[0];
    }
    length()
    {
        return this.items.length ;
    }

}


s = new Queue();
s.enqueue(5);
s.enqueue(51);
s.enqueue(55);
s.enqueue(59);

for(i=0;i<4;i++)
{
    console.log(s.dequeue());
}