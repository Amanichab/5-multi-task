import os
import warnings
from utils import set_seeds, measure_uniformity_A, measure_uniformity_B
import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.core.observation import ObservationFeatures
from ax.modelbridge.generation_strategy import GenerationStep, GenerationStrategy
from ax.modelbridge.registry import Models
from ax.modelbridge.transforms.task_encode import TaskEncode
from ax.modelbridge.transforms.unit_x import UnitX

import pytest


@pytest.fixture(scope="session")
def get_namespace():
    script_fname = "MTBO_assignment_ans.py"
    script_content = open(script_fname).read()

    namespace = {}
    exec(script_content, namespace)
    return namespace


def test_task_a(get_namespace):

    running_ax_client = get_namespace["ax_client"]

    assert (
        len(running_ax_client.experiment.parameters) == 4
    ), "Incorrect number of parameters, expected 4"

    assert list(running_ax_client.experiment.parameters.keys()) == [
        "Temperature",
        "Pressure",
        "Gas_Flow",
        "Task",
    ], "Incorrect parameter names, expected ['Temperature', 'Pressure', 'Gas_Flow', 'Task']"

    assert running_ax_client.experiment.parameters[
        "Task"
    ].is_task, "Task parameter needs 'is_task' set to True"


def test_task_b(get_namespace):

    running_ax_client = get_namespace["ax_client"]

    running_df = running_ax_client.get_trials_data_frame()
    assert len(running_df) == 40, "Incorrect number of trials, expected 40"

    assert (
        running_df["Task"].value_counts().iloc[0] == 20
    ), "Incorrect number of Task A trials, expected 20"
    assert (
        running_df["Task"].value_counts().iloc[1] == 20
    ), "Incorrect number of Task B trials, expected 20"


def test_task_c(get_namespace):

    user_uniformity_A = get_namespace["uniformity_A"]
    user_uniformity_B = get_namespace["uniformity_B"]

    assert (
        user_uniformity_A >= 0.95
    ), "Incorrect optimal uniformity for reactor A, expected >= 0.95"
    assert (
        user_uniformity_B >= 0.93
    ), "Incorrect optimal uniformity for reactor B, expected >= 0.93"


def test_task_d(get_namespace):

    running_ax_client = get_namespace["ax_client"]

    user_best_reactor = get_namespace["best_reactor"]
    user_temp_diff = get_namespace["temp_diff"]
    user_pressure_diff = get_namespace["pressure_diff"]

    assert user_best_reactor == "A", "Incorrect best reactor, expected A"
    assert user_temp_diff >= 50, "Incorrect temperature difference, expected >= 50"
    assert user_pressure_diff >= 24, "Incorrect pressure difference, expected >= 24"


def test_task_e(get_namespace):

    running_ax_client = get_namespace["ax_client"]

    user_num_iterations_single = get_namespace["num_iterations_single"]
    user_higher_or_lower = get_namespace["higher_or_lower"]

    assert (
        user_num_iterations_single > 20
    ), "Incorrect number of iterations, expected < 20"
    assert user_higher_or_lower == "higher", "Incorrect comparison, expected higher"
