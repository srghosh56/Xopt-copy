from typing import Dict, List

import torch
from botorch.acquisition.objective import MCAcquisitionObjective
from botorch.models.transforms.input import InputTransform
from botorch.models.transforms.outcome import OutcomeTransform
from botorch.sampling import MCSampler, SobolQMCNormalSampler
from pydantic import BaseModel, Field

from xopt.generator import GeneratorOptions


class AcqOptions(BaseModel):
    """Options for defining the acquisition function in BO"""

    # monte carlo options
    monte_carlo_samples = Field(512, description="number of monte carlo samples to use")

    proximal_lengthscales: List[float] = Field(
        None, description="lengthscales for proximal biasing"
    )

class OptimOptions(BaseModel):
    """Options for optimizing the acquisition function in BO"""

    num_restarts: int = Field(
        5, description="number of restarts during acquistion " "function optimization"
    )
    raw_samples: int = Field(
        20, description="number of raw samples used to seed optimization"
    )
    sequential: bool = Field(
        True,
        description="flag to use sequential optimization for q-batch point "
        "selection",
    )


class ModelOptions(BaseModel):
    """Options for defining the GP model in BO"""

    # input_transform: InputTransform = Field(
    #    None, description="transform applied to GP input model data", exclude=True
    # )
    # outcome_transform: OutcomeTransform = Field(
    #    None, description="transform applied to GP outcome model data", exclude=True
    # )

    # class Config:
    #    arbitrary_types_allowed = True


class BayesianOptions(GeneratorOptions):
    optim: OptimOptions = OptimOptions()
    acq: AcqOptions = AcqOptions()
    model: ModelOptions = ModelOptions()

    n_initial: int = Field(
        3, description="number of random initial points to measure during first step"
    )



if __name__ == "__main__":
    options = BayesianOptions()
    options.optim.raw_samples = 30
    print(options.dict())

    print(BayesianOptions.schema())
