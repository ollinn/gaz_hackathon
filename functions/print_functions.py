def find_root(tree: dict):
    root = [name for name in tree.keys() if tree[name] is None].pop()
    return root


def find_branches(tree, element):
    return [name for name in tree.keys() if tree[name] == element]


def print_tree_element(element, tree, tab=''):
    print(tab, element)
    for branch in find_branches(tree, element):
        print_tree_element(branch, tree, tab + '    ')


def print_tree(tree: dict):
    print_tree_element(find_root(tree), tree)
