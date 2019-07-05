#include <stdio.h>
#include <stdlib.h>
#define MaxSize 1024
// solve maze problem by queue
int maze[20][20] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};


struct Block{
  int i;
  int j;
  int pre;  
};

typedef struct {
    Block data[MaxSize];
    int front;   //指向第一个元素的前面位置
    int rear;    //指向最后一个元素
} BlockQueue;

int InitQueue(BlockQueue *&bq)
{
    bq = (BlockQueue *)malloc(sizeof(BlockQueue));
    bq->front = bq->rear = -1;
    return 0;
}

bool is_empty_queue(BlockQueue bq)
{
    if(q->front == q->rear)
        return true;
    return false;
}

int dequeue(BlockQueue *q, Block &blk)
{
    if(!is_empty_queue(q))
        blk = q->data[q->front];
        q->front += 1;
        return 0;
    else
        return 1
}

int enqueue(BlockQueue q, Block blk)
{
    if(q->rear == MaxSize-1)
        return 1;
    else
    {
        q->rear += 1;
        q->data[q->rear] = blk;
        return 0;
    }
    
}

int destroy_queue(BlockQueue *q)
{
    free(q);
    return 0;
}

int main()
{
    
    return 0;
}
