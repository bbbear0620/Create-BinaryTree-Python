
def createBiTree(alist):
    maxnum = len(alist)-1
    ss = []
    root = TreeNode(alist[0])
    ss.append(root)
    for i,element in enumerate(alist):
        if not element == 'null':
            current_node = ss.pop(0)
            #print(current_node.val)
            if 2*i+1>maxnum or alist[2*i+1]=='null':
                current_node.left = None
            else:
                current_node.left = TreeNode(alist[2*i+1])
                ss.append(current_node.left)
                #print('this node\'s left:',current_node.left.val)
            if 2*i+2>maxnum or alist[2*i+2]=='null':
                current_node.right = None
            else:
                current_node.right = TreeNode(alist[2*i+2])
                ss.append(current_node.right)
                #print('this node\'s right:',current_node.right.val)
    return root
