use std::cmp::max;
use std::collections::VecDeque;

#[derive(Debug)]
struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Node {
    fn new(value: i32) -> Self {
        Self {
            value,
            left: None,
            right: None,
        }
    }
}

struct BST {
    root: Option<Box<Node>>,
}

impl BST {
    fn new() -> Self {
        Self { root: None }
    }

    fn insert(&mut self, value: i32) {
        self.root = Self::insert_rec(self.root.take(), value);
    }

    fn insert_rec(node: Option<Box<Node>>, value: i32) -> Option<Box<Node>> {
        match node {
            Some(mut n) => {
                if value < n.value {
                    n.left = Self::insert_rec(n.left, value);
                } else if value > n.value {
                    n.right = Self::insert_rec(n.right, value);
                }
                Some(n)
            }
            None => Some(Box::new(Node::new(value))),
        }
    }

    fn search(&self, value: i32) -> bool {
        Self::search_rec(&self.root, value)
    }

    fn search_rec(node: &Option<Box<Node>>, value: i32) -> bool {
        match node {
            Some(n) => {
                if value == n.value {
                    true
                } else if value < n.value {
                    Self::search_rec(&n.left, value)
                } else {
                    Self::search_rec(&n.right, value)
                }
            }
            None => false,
        }
    }

    fn height(&self) -> i32 {
        Self::height_rec(&self.root)
    }

    fn height_rec(node: &Option<Box<Node>>) -> i32 {
        match node {
            Some(n) => 1 + max(Self::height_rec(&n.left), Self::height_rec(&n.right)),
            None => 0,
        }
    }

    fn inorder(&self) {
        Self::inorder_rec(&self.root);
        println!();
    }

    fn inorder_rec(node: &Option<Box<Node>>) {
        if let Some(n) = node {
            Self::inorder_rec(&n.left);
            print!("{} ", n.value);
            Self::inorder_rec(&n.right);
        }
    }
}

fn main() {
    let mut tree = BST::new();
    let values = [50, 30, 70, 20, 40, 60, 80];

    for v in values {
        tree.insert(v);
    }

    println!("Inorder:");
    tree.inorder();
    println!("Height: {}", tree.height());
    println!("Search 40: {}", tree.search(40));
}
