//merge 2 list with the same length
//find the middle number of the merged list
#include <stdlib.h>
#include <stdio.h>

int find_median(int *L1,int *L2,int length) //L1 and L2 have the same length
{
    int i=0,j=0;
    for(int index=0;index<length-1;index++) //merger (length) times can get the median
    {
        if(L1[i]<L2[j])
            i++;
        else
            j++;
        
    }
    if(L1[i]<L2[j])
        return L1[i];
    else return L2[j];
}

int main()
{
    int L1[]={1,3,5,7,9};
    int L2[]={2,4,6,8,10};
    int median = find_median(L1,L2,sizeof(L1)/sizeof(L1[0]));
    printf("%d", median);
    return 0;
}

