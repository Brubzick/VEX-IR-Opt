#include <stddef.h>

struct dpsNode{
    int data;
    struct dpsNode* pre;
};

int main(struct dpsNode* node){

    int dataList[100];

    int i = 0;
    while (node->pre != NULL){
        dataList[i] = node->data;
        node = node->pre;
    }
}