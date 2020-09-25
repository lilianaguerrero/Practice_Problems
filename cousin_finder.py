tree = [(1,4),(1,10),(10,20),(10,15),(4,7)]

def cousin_finder(tree,n1,n2):
    parent_child = {}
    for parent, child in tree:
        if parent not in parent_child:
            parent_child[parent] = [child]
        else:
            parent_child[parent].append(child)
    for ancestor in parent_child.keys():
        for parent, child in parent_child.items():
            if ancestor in child:
                parent_child[parent].append(parent_child[ancestor])
    print(parent_child)
    for ancestor in parent_child.keys():
        if n1 and n2 in parent_child[ancestor]:
            return ancestor
    return False

print(cousin_finder(tree,20,7))
