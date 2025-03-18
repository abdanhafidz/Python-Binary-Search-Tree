def new_bst(key = 0):
    return {'key': key, 'left': None, 'right': None}

def insert(tree, key):
    if tree is None:
        return {'key': key, 'left': None, 'right': None}
    if key < tree['key']:
        tree['left'] = insert(tree['left'], key)
    else:
        tree['right'] = insert(tree['right'], key)
    return tree


def search(tree, key):
    if tree is None or tree['key'] == key:
        return tree is not None
    if key < tree['key']:
        return search(tree['left'], key)
    return search(tree['right'], key)


def inorder_traversal(tree):
    if tree is None:
        return []
    return inorder_traversal(tree['left']) + [tree['key']] + inorder_traversal(tree['right'])
def preorder_traversal(tree):
    if tree is None:
        return []
    return [tree['key']] + preorder_traversal(tree['left']) + preorder_traversal(tree['right'])

def postorder_traversal(tree):
    if tree is None:
        return []
    return postorder_traversal(tree['left']) + postorder_traversal(tree['right']) + [tree['key']]

def delete(tree, key):
    if tree is None:
        return tree
    if key < tree['key']:
        tree['left'] = delete(tree['left'], key)
    elif key > tree['key']:
        tree['right'] = delete(tree['right'], key)
    else:
        if tree['left'] is None:
            return tree['right']
        elif tree['right'] is None:
            return tree['left']
        min_larger_node = tree['right']
        while min_larger_node['left'] is not None:
            min_larger_node = min_larger_node['left']
        tree['key'] = min_larger_node['key']
        tree['right'] = delete(tree['right'], min_larger_node['key'])
    return tree
