using System;

class Node {
    public int Value;
    public Node Left, Right;

    public Node(int value) {
        Value = value;
    }
}

class BST {
    private Node root;

    public void Insert(int value) {
        root = InsertRec(root, value);
    }

    private Node InsertRec(Node node, int value) {
        if (node == null) return new Node(value);

        if (value < node.Value)
            node.Left = InsertRec(node.Left, value);
        else if (value > node.Value)
            node.Right = InsertRec(node.Right, value);

        return node;
    }

    public void Inorder() {
        InorderRec(root);
        Console.WriteLine();
    }

    private void InorderRec(Node node) {
        if (node == null) return;
        InorderRec(node.Left);
        Console.Write(node.Value + " ");
        InorderRec(node.Right);
    }

    static void Main() {
        BST tree = new BST();
        int[] values = {50,30,70,20,40,60,80};

        foreach (int v in values)
            tree.Insert(v);

        tree.Inorder();
    }
}
