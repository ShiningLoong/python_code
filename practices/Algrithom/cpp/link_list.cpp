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

int main()
{
    ELE_TYPE a[] = {1,3,4,65,66,88,133,-2};
    LinkNode* L;
    InitLinkList(L,a, sizeof(a)/sizeof(a[0]));
    PrintLinkList(L);
    // printf("%d", L->next->data);
    // DestroyLinkList(L);
    // PrintLinkList(L);
    int i ;
    ELE_TYPE e;
    scanf("%d", &i);
    // ELE_TYPE e;
    // if(GetNodeByIndex(L, i, e))
        // printf("%d", e);
    // printf("%d", GetNodeByValue(L, i));
    // printf("%d\n", InsertLinkLisk(L,i,e));
    printf("%d\n", DeleteLinkNode(L,e,i));
    PrintLinkList(L);
    return 0;
}

