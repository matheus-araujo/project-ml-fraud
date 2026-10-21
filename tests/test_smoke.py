import importlib 


def test_import():
    assert importlib.import_module("fraud_detection") is not None
    
