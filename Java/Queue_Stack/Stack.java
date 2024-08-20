package Java.Queue_Stack;

import java.util.ArrayList;

public class Stack {
     public Stack()
    {
        m_arr = new ArrayList<Integer>();
    };

    public void Push(int item)
    {
        m_arr.add(item);
    }

    public int Pop()
    {
        int n = m_arr.get(Size()-1);
        m_arr.remove(Size()-1);
        return n;
    }

    public int Size()
    {
        return m_arr.size();
    }


    private ArrayList<Integer> m_arr;
    
}

