from app.binary_tree import BNode


def test_insert_nodes():
    tree = BNode(2)
    tree.insert(BNode(1))
    tree.insert(BNode(3))

    assert tree.left.val == 1
    assert tree.right.val == 3


def test_preorder_traversal(capfd):
    tree = BNode(10)
    tree.insert(BNode(2))
    tree.insert(BNode(12))
    tree.insert(BNode(1))
    tree.insert(BNode(11))
    tree.insert(BNode(4))

    print(tree)
    out, err = capfd.readouterr()
    assert out == '10 2 1 4 12 11 \n'
