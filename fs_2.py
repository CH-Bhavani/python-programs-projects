'''Kiran Rao purchased two boxes (Box1,Box2) of unique weights of gold coins, where first box weights are subset of second box gold weights.

 Now design a method for Gumadi Baleshwar Rao to find all the next largest weights 
of Box1 gold coins in the corresponding locations of box2 , 
if doesn’t exist return -1.

The Next largest Weight is Weight ‘W’ in Box1 is the first largest weight 
 to its right side weight in Box2.

NOTE: Unique weights means, no two coins will have same weight.

 Input Format:
 -------------
Line-1: space separated integers, weihts of gold coins in the first box.
Line-2: space separated integers, weihts of gold coins in the second box.

Output Format:
--------------
 Print a list of integers, next largest weights

Sample Input-1:
---------------
 4 3 2
 1 3 4 2

Sample Output-1:
 ----------------
 [-1, 4, -1]


 Sample Input-2:
 ---------------
5 6 3 4
1 5 3 7 8 6 4 2

 Sample Output-2:
 ----------------
[7, -1, 7, -1]
 '''


def next_max(arr1,arr2):
    l=[]
    for i in arr1:
        flag=0
        if i not in arr2:
            l.append(-1)
        else:
            ind=arr2.index(i)
            for j in range(ind+1,len(arr2)):
                if arr2[j]>i:
                    l.append(arr2[j])
                    flag=1;
                    break;
            if flag==0:
                l.append(-1)
    return l
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(next_max(arr1,arr2))

       
    
