# ======================================================================================
# ASSIGNMENT 5: Optimizing CVD Devices in Different Locations

# Your goal is to use Honegumi to develop a multi-task optimization script to
# determine a set of parameters for each of two reactors that maximizes the
# uniformity of the films produced. Your experimental budget is limited to 40
# total experiments for both reactors. A set of synthetic objective functions
# have been provided that will serve as proxies for real experimental
# measurements. Refer to the README for specifics regarding each task.
# ======================================================================================

from utils import set_seeds, measure_uniformity_A, measure_uniformity_B

set_seeds()  # setting the random seed for reproducibility

# --------------------------------------------------------------------------------------
# TASK A: Use Honegumi to help populate the optimization parameters below.
# --------------------------------------------------------------------------------------

import numpy as np
from ax.core.observation import ObservationFeatures
from ax.modelbridge.factory import Generators
from ax.generation_strategy.generation_strategy import GenerationStep, GenerationStrategy
from ax.modelbridge.transforms.task_encode import TaskEncode
from ax.modelbridge.transforms.unit_x import UnitX
from ax.service.ax_client import AxClient, ObjectiveProperties

transforms = [TaskEncode, UnitX]

gs = GenerationStrategy(
    name="MultiTaskOp",
    steps=[
        GenerationStep(
            model=Generators.SOBOL,
            num_trials=10,
            model_kwargs={"deduplicate": True, "transforms": transforms},
        ),
        GenerationStep(
            model=Generators.BOTORCH_MODULAR,
            num_trials=-1,
            model_kwargs={"transforms": transforms},
        ),
    ],
)

ax_client = AxClient(generation_strategy=gs, random_seed=42)

ax_client.create_experiment(
    parameters= # TODO: Your Code Goes Here
    objectives={"Uniformity": ObjectiveProperties(minimize=False)},
)

# --------------------------------------------------------------------------------------
# TASK B: Run the optimization campaign, alternating between the two reactors.
# --------------------------------------------------------------------------------------

for i in range(40):
    parameterization, trial_index = ax_client.get_next_trial(
        fixed_features=ObservationFeatures({"Task": "A" if i % 2 else "B"})
    )

    # TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK C: Report the optimal parameters for each reactor and associated uniformity.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK D: How do the reactors compare with one another?
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK E: Was there an advantage to using a multi-task model?
# --------------------------------------------------------------------------------------

ax_client_single = AxClient()

gs = GenerationStrategy(
    name="MultiTaskOp",
    steps=[
        GenerationStep(
            model=Generators.SOBOL,
            num_trials=10,
        ),
        GenerationStep(
            model=Generators.BOTORCH_MODULAR,
            num_trials=-1,
        ),
    ],
)

# TODO: Your Code Goes Here
