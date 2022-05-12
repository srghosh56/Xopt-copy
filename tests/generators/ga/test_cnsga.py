
from xopt.generators.ga.cnsga import CNSGAGenerator
from xopt.resources.test_functions.tnk import evaluate_TNK, tnk_vocs
from xopt import Xopt, Evaluator
from xopt.resources.testing import TEST_YAML

def test_cnsga():
    X = Xopt(
        generator=CNSGAGenerator(tnk_vocs),
        evaluator=Evaluator(evaluate_TNK),
        vocs=tnk_vocs,
    )
    X.options.max_evaluations = 100
    X.run()



def test_cnsga_from_yaml():  
    X = Xopt(TEST_YAML)
    # Patch in generator
    X._generator = CNSGAGenerator(X.vocs)
    X.options.max_evaluations = 100
    X.run()
    assert len(X.data) == 100
    assert all(X.data["xopt_error"] == False)  