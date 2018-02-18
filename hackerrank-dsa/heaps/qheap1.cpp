// qheap1.cpp at hackerrank.com data structures
// rohan kumar oddlypoetic.com

#include <iostream>
#include <set>
using namespace std;

int main() 
{
	int queries;
	
	cin >> queries;
	
	set<int> heap;
	
	for (int i = 0; i < queries; i++) {
		
		int ops, value;
		
		cin >> ops;
		
		switch(ops) {
			case 1: 
				cin >> value;
				heap.insert(value);
				break;
			case 2: 
				cin >> value;
				heap.erase(heap.find(value));
				break;
			case 3: 
				cout << *heap.begin() << endl;
				break;
		}
	}
	return 0;
}

//this works, I'm looking for a pure Cpp solution.
/*
#include <iostream>
#include <cimits>
using namespace std;

void swap (int *x, int *y);

class MinHeap
{
	int *harr;
	int capacity;
	int heap_size;
	
    public:
	MinHeap(int capacity);
	
	void parent(int i) {
		return (i - 1) / 2;
	}
	
	int left(int i) {
		return (2 * i + 1); 
	}
	
	int right(int i) {
		return (2 * i + 2);
	}
	
	int extractMin();
	
	void decreaseKey(int i, int new_val);
	
	int getMin() {
		return harr[0];
	}
	
	void deleterKey(int i);
	
	void insertKey(int k);
};	
		
//Constructor: Build a heap from a given array ll of given size
MinHeap::MinHeap(int cap)
{
	heap_size = 0;
	capacity = cap;
	harr = new int[cap];
}

//insert new key 'k'
void MinHeap::insertKey(int k)
{
	if (heap_size == capacity) {
		cout << "\n Overflow: Could not insertKey\n";
		return;
	}
	
	//first insert the new key 
	heap_size++;
	int i = heap_size - 1;
	harr[i] = k;
	
	while (i != 0 && harr[parent(i)] > harr[i]) {
		swap(&harr[i], &harr[parent(i)]);
		i = parent(i);
	}
}

//decrease value of key at index 'i' to new_val.
void MinHeap::decreaseKey(int i, int new_val)
{
	harr[i] = new_val;
	while (i != 0 && harr[parent(i)] > harr[i])
	{
		swap(&harr[i], &harr[parent(i)]);
		i = parent(i);
	}
}

//remove minimum element (or root from min heap
int MinHeap::extractMin()
{
	if (heap_size <= 0) 
		return INT_MAX;
	if (heap_size == 0) {
		heap_size--;
		return harr[0];
	}
	
	int root = harr[0];
	harr[0] =harr[heap_size - 1];
	heap_size--;
	MinHeapify(0);
	
	return root;
}

//deletes key at index i.
//reduce val to infinite, then calls extractMin()
void MinHeap::deleteKey(int i)
{
	decreaseKey(i, INT_MIN);
	extractMin();
}

//recursive method to heapity subtree with root at given index
//this method assumes that the subtrees are already heapified
void MinHeap::MinHeapify(int i)
{
	int l = left(i);
	int r = right(i);
	int smallest = i;
	if (l < heap_size && harr[l] < harr[i])
		smallest = l;
	if (r < heap_size && harr[r] < harr[smallest])
		smallest = r;
	if (smallest != i)
	{
		swap(&harr[i], &harr[smalest]);
		Minheapify(smallest);
	}
}

//swap function
void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y; 
	*y = temp;
}

//driver program
int main()
{
	MinHeap heap(11);
	heap.insertKey(3);
	heap.insertKey(2);
	heap.deleteKey(1);
	heap.insertKey(16);
	heap.insertKey(4);
	heap.insertKey(55);
	heap.insertKey(15);
	heap.insertKey(5);
	cout << heap.extractMin() << " ";
	cout << heap.getMin() << " ";
	heap.decreaseKey(2, 1);
	cout << heap.getMin();
	return 0;
}
*/

