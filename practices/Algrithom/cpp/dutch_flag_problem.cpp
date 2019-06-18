#include <stdio.h>
#include <stdlib.h>
#define ELE_TYPE int
#define MAX_SIZE 256

typedef struct LinkND{
    ELE_TYPE data;
    struct LinkND *next;
}LinkNode;

struct LinearList{
    ELE_TYPE data[MAX_SIZE];
    int length;
};

int InitLinearList(LinearList* linear_list, ELE_TYPE array[], int n)
{
    linear_list->length = n;
    for (int i=0;i<n;i++)
        linear_list->data[i] = array[i];
    return 0;
}

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

int PrintLinearList(LinearList* L)
{
    printf("List's length is: %d\n", L->length);
    printf("values are: ");
    for (int i=0;i<L->length;i++)
        printf("%d ", L->data[i]);
    printf("\n");
    return 0;
}


int swap(ELE_TYPE &p, ELE_TYPE &q)
{
    ELE_TYPE temp = p;
    p = q;
    q = temp;
    return 0;
}


int solve_linear(LinearList* L)
{
    int p = 0, i = 0, j = L->length-1;
    while(p <= j)
    {
        if(L->data[p]==0)
        {
            swap(L->data[i],L->data[p]);
            i++;
            p++;
        }
        else if(L->data[p]==2)
        {
            swap(L->data[j],L->data[p]);
            j--;
        }
        else 
            p++;        
    }
    return 0;
}

int main()
{
    ELE_TYPE list[] = {1,2,0,0,0,2,2,1,2,2,0,0,0,2,1,2,1,2,1,1,2,2,0};
    int length = sizeof(list)/sizeof(list[0]);  
    LinearList *L1 = (LinearList*)malloc(sizeof(LinearList));
    LinkNode *L2;
    InitLinearList(L1,list,length);
    InitLinkList(L2,list,length);
    PrintLinearList(L1);
    PrintLinkList(L2);
    solve_linear(L1);
    PrintLinearList(L1);
    
    return 0;
}

