#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#define MAX_STACK_SIZE 256
#define ELE_TYPE char

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

bool IsInString(char c, char *s)
{
    for(int i=0;s[i]!='\0';i++)
        if(c == s[i])
            return true;
    return false;
}

int GetPrior(char c)
{
    char *s1 = "+-";
    char *s2 = "*/";
    if(IsInString(c,s1))
        return 1;
    else if(IsInString(c,s2))
        return 2;
    else if(c == '(')
        return 0;
}

bool IsNum(char c)
{
    char *s = "0123456789";
    if(IsInString(c,s))
        return true;
    return false;
}

int EasyArithmetic(int x, int y,char c)
{
    switch(c)
    {
        case '+' : return x+y;
        case '-' : return x-y;
        case '*' : return x*y;
        case '/' : return x/y;
    }
}


int Calculate(char *s) //calculate the value of a expression only contains +-*/
{
    char post_exp[100] = {'\0'};
	// printf("%d",post_exp[90]);
    int i=0,j=0,result=0;
    // ------------------------------Transform middian exp to post exp--------------------------------------------
    for(;s[i]!='\0';i++)
    {
        if(IsNum(s[i]))
            {post_exp[j]=s[i];j++;} //if is a num, append it to post_exp
        else
        {
            if(i!=0 and IsNum(s[i-1])) //don't take account expressions starting with "+-*/" , that's illegal
                {post_exp[j]='#';j++;}  //add a # to the end of a num
            if(s[i]=='(') //if it is '(', push it to stack
                PushStack(L,s[i]);
            else if(s[i]==')') //when it is ')', pop all operator until '('
                {
                    while(GetStackTop(L)!='(')
                        {post_exp[j]=PopStack(L);j++;}
                    PopStack(L);
                }
            else if(IsEmptyStack(L) or GetPrior(s[i])>GetPrior(GetStackTop(L)))
                PushStack(L,s[i]);
            else
                {
                    while(!IsEmptyStack(L) and GetStackTop(L)!='(' and GetPrior(s[i])<=GetPrior(GetStackTop(L)))
                        // pop all operators until it is '(' or the stack is empty or the top is not less prior
                        {post_exp[j]=PopStack(L);j++;}
                    PushStack(L,s[i]);
                }         
        }
    }
    while(!IsEmptyStack(L))
        {post_exp[j]=PopStack(L);j++;}
    printf("%s\n", post_exp);
    
    // ------------------------------calculate post expression--------------------------------------------
	int k=0;
	StackNode *L1;
	InitStack(L1);
	int position,num;
	int x,y;
	while(post_exp[k]!='\0')
	{
		for(;IsNum(post_exp[k]);k++)
			PushStack(L1,post_exp[k]);
		position = 1,num=0;
		while(!IsEmptyStack(L1))
			{num+=PopStack(L1)* position; position=position*10;}
		// printf("%d\n",post_exp[k]);
		PushStack(L,num);
        if(post_exp[k]=='#')
			k++;
		else
			{
				y = PopStack(L);
				x = PopStack(L);
				result = EasyArithmetic(x,y,post_exp[k]);
				PushStack(L,result);
			}				
	}
    return result;
}

int main()
{
    InitStack(L);
    char s[50];
    std::cin>>s; 
    // printf("s is: %s", s);
    int r=Calculate(s);
	printf("%d\n",r);
    return 0;
}
