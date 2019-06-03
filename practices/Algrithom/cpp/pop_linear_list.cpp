#include <stdlib.h>
#include <stdio.h>
#define MAX_SIZE 256
#define ELE_TYPE int
using namespace std;

ELE_TYPE a[] = {1,2,-6,2,-7,-2,-8,2,2222,135,-999,-888,-11,87};
typedef struct {
    ELE_TYPE data[MAX_SIZE];
    int length;
}LinearList;

int InitList(LinearList* linear_list, int array[], int n)
{
    linear_list->length = n;
    for (int i=0;i<n;i++)
        linear_list->data[i] = array[i];
    return 0;
}

int PrintList(LinearList* L)
{
    printf("List's length is: %d\n", L->length);
    printf("values are: ");
    for (int i=0;i<L->length;i++)
        printf("%d ", L->data[i]);
    printf("\n");
    return 0;
}

int PopAll_x(LinearList* L, ELE_TYPE x)
{
    int k = 0;
    for (int i=0;i<L->length;i++)
        if (L->data[i] == x)
            k += 1;
        else
            L->data[i-k] = L->data[i];
        L->length -= k;
    return 0;
}

int DevideList(LinearList* L)
{
    int boundary = 0;
    int tmp = 0;
    for (int i=1;i+boundary<L->length;)
        if (L->data[boundary+i] <= L->data[boundary])
        {
            tmp = L->data[boundary+i];
            for (int j=boundary+i-1;j>=boundary;j--)
                L->data[j+1] = L->data[j];
            L->data[boundary] = tmp;
            boundary += 1;
        }
        else
            i += 1;
    return 0 ;
        
}

int DevideList2(LinearList* L) //使用前后交换的方法
{
    int i = 0;
    int j = L->length-1;
    ELE_TYPE tmp;
    while (i != j)
    {
        while(i <j && L->data[j]>L->data[0])
            j--;
        while(i<j && L->data[i]<=L->data[0])
            i++;
        if(i<j)
        {
           tmp = L->data[i];
           L->data[i] = L->data[j];
           L->data[j] = tmp;
        }      
    }
    tmp = L->data[0];
    L->data[0] = L->data[j];
    L->data[j] = tmp;   
    return 0;
}

int DevideList3(LinearList* L)
{
    int i = 0;
    int j = L->length - 1;
    int tmp = L->data[0];
    while(i < j)
    {
        while(i<j && L->data[j] > tmp)
            j--;
        L->data[i] = L->data[j];
        while(i<j && L->data[i]<= tmp)
            i++;
        L->data[j] = L->data[i];
    }
    L->data[i] = tmp;
    return 0;
}


int main()
{
LinearList* L = (LinearList *)malloc(sizeof(LinearList));
InitList(L,a,sizeof(a)/sizeof(a[0]));
PrintList(L);
// PopAll_x(L, 2);
// PrintList(L);
// printf("%d", L->data[255]); # 不会越界
DevideList3(L);
PrintList(L);
return 0;
}

