
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
 
// 深度优先遍历
void DFS(struct Graph* graph, int node) {
    // 标记当前节点为已访问
    graph->visited[node] = 1;
    printf("%d ", node);
 
    // 遍历当前节点的邻接节点
    struct Node* current = graph->adjacencyList[node];
    while (current != NULL) {
        if (!graph->visited[current->data]) {
            // 递归调用DFS
            DFS(graph, current->data);
        }
        current = current->next;
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
 
    // 执行深度优先遍历
    printf("Depth-First Traversal: ");
    DFS(&graph, 0);
 
    return 0;
}