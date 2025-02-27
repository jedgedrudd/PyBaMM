#
# Tests for the Parameter class
#
import pybamm

import unittest


class TestIndependentVariable(unittest.TestCase):
    def test_variable_init(self):
        a = pybamm.IndependentVariable("a")
        self.assertEqual(a.name, "a")
        self.assertEqual(a.domain, [])
        a = pybamm.IndependentVariable("a", domain=["test"])
        self.assertEqual(a.domain[0], "test")
        a = pybamm.IndependentVariable("a", domain="test")
        self.assertEqual(a.domain[0], "test")
        with self.assertRaises(TypeError):
            pybamm.IndependentVariable("a", domain=1)

    def test_time(self):
        t = pybamm.Time()
        self.assertEqual(t.name, "time")
        self.assertEqual(t.evaluate(4), 4)
        with self.assertRaises(ValueError):
            t.evaluate(None)

        t = pybamm.t
        self.assertEqual(t.name, "time")
        self.assertEqual(t.evaluate(4), 4)
        with self.assertRaises(ValueError):
            t.evaluate(None)

    def test_spatial_variable(self):
        x = pybamm.SpatialVariable("x", "negative electrode")
        self.assertEqual(x.name, "x")
        y = pybamm.SpatialVariable("y", "separator")
        self.assertEqual(y.name, "y")
        z = pybamm.SpatialVariable("z", "positive electrode")
        self.assertEqual(z.name, "z")
        r = pybamm.SpatialVariable("r", "negative particle")
        self.assertEqual(r.name, "r")
        with self.assertRaises(NotImplementedError):
            x.evaluate()

        with self.assertRaisesRegex(ValueError, "name must be"):
            pybamm.SpatialVariable("not a variable", ["negative electrode"])
        with self.assertRaisesRegex(ValueError, "domain must be"):
            pybamm.SpatialVariable("x", [])
        with self.assertRaises(pybamm.DomainError):
            pybamm.SpatialVariable("r", ["negative electrode"])
        with self.assertRaises(pybamm.DomainError):
            pybamm.SpatialVariable("r_n", ["positive particle"])
        with self.assertRaises(pybamm.DomainError):
            pybamm.SpatialVariable("r_p", ["negative particle"])
        with self.assertRaises(pybamm.DomainError):
            pybamm.SpatialVariable("x", ["negative particle"])


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
