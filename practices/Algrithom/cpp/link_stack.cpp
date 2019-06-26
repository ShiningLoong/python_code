#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 256
#define ELE_TYPE int

typedef struct LNode{
    ELE_TYPE data;
    LNode *next;
}StackNode;

StackNode *L; //全局变量

int InitStack(StackNode *&L)
{
    L = (StackNode *)malloc(sizeof(StackNode));
    L->next = NULL;
    return 0;
}

ELE_TYPE GetStackTop(StackNode *L)
{
    if(L->next != NULL)
        return L->next->data;
    else
        exit(1);
}

ELE_TYPE PopStack(StackNode *L)
{
    StackNode *p = L->next;
    if(p == NULL)
        exit(1);
    L->next = p->next;
    ELE_TYPE e = p->data;
    free(p);
    return e;
}

void PushStack(StackNode *L, ELE_TYPE e)
{
    StackNode *p = (StackNode *)malloc(sizeof(StackNode));
    p->data = e;
    p->next = L->next;
    L->next = p;
}

bool IsEmptyStack(StackNode *L)
{
    if(L->next == NULL)
        return true;
    return false;
}

bool IsBracketMatch(char *s)
{
    for(int i=0;s[i]!='\0';i++)
    {
        if(s[i] == '(')
            PushStack(L,s[i]);
        else if(s[i] == ')')
             if(IsEmptyStack(L))
                 return false;
             else
                 PopStack(L);               
    }
    if (IsEmptyStack(L))
        return true;
    else
        return false;
}

int Calculate(*s) //calculate the value of a expression only contains +-*/
{
    
}

int main()
{
    InitStack(L);
    char *s = "ask(akjsnsav)(kjbskjvd)kn((knjdv)anv)mkkm()a(sv";
    if(IsBracketMatch(s))
        printf("OK");
    else
        printf("Not match");
    return 0;
}
