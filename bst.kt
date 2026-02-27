class Node(var value: Int) {
    var left: Node? = null
    var right: Node? = null
}

class BST {
    var root: Node? = null

    fun insert(value: Int) {
        root = insertRec(root, value)
    }

    private fun insertRec(node: Node?, value: Int): Node {
        if (node == null) return Node(value)
        if (value < node.value)
            node.left = insertRec(node.left, value)
        else if (value > node.value)
            node.right = insertRec(node.right, value)
        return node
    }

    fun inorder(node: Node?) {
        if (node == null) return
        inorder(node.left)
        print("${node.value} ")
        inorder(node.right)
    }
}

fun main() {
    val tree = BST()
    val values = listOf(50,30,70,20,40,60,80)

    values.forEach { tree.insert(it) }

    tree.inorder(tree.root)
}
