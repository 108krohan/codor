"""gordon's beverage at codeagon at hackerrank.com
"""
trees = int(raw_input())
bottom_right_back = [map(int, raw_input().split()) for i in range(trees)]
top_left_front = [[ i - 3 for i in bottom_right_back[j]] for j in range(trees)]
##for index in range(trees) :
####    print ' '.join([str(i) for i in top_left_front[index]]) + "|" + \
####          ' '.join([str(i) for i in bottom_right_back[index]])
##    print bottom_right_back[index]
queries = int(raw_input())
for _ in range(queries) :
    cords = map(int, raw_input().split())
    top_corner = [i for i in cords[:3]]
##    print 'top_corner', top_corner
    bottom_corner = [i for i in cords[3:]]
##    print 'bottom_corner', bottom_corner
    result = 0
    for j in range(trees) :
        init = 0
##        print 'top_left =', top_left_front[j],
##        print 'bottom_right =', bottom_right_back[j]
        for i in range(3) :
            if top_corner[i] <= top_left_front[j][i] <= bottom_corner[i] and \
               top_corner[i] <= bottom_right_back[j][i] <= bottom_corner[i] :
                init += 1
##        print 'init =', init
        if init == 3 :
            result += 1
    print result 

"""

Problem Statement


Mr Gordon likes making beverages. Mr Gordon is very rich, so he has a farm in space. His farm is divided into sections wich are cubes of size 1*1*1. There are N fields of different fruit trees. Each field of trees is located in a big cube of size 4*4*4, with bottom-right-back corner at (Xf,Yf,Zf).
 Mr Gordon wonders how many different fruit trees are completely contained in the big cube with top-left-front corner at (X1,Y1,Z1) and bottom-right-back corner at (X2,Y2,Z2) .

Help him with that.

Input format 
 The first line contains the number of fruit trees, N. 
 Next N lines contains 3 integers each: Xfi,Yfi,Zfi, coordinates of fruit field's bottom-right-back corner. 
 Next line contains number of Mr Gordon requests M. 
 Next M lines contains 6 integers each: X1i,Y1i,Z1i,X2i,Y2i,Z2i, coordinates of two opposite corners of big cube. 

Output Format You have to print M lines where the I-th line contains one integer, answer for the I-th request.

Constraints 
1≤N,M≤105 
0≤|X|,|Y|,|Z|≤100 
X1i<X2i 
Y1i<Y2i 
Z1i<Z2i 

Sample Input 
7
4 4 4
7 7 7
4 7 4
7 4 7
7 7 4
4 4 7
-4 -4 -4
4
-8 -8 -8 8 8 8
0 0 0 7 7 5
3 7 3 10 10 10
3 2 0 8 8 6


Sample Output 
7
3
0
1



Explanation


Here are the top-left-front and bottom-right-back coordinates of all the fruit fields:
1. (1, 1, 1) (4, 4, 4)
2. (4, 4, 4) (7, 7, 7)
3. (1, 4, 1) (4, 7, 4)
4. (4, 1, 4) (7, 4, 7)
5. (4, 4, 1) (7, 7, 4)
6. (1, 1, 4) (4, 4, 7)
7. (-7, -7, -7) (-4, -4, -4)


•For query (-8, -8, -8) (8, 8, 8), all fruit fields are inside it. 


•For query (0, 0, 0) (7, 7, 5), the 1st, 3rd, 5th fruit fields are inside it. 


•For query (3, 7, 3) (10, 10, 10), no field is inside it, because every top-left-front vertex is outside of the query cube.


•For query (3, 2, 0) (8, 8, 6), the 5th fruit field is inside it. 


"""
