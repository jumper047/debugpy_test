import pytest

@pytest.fixture(autouse=True)
def debug():
    import debugpy
    debugpy.listen(("0.0.0.0", 3000))
    debugpy.wait_for_client()
    debugpy.breakpoint()
    print("You shall [not] pass!")


def test_test():
    assert True
