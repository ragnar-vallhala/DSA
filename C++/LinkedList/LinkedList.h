#pragma once
#include"Node.h"
#include<iostream>
template<typename T>

class LinkedList
{
public:
    LinkedList();
    ~LinkedList();
    void add(T data);
    void remove(T data);
    void printList();
    int size();
private:
    Node<T>* head = nullptr;
};

