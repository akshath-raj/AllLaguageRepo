class Node {
    var value: Int
    var left: Node?
    var right: Node?

    init(_ value: Int) {
        self.value = value
    }
}

class BST {
    var root: Node?

    func insert(_ value: Int) {
        root = insertRec(root, value)
    }

    private func insertRec(_ node: Node?, _ value: Int) -> Node {
        guard let node = node else {
            return Node(value)
        }
        if value < node.value {
            node.left = insertRec(node.left, value)
        } else if value > node.value {
            node.right = insertRec(node.right, value)
        }
        return node
    }

    func inorder(_ node: Node?) {
        guard let node = node else { return }
        inorder(node.left)
        print(node.value, terminator: " ")
        inorder(node.right)
    }
}

let tree = BST()
[50,30,70,20,40,60,80].forEach { tree.insert($0) }
tree.inorder(tree.root)
