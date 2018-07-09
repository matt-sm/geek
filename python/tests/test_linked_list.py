from app.linked_list import Node


def test_add_nodes(capfd):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    node1.traverse()
    out, err = capfd.readouterr()
    assert out == '1\n2\n3\n'


def test_delete_node(capfd):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    node1.delete(node2)
    node1.traverse()
    out, err = capfd.readouterr()
    assert out == '1\n3\n'

    node1.delete(node3)
    node1.traverse()
    out, err = capfd.readouterr()
    assert out == '1\n'


def test_kth_from_last():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    assert node1.kth_from_last(2) == node4
    assert node1.kth_from_last(1) == node5
    assert node1.kth_from_last(5) == node1
