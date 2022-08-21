# 快排，时间复杂度：nlogn，空间复杂度：logN
class QuickSort:
    def partition(self,l,left,right):
        if right<=left:return
        mid = self.quick_sort(l,left,right)
        self.partition(l,left,mid-1)
        self.partition(l,mid+1,right)

    def quick_sort(self,l,left,right):
        x = l[right]
        i=left;j=right;k=left
        while k<=j:
            if l[k]>x:
                l[k],l[j]=l[j],l[k]
                j-=1;k-=1
            elif l[k]<x:
                l[i],l[k]=l[k],l[i]
                i+=1
            k+=1
        l[i]=x
        return i

# 归排，时间复杂度O(NlogN)，空间复杂度O(N)
class MergeSort:
    def partition(self,l,left,right):
        if right<=left:return [l[left]]
        mid = left+(right-left)//2
        ll = self.partition(l,left,mid)
        rl = self.partition(l,mid+1,right)
        return self.merge_sort(ll,rl)
    def merge_sort(self,l1,l2):
        i=0;j=0;help=[]
        while i<len(l1) and j<len(l2):
            if l1[i]<=l2[j]:
                help.append(l1[i])
                i+=1
            else:
                help.append(l2[j])
                j+=1
        if i<len(l1):
            help.extend(l1[i:])
        if j<len(l2):
            help.extend(l2[j:])
        return help

'''堆排序，当前节点下标为i，则左子节点为2*i+1 ，右子节点为2*i+2，父节点(i-1)//2,
1、heapinsert：每次新来数字，需要和父节点比较，更大的话交换位置；
2、heapify：建堆过程，默认情况是从index=0开始，但实际上可以从任何位置开始；
时间复杂度为O(NlogN)，空间复杂度为O(logN)
'''
class HeapqSort:
    def heapSort(self,l):
        if len(l)<2:return
        # 初始建堆方式，最大值放在最左端
        for i in range(len(l)):
            self.heapInsert(l,i)
        length=len(l)
        while length>0:
            # 每次建堆把最大值放在最后，并重新建立剩余的堆
            self.heapify(l,0,length)
            l[0],l[length-1] = l[length-1],l[0]
            length-=1
    def heapInsert(self,l,index):
        while index>0 and l[index]>l[(index-1)//2]:
            l[index],l[(index-1)//2]=l[(index-1)//2],l[index]
            index=(index-1)//2
    def heapify(self,l,index,heapSize):
        left = index*2+1
        while left<heapSize:
            # 左右子节点比较最大值，并记录下标
            largest = left+1 if left+1<heapSize and l[left+1]>l[left] else left
            # largest记录父节点和左右子节点中的最大值下标
            largest = index if l[index]>l[largest] else largest
            # 如果子节点和父节点相等，则退出循环
            if largest==index:break
            l[index],l[largest] = l[largest],l[index]
            index = largest
            left = index*2+1

l1=[1,4,5,2,7,3,11,8,2,6,4,7,9]
l2=[1,4,5,2,7,3,11,8,2,6,4,7,9]
l3=[1,4,5,2,7,3,11,8,2,6,4,7,9]
q = QuickSort().partition(l1,0,len(l1)-1)
p = MergeSort().partition(l2,0,len(l2)-1)
t = HeapqSort().heapSort(l3)
print(l1)
print(p)
print(l3)