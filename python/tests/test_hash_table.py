import pytest
from app.hash_table import HashTable


def test_get_set():
    ht = HashTable()
    ht.set('test', 1)
    assert ht.get('test') == 1
    assert ht.get('invalid') is None


def test_invalid_key():
    ht = HashTable()
    with pytest.raises(ValueError):
        ht.set(None, 1)

    with pytest.raises(ValueError):
        ht.get(None)


def test_collisions():
    ht = HashTable(1)
    ht.set('test', 1)
    ht.set('test2', 2)
    assert ht.get('test') == 1
    assert ht.get('test2') == 2
    assert ht.get('test3') is None
