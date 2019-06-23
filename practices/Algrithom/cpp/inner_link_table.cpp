#include <stdlib.h>
#include <stdio.h>
#define MAX_COL 10
#define ELE_TYPE int
// 用线性表实现二维表的内连接


typedef struct LNode1{
    struct LNode1 *next;
    ELE_TYPE data[MAX_COL];
}LNode;

typedef struct LNode2{
    struct LNode1 *next;
    ELE_TYPE line, column;
}HNode;

int CreateTable(HNode *&L)
{
    L->next = NULL;
    printf("input the lines and columns of the table:\n");
    scanf("%d%d", &L->line, &L->column);
    LNode *p, *pre;
    for (int i=0;i<L->line;i++)
    {
        p = (LNode*)malloc(sizeof(LNode));
        printf("input %d data of %d line:\n",L->column,i+1);
        for(int j=0;j<L->column;j++)
            scanf("%d", &p->data[j]);
        if(i==0)
        {
            p->next = L->next;
            L->next = p;
        }       
        else
        {
            p->next = pre->next;
            pre->next = p;
        }
        pre = p;
    }
    return 0;
}

int PrintTable(HNode *L)
{
    LNode* p = L->next;
    printf("Table:\n");
    for(int i=0;i<L->line;i++)
        {
        for(int j=0;j<L->column;j++)
            printf("%d ",p->data[j]);
        printf("\n");
        p = p->next;
        }
    return 0;
}

int InnerLink(HNode *&L1, HNode *&L2, HNode *&L)
{
    int key_t1,key_t2;
    printf("key columns of the 2 tables which to link by:");
    scanf("%d%d",&key_t1,&key_t2);
    L->line = 0;
    L->column = L1->column + L2->column;
    L->next = NULL;
    LNode *p,*r;
    LNode *p1=L1->next,*p2=L2->next;
    while(p1 != NULL)
    {
        while(p2 != NULL)
        {
            if(p1->data[key_t1-1]==p2->data[key_t2-1])
                //link the 2 lines
                {
                    p = (LNode*)malloc(sizeof(LNode));
                    for(int ii=0;ii<L1->column;ii++)
                        p->data[ii] = p1->data[ii];
                    for(int ii=0;ii<L2->column;ii++)
                        p->data[ii+L1->column] = p2->data[ii];
                    if(L->next == NULL)
                        L->next = p;
                    else
                        r->next = p;
                    r = p;
					L->line++;
                }
                p2 = p2->next;
        }
		p2 = L2->next;
        p1 = p1->next;
    }
    r->next = NULL;
    return 0;
}


int main()
{
    HNode *L = (HNode *)malloc(sizeof(HNode));
    HNode *L1 = (HNode *)malloc(sizeof(HNode));
    HNode *L2 = (HNode *)malloc(sizeof(HNode));
    CreateTable(L1);
    CreateTable(L2);
	PrintTable(L1);
	PrintTable(L2);
    InnerLink(L1,L2,L);
    PrintTable(L);
    return 0;
}

