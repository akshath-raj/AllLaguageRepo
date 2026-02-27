package main

import "fmt"

type Node struct {
	value int
	left  *Node
	right *Node
}

type BST struct {
	root *Node
}

func (t *BST) Insert(value int) {
	t.root = insertRec(t.root, value)
}

func insertRec(node *Node, value int) *Node {
	if node == nil {
		return &Node{value: value}
	}
	if value < node.value {
		node.left = insertRec(node.left, value)
	} else if value > node.value {
		node.right = insertRec(node.right, value)
	}
	return node
}

func inorder(node *Node) {
	if node == nil {
		return
	}
	inorder(node.left)
	fmt.Print(node.value, " ")
	inorder(node.right)
}

func main() {
	tree := BST{}
	values := []int{50, 30, 70, 20, 40, 60, 80}

	for _, v := range values {
		tree.Insert(v)
	}

	fmt.Println("Inorder:")
	inorder(tree.root)
}
