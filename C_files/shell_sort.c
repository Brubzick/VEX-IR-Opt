
int main(int arr[],int len)
{	//本质上也是一种插入排序，避免了大量数据的移动，在每一组排序过后，每个数据已经到了大致的位置。
	int i,j;
	int step=0;
	for(step = len/2;step>=1;step=step/2)
    {	//分组  分为step组,对每组的元素进行插入排序
		for(i=step;i<len;i++)
        {
			int key = arr[i];
			for(j=i-step;j>=0&&arr[j]>key;j=j-step)
            {
				arr[j+step] = arr[j];	
			}	
			arr[j+step] = key;
		}
	}
}
