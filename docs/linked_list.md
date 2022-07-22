# Linked List

## operations

### delete next node

```py
def delete_next(node):
    node.next = node.next.next
    return node
```

### insert node

```py
def insert_node(node, new_node):
    new_node.next = node.next
    node.next = new_node
    return node
```
