from unittest import TestCase
from src.calc import Calc
from ddt import ddt, data, unpack, file_data
import yaml

@ddt
class TestCalc(TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    @data(5)
    def test_demo(self, real):
        self.assertEqual(real, 5)

    @data((1, 1, 2),
          (1, 0, 1)
          )
    @unpack
    def test_add(self, a, b, c):
        self.assertEqual(self.calc.add(a, b), c)

    @file_data("calc.yaml")
    def test_div(self, a, b, c):
        self.assertEqual(self.calc.div(a, b), c)