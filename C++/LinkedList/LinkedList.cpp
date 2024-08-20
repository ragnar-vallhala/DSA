#include "LinkedList.h"

template <typename T>
LinkedList<T>::LinkedList()
{
}
template <typename T>
LinkedList<T>::~LinkedList()
{
    while (head != nullptr)
    {
        Node* curr = head;
        head=head->next;
        delete curr;
    }
}

template <typename T>
void LinkedList<T>::add(T data)
{
    Node* newNode = new Node(data);
    if (head == nullptr)
        head = newNode;
    else
    {
        Node* curr = head;
        while (curr->next != nullptr)
        {
            curr=curr->next;
        }
        curr->next = newNode;
    }
}

template <typename T>
void LinkedList<T>::remove(T data)
{
    Node* curr = head;
    if(curr!=nullptr && curr->data==data)
    {
        head=curr->next;
        delete curr;
        return;
    }
    while(curr->next!=nullptr)
    {
        if(curr->next->data==data)
        {
            curr->next = curr->next->next;
            delete curr->next;
            return;
        }
        curr=curr->next;
    }
}

template <typename T>
void LinkedList<T>::printList()
{
    Node* curr = head;
    while(curr!=nullptr)
    {
        std::cout<<curr->data<<" ";
        curr=curr->next;
    }
    std::cout<<std::endl;
}

template <typename T>
int LinkedList<T>::size()
{
    int n=0;
    Node* curr = head;
    while(curr!=nullptr)
    {
        n++;
        curr=curr->next;
    }
    return n;
}
