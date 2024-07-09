#include<iostream>
using namespace std;
#define MAX 10

struct Que
{
    int queue[MAX];
}s;
class Queue
{
    public:
    int ele ,i;
    int rr,ft;
    void insert();
    void delet();
    void display();
    Queue()
    {
        rr=ft=-1;
    }
};


void Queue::insert()
{
    if (rr==MAX-1)
    { 
        cout<<"Queue is FULL!!!"<<endl;
    }
    else
    {
        cout<<"Enter the job element:\n";
        cin>>ele;
        rr=rr+1;
        s.queue[rr]=ele;
    }
    if (rr==0)
    {
        ft=0;
    }
};


void Queue::delet()
{
    if(ft==-1)
    {
        cout<<"Queue is EMPTY!!!"<<endl;
    }

    else
    {
        cout<<"Delet the job:-";
        ft=ft+1;
    }

    if (ft>rr)
    {
        cout<<"Queue is EMPTY!!!"<<endl;
    }

};  

void Queue::display()
{
    cout<<"JOB QUEUE IS:\n";
    for (i=ft;i<=rr;i++)
    {
        cout<<"\t"<<s.queue[i];
    }
};

int main()
{
    int ch;
    Queue q;
    do
    {
        cout<<endl<<"-----MENU-----"<<endl;
 
        cout<<"1.INSERT THE JOB IN THE QUEUE"<<endl;
 
        cout<<"2.DELETE THE JOB IN THE QUEUE"<<endl;
 
        cout<<"3.DISPLAY THE QUEUE"<<endl;
 
        cout<<"4.EXIT"<<endl;
 
        cout<<"Enter the choice:- ";
 
        cin>>ch;

        switch (ch)
        {
        case 1:
            q.insert();
            break;
        case 2:
            q.delet();
            break;
        case 3:
            q.display();
            break;
        case 4:
            return 0;
        default:
            cout<<"INVALID CHOICE";
            break;
        }
    }
    while(ch!=4);
    return 0;
};
