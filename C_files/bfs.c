
#include <stdio.h>
#include <stdlib.h>
 
// 定义图的最大节点数
#define MAX_NODES 100
 
// 定义图的邻接表节点
struct Node {
    int data;
    struct Node* next;
};
 
// 定义图
struct Graph {
    int numNodes;
    struct Node* adjacencyList[MAX_NODES];
    int visited[MAX_NODES];
};
 
// 初始化图
void initGraph(struct Graph* graph, int numNodes) {
    graph->numNodes = numNodes;
    for (int i = 0; i < numNodes; ++i) {
        graph->adjacencyList[i] = NULL;
        graph->visited[i] = 0;
    }
}
 
// 添加边
void addEdge(struct Graph* graph, int src, int dest) {
    // 创建邻接表节点
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = dest;
    newNode->next = graph->adjacencyList[src];
    graph->adjacencyList[src] = newNode;
}
 
// 广度优先遍历
void BFS(struct Graph* graph, int startNode) {
    // 创建队列用于存储待访问节点
    int queue[MAX_NODES];
    int front = 0, rear = 0;
 
    // 将起始节点加入队列并标记为已访问
    queue[rear++] = startNode;
    graph->visited[startNode] = 1;
 
    // 开始遍历
    while (front < rear) {
        // 出队列
        int currentNode = queue[front++];
        printf("%d ", currentNode);
 
        // 遍历邻接节点
        struct Node* current = graph->adjacencyList[currentNode];
        while (current != NULL) {
            if (!graph->visited[current->data]) {
                // 将未访问的邻接节点加入队列并标记为已访问
                queue[rear++] = current->data;
                graph->visited[current->data] = 1;
            }
            current = current->next;
        }
    }
}
 
int main() {
    // 创建一个图并初始化
    struct Graph graph;
    initGraph(&graph, 6);
 
    // 添加图的边
    addEdge(&graph, 0, 1);
    addEdge(&graph, 0, 2);
    addEdge(&graph, 1, 3);
    addEdge(&graph, 2, 4);
    addEdge(&graph, 3, 5);
 
    // 执行广度优先遍历
    printf("Breadth-First Traversal: ");
    BFS(&graph, 0);
 
    return 0;
}