int main(int arr[],int len)
{
	int i,j;
	for(i=1;i<len;i++)
    {
		int key = arr[i]; //记录当前需要插入的数据
		for(j= i-1;i>=0&&arr[j]>key;j--)
        {	//找到插入的位置
			arr[j+1] = arr[j]; //把需要插入的元素后面的元素往后移
		}
		arr[j+1] = key;	//插入该元素
	}
}
