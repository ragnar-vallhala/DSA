#include <iostream>
#include <vector>

class Stack
{
public:
    Stack();
    void push(int value);
    int pop();
    int size();
private:
    std::vector<int> items;
};



int main()
{
    Stack q;
    q.push(1);
    q.push(3);
    q.push(5);
    q.push(7);
    q.push(2);
    for (int i{};i<5;i++)
    {
        std::cout<<q.pop()<<std::endl;
    }
    return 0;
}


Stack::Stack()
{
    items = std::vector<int>();
}

void Stack::push(int value)
{
    this->items.push_back(value);
}

int Stack::pop()
{
    int n = items[items.size()-1];
    this->items.pop_back();
    return n;
}

int Stack::size()
{
    return this->items.size();
}