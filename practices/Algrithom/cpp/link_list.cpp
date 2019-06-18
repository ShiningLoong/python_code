#include <stdlib.h>
#include <stdio.h>
#define ELE_TYPE int
typedef struct LNode{
    ELE_TYPE data;
    struct LNode * next;
}LinkNode;

int InitLinkList(LinkNode*& L, ELE_TYPE a[], int n)
{
    L = (LinkNode*)malloc(sizeof(LinkNode));
    int i = 0;
    LinkNode* pre = L;
    for (;i<n;i++)
    {
        LinkNode* p = (LinkNode*)malloc(sizeof(LinkNode));
        p->data = a[i];
        pre->next = p;
        pre = p;
    }
    pre->next = NULL;
    return 0;
}

int PrintLinkList(LinkNode* L)
{
    //LinkNode * pre = L;
    if(L == NULL)
        return -1;
    LinkNode * p = L->next;
    while (p->next != NULL)
    {
        printf("%d ", p->data);
        p = p->next;        
    }
    printf("%d\n", p->data);
    return 0;
}

int DestroyLinkList(LinkNode*& L)
{
    LinkNode* p = L;
    LinkNode* next_p = p->next;
    while(next_p != NULL)
    {
        free(p);
        p = next_p;
        next_p = p->next;      
    }
    free(p);
    L = NULL;
    return 0;
}

int GetNodeByIndex(LinkNode* L, int i, ELE_TYPE & e)
{
    if (i <= 0)
        return false;
    LinkNode * p = L->next;
    while(--i > 0 && p != NULL)
        p = p->next;
    if (p == NULL)
        return false;
    else
        e = p->data;
    return true;
}

int GetNodeByValue(LinkNode* L, ELE_TYPE v)
{
    LinkNode* p = L->next;
    int i = 0;
    while(p != NULL)
    {
        i ++;
        if (p->data == v)
            break;
        p = p->next;
    }
    if (p == NULL)
        return -1;
    return i;
}

int InsertLinkLisk(LinkNode* L, int i, ELE_TYPE e)    
{
    if (i <= 0)
        return -1;
    LinkNode* p = L;
    while(--i>0 && p != NULL)
        p = p->next;
    if (p == NULL)
        return -1;
    LinkNode* new_node = (LinkNode*)malloc(sizeof(LinkNode));
    new_node->data = e;
    new_node->next = p->next;
    p->next = new_node;
    return 0;
}

int DeleteLinkNode(LinkNode *L, ELE_TYPE &e, int i)
{
    if (i<=0)
        return -1;
    LinkNode *p = L;
    while(--i > 0 && p != NULL)
        p = p->next;
    if (p == NULL)
        return -1;
    if (p->next == NULL)
        return -1;
    LinkNode* q = p->next;
    p->next = q->next;
    e = q->data;
    free(q);
    return 0;
}

int SortLinkList_select(LinkNode *L) //选择排序
{
    LinkNode *start = L->next;
    LinkNode *p = start; 
    LinkNode *tmp_p = p;
    ELE_TYPE tmp;
    while(start != NULL)
    {
        while(p != NULL)
        {
            if(tmp_p->data < p->data)
                tmp_p = p;
            p = p->next;
        }
        tmp = tmp_p->data;
        tmp_p->data = start->data;
        start->data = tmp;
        start = start->next;
        p = start;
        tmp_p = start;
    }
    return 0;
}

int ReverseLinkList(LinkNode *L)
{
    LinkNode *p = L->next, *q;
    L->next = NULL;
    while(p != NULL)
    {
        q = p->next;
        p->next = L->next;
        L->next = p;
        p = q;
    }
    return 0 ;
}


int SplitLinkList(LinkNode *L, LinkNode *&L1)
{
    L1 = (LinkNode *)malloc(sizeof(LinkNode));
    LinkNode *p = L->next,*q;
    L->next = NULL;
    L1->next = NULL;
    LinkNode *tail = L; //point to tail of L1
    while(p!=NULL)
    {
        q = p->next;
        p->next = tail->next;
        tail->next = p;
        tail = p;
        
        if(q != NULL)
        {
            p = q->next;
            q->next = L1->next;
            L1->next = q;
            q = p->next;
        }
        else
            p = q;            
    }
    return 0;
}

// int Split(LinkNode *&L, LinkNode *&L1, LinkNode *&L2)  //课件中的代码步骤有误
// {
    // LinkNode *p=L->next,*q,*r1;
    // L1=L;			//L1利用原来L的头结点
    // r1=L1;			//r1始终指向L1的尾结点
    // L2=(LinkNode *)malloc(sizeof(LinkNode));    //创建L2的头结点
    // L2->next=NULL;		//置L2的指针域为NULL     
    // while (p!=NULL)
      // {	r1->next=p;		//采用尾插法将*p(data值为ai)插入L1中
        // r1=p;
        // p=p->next;		//p移向下一个结点(data值为bi)
        // q=p->next;     		//用q保存*p的后继结点
        // p->next=L2->next;	//采用头插法将*p插入L2中
        // L2->next=p;
        // p=q;			//p重新指向ai+1的结点
      // }
    // r1->next=NULL;		//尾结点next置空
    // return 0;
// }

int main()
{
    ELE_TYPE a[] = {1,3,4,65,66,88,133,-2,-99,-123,897};
    LinkNode* L;
    InitLinkList(L,a, sizeof(a)/sizeof(a[0]));
    PrintLinkList(L);
    LinkNode * L1;
    SplitLinkList(L,L1);
    PrintLinkList(L);
    PrintLinkList(L1);
    // LinkNode *L2;
    // Split(L,L1,L2);
    // PrintLinkList(L1);
    // PrintLinkList(L2);
    return 0;
}

