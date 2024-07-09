/*A double-ended queue (deque) is a linear list in which additions and deletions may be made at either end. Obtain a data representation mapping a deque into a one-dimensional array. Write C++ program to simulate deque with functions to add and delete elements from either end of the deque.
*/

#include<iostream>
using namespace std;
#define SIZE 10

class dequeue
{
    int a[SIZE],front,rear,count;

    public:
    dequeue();
    void add_fr(int);
    void add_rr(int);
    void del_fr();
    void del_rr();
    void display();
};

dequeue::dequeue()
{
    front=-1;
    rear=-1;
    count=0;
}

void dequeue::add_fr(int item)
{
    int i;
    if (front=-1)
    {
        front++;
        rear++;
        a[rear]=item;
        count++;
    }
    else if (rear>=SIZE-1)
    {
        cout<<"Queue is FULL!!!"<<endl;
    }
    else
    {
        for(i=count;i>=0;i--)
        {
            a[i]=a[i-1];
        }
        a[i]=item;
        count++;
        rear++;
    }
};

void dequeue::add_rr(int item)
{
    if (front=-1)
    {
        front++;
        rear++;
        a[rear]=item;
        count++;
    }
    else if (rear>=SIZE-1)
    {
        cout<<"Queue is FULL!!!"<<endl;
    }
    else
    {
        a[++rear]=item;
    }

}

void dequeue::del_fr()
{
    if (front=-1)
    {
        cout<<"Queue is EMPTY!!!";
    }
    else 
    {   if (front==rear)
        {
            front=rear=-1;
        }
    }
        cout<<"Deleted element is ;"<<a[front];
        front=front+1;
    
}

void dequeue::del_rr()
{
    if (front=-1)
    {
        cout<<"Queue is EMPTY!!";
    }
    else
    {   if (front==rear)
        {
            front=rear=-1;
        }
    }
        cout<<"Deleted element is ;"<<a[rear];
        rear=rear-1;
    
}


void dequeue::display()
{
    int i;
    for(i=front;i<=rear;i++)
    {
        cout<<a[i]<<" ";
    }
}




int main()
{
    int c,item;
    dequeue deq;
    do
    {
        cout<<"\n\n****DEQUEUE OPERATION****\n";
		cout<<"\n1-Insert at beginning";
		cout<<"\n2-Insert at end";
		cout<<"\n3_Deletion from front";
		cout<<"\n4-Deletion from rear";
        cout<<"\n5_Display";
		cout<<"\n6_Exit";
		cout<<"\nEnter your choice<1-6>:\n";
		cin>>c;

        switch (c)
        {
        case 1:
            cout<<"Enter the element:";
            cin>>item;
			deq.add_fr(item);
            break;
        case 2:
            cout<<"Enter the element:";
            cin>>item;
            deq.add_rr(item);
            break;
        case 3:
            deq.del_fr();
            break;
        case 4:
            deq.del_rr();
            break;
        case 5:
            deq.display();
            break;
        case 6:
                return 0;
        default:
            cout<<"INVALID INPUT";
            break;
        }



    } while (c!=6);

    return 0;
    
}