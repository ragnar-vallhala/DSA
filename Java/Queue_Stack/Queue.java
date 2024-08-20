package Java.Queue_Stack;

import java.util.ArrayList;

public class Queue {

    public Queue()
    {
        m_arr = new ArrayList<Integer>();
    };

    public void Enqueue(int item)
    {
        m_arr.add(item);
    }

    public int Dequeue()
    {
        int n = m_arr.get(0);
        m_arr.remove(0);
        return n;
    }

    public int Size()
    {
        return m_arr.size();
    }


    private ArrayList<Integer> m_arr;
    
}