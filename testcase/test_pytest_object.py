import logging

logging.basicConfig(level=logging.DEBUG)

def setup_module():
    logging.info("setup_module")

def teardown_module():
    logging.info("teardown_module")

class TestPytestObject2:
    def test_three(self):
        assert [1, 2] == [1, 2]

    def test_four(self):
        assert {"a":1, "b":"ss"} == {"a":1, "b":"ss"}

class TestPytestObject:
    @classmethod
    def setup_class(cls):
        logging.info("setup_class")

    def setup_method(self):
        logging.info("setup")

    def test_two(self):
        assert 1==1

    def test_one(self):
        assert True==True

    def teardown_method(self):
        logging.info("teardown")

    @classmethod
    def teardown_class(cls):
        logging.info("teardown_class")