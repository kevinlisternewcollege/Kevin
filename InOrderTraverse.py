#in order transverse of tree
output =[] # we set this list to collect the data from the tree

def inorderTraverse (p):

    print("p=",p)

    if tree[p][0] != -1:
        print("loop 1","p=",p,tree[p][0])
        inorderTraverse(tree[p][0])  # note the use of the double indexing and the function recursively calling itself
    else:
        print(p,tree[p][1])
        output.append(tree[p][1])
    if tree[p][2] != -1:
        print("loop 2","p=",p,tree[p][2])
        output.append(tree[p][1])   # this function is missing from the pseudo code
        inorderTraverse(tree[p][2]) # note the use of the double indexing and the function recursively calling itself

# code starts here:
tree = [(1,"+",2), (3,"*",4), (5,"/",6),(-1,"a",-1),(-1,"b",-1),(-1,"c",-1),(-1,"d",-1)] # the tuple must be parenthesized, otherwise an error is raised

inorderTraverse(0)
print ("output",output)
