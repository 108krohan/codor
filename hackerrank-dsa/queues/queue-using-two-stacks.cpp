

/*Queue using two stacks hackerrank
Rohan Kumar oddlypoetic.com
*/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <deque>
#include <iostream>
#include <list>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define ll long long

#define MIN(a, b) a < b ? a : b
#define MAX(a, b) a > b ? a : b

using namespace std;

int readline(char *str) {
    int i = 0;
    char ch;
    while((ch = getchar()) != '\n') {
        str[i++] = ch;
    }
    str[i] = '\0';
    return i;
}

stack<int> s1;
stack<int> s2;
int front_val;

void enqueue(int x) {
    while(!s2.empty()) {
        s1.push(s2.top());
        s2.pop();
    }
    if(s1.empty()) {
        front_val = x;
    }
    s1.push(x);
}

int dequeue() {
    while(!s1.empty()) {
        s2.push(s1.top());
        s1.pop();
    }
    int x = s2.top();
    s2.pop();
    if(!s2.empty()) {
        front_val = s2.top();
    }
    return x;
}

int front() {
    return front_val;
}

int main(int argc, char *argv[]) {
    int t;
    scanf("%d", &t);
    while(t--) {
        int op;
        scanf("%d", &op);
        switch(op) {
            case 1:
                int x;
                scanf("%d", &x);
                enqueue(x);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                printf("%d\n", front());
                break;
        }

    }

    return 0;
}


/*

#include <stdio.h>
#include <iostream>
#include <stdlib.h>

using namespace std;

struct Node
{
	int data;
	struct Node * next;
};

void push(struct Node** top_ref, int new_data);
void pop(struct Node ** top_ref);
struct queue
{
	struct Node * stack1;
	struct Node * stack2;
};

void enQueue(struct queue * q, int x)
{
	push(&q->stack1, x);
}

int deQueue(struct queue * q)
{
	int x;
	/* If both stacks are empty then error */
	if (q->stack1 == NULL && q->stack2 == NULL) {
		cout << "Queue is empty";
		exit(0);
	}
	
	if (q->stack2 == NULL) {
		while(q->stack1 != NULL) {
			x = pop(&q->stack1);
			push(&q->stack2, x);
		}
	}
	
	x = pop(&q->stack2);
	return x;
}

void push(struct sNode** top_ref, int new_data)
{
	struct sNode* new_node = (struct sNode*) malloc(sizeof(struct sNode)); 
	if (new_node == NULL) {
		cout << "Stack overflow \n";
		exit(0);
	}
 
	new_node->data = new_data;
	new_node->next = (*top_ref);
 
	(*top_ref) = new_node;
}

int pop(struct Node ** top_ref)
{
	int res;
	struct Node * top;
	if (*top_ref == NULL) {
		cout << "Stack Overflow \n";
		exit(0);
	}
	else {
		top = *top_ref;
		res = top->data;
		*top_ref = top->next;
		free(top);
		return res;
	}
}

*/
