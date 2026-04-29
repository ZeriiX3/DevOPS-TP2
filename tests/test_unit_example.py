from app import normalize_item_name


def test_normalize_item_name_removes_spaces():
    assert normalize_item_name("  hello  ") == "hello"