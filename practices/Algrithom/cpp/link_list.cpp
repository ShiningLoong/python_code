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
    L->next = NULL;
    int i = 0;
    for (;i<n;i++)
    {
        LinkNode* pre = L;
        LinkNode* p = (LinkNode*)malloc(sizeof(LinkNode));
        p->data = a[i];
        p->next = pre->next;
        pre->next = p;
    }
    return 0;
}

int PrintLinkList(LinkNode* L)
{
    //LinkNode * pre = L;
    LinkNode * p = L->next;
    while (p->next != NULL)
    {
        printf("%d ", p->data);
        p = p->next;
        
    }
    printf("%d\n", p->data);
    return 0;
}

int main()
{
    ELE_TYPE a[] = {1,3,4,65,66,88,133,-2};
    LinkNode* L;
    InitLinkList(L,a, sizeof(a)/sizeof(a[0]));
    PrintLinkList(L);
    printf("%d", L->next->data);
    return 0;
}

