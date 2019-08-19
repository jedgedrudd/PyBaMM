#
# Test isothermal submodel
#

import pybamm
import tests
import unittest


class TestIsothermal(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.standard_parameters_lithium_ion
        i_boundary_cc = pybamm.PrimaryBroadcast(pybamm.Scalar(1), ["current collector"])
        variables = {"Current collector current density": i_boundary_cc}

        submodel = pybamm.thermal.current_collector.Isothermal2D(param)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        submodel = pybamm.thermal.current_collector.Isothermal3D(param)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
