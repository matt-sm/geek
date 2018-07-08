from app.hash_table import HashTable


def test_get_set():
    ht = HashTable()
    ht.set('test', 1)
    assert ht.get('test') == 1
    assert ht.get('invalid') is None
