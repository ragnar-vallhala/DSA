package Java.Queue_Stack;

public class Main {


    public static void main(String[] args)
    {
        Stack stack = new Stack();
        stack.Push(5);
        stack.Push(55);
        stack.Push(56);
        stack.Push(15);
        for(int i=0;i<4;i++)
        {
            System.out.println(stack.Pop());
        }
    }
    
}