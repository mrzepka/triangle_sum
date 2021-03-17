class Node:
    def __init__(self, value, index):
        self.value = value
        self.max_value = value
        self.index = index #So we can find children... I don't like it
        self.r_child = None
        self.l_child = None
        self.solved = False #to avoid double work with two parents

    def add_right_child(self, node):
        self.r_child = node

    def add_left_child(self, node):
        self.l_child = node

    def mark_visited(self):
        self.solved = True

def parse_file(file):
    triangle_text = open(file, "r")
    rows = []
    for line in triangle_text:
        line = line.rstrip()
        rows.append(line.split(' '))
    triangle_text.close()
    return rows

def initialize_tree(triangle):
    if triangle is []:
        return Node(0, 0)
    parent_nodes = [] #Array of nodes to add children too
    for row in triangle:
        new_nodes = []
        if len(row) == 1: #root node
            root = Node(int(row[0]), 0)
            parent_nodes.append(root)
            continue
        index = 0
        for i in row:
            curr_node = Node(int(i), index)
            index = index + 1
            new_nodes.append(curr_node)

        for node in parent_nodes:
            node.add_left_child(new_nodes[node.index])
            node.add_right_child(new_nodes[node.index + 1])
        parent_nodes = new_nodes
    return root

def find_max_value_of_children(node):
    if node.l_child is None and node.r_child is None:
        return node.max_value
    if node.solved: #two parents means that each node will be calculated twice
        return node.max_value
    l_max = find_max_value_of_children(node.l_child)
    r_max = find_max_value_of_children(node.r_child)
    max_of_children = l_max if l_max > r_max else r_max
    #print('max of children: ' + str(max_of_children)) #for testing recursion
    node.max_value = node.max_value + max_of_children
    node.mark_visited()
    return node.max_value

def main():
    triangle_rows = parse_file('triangle.txt')
    root = initialize_tree(triangle_rows)
    m_val = find_max_value_of_children(root)
    print(str(m_val))

main()