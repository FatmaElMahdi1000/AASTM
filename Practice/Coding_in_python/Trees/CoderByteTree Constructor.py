import re #regex
def TreeConstructor(strArr):
    child_to_parent = {}
    parent_to_child = {}
    allNode = set()
    for pair in strArr:
        #nums will be a list of 2
        nums = re.findall(r"\d+", pair)
        if len(nums) < 2:
            continue
        child, parent = int(nums[0]), int(nums[1])
        allNode.add(child)
        allNode.add(parent)

        # Rule 1: A child can only have ONE parent
        if child in child_to_parent:
            return "false"
        else:
            child_to_parent[child] = parent
        if parent not in parent_to_child:
            parent_to_child[parent] = []
        parent_to_child[parent].append(child)
    # return parent_to_child ... this can generate the tree output: {2: [1, 7], 4: [2], 7: [5], 5: [9]}
    # Rule 2: A parent cannot have more than 2 children
    if len(parent_to_child[parent]) > 2:
        return "false"
    # Rule 3: Ensure there is exactly ONE root node
    root = [node for node in allNode if node not in child_to_parent]
    #this means only one root exists, and it has no other parent, it's not the child
    if len(root) == 1:
        return "true"
    else:
        return "false"

strArr =  ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]

print(TreeConstructor(strArr))