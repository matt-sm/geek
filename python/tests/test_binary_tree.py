from app.binary_tree import BNode


def test_insert_nodes():
    tree = BNode(2)
    tree.insert(BNode(1))
    tree.insert(BNode(3))

    assert tree.left.val == 1
    assert tree.right.val == 3
