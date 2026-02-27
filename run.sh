#!/bin/bash

echo "Running BST demo..."

if [ -f "bst.go" ]; then
  go run bst.go
elif [ -f "BST.java" ]; then
  javac BST.java && java BST
else
  echo "No supported file found."
fi
