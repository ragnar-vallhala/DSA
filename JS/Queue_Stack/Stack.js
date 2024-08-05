class Stack
{

    constructor()
    {
        this.items = [];
    }
    push(element)
    {
        this.items.push(element);
    }
    pop()
    {
        return this.items.pop();
    }
    peek()
    {
        return this.items[this.items.length - 1];
    }
    length()
    {
        return this.items.length ;
    }

}


s = new Stack();
s.push(5);
s.push(51);
s.push(55);
s.push(59);

for(i=0;i<4;i++)
{
    console.log(s.pop());
}