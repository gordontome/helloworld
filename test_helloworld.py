def hello(prenom):
    return f"Hello {prenom}"

def test_hello():
    assert hello('Nicolas') == "Hello Nicolas"