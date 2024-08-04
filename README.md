# 5. Multi-task BO: Optimizing Chemical Vapor Deposition Devices in Different Locations

Perform multi-task Bayesian optimization to maximize thin film uniformity for
two separate chemical vapor deposition reactors.

## The Assignment

Chemical vapor deposition (CVD) is a synthesis technique that can be used to produce
high quality thin films through the reaction or decomposition of gaseous precursors on
a substrate. A key challenge in CVD is to produce films with uniform thickness and
composition over large areas. Your company has recently purchased two CVD reactors
with the intent of depositing insulating films on integrated circuits. One reactor (A)
is located at the facility you work at, but the other reactor (B) has been installed
at a facility on the other side of the country. After performing some initial tests,
you have found that the two CVD recators produce films of differing uniformity for
the same set of process parameters. You have been tasked with optimizing the process
parameters of each reactor to produce films with the highest uniformity possible.

The parameters of interest along with the manufacturer recommended ranges are:

| Parameter   | Range    | Unit |
| ----------- | -------- | ---- |
| Temperature | 600-1100 | C    |
| Pressure    | 5-300    | Torr |
| Gas_Flow    | 10-700   | sccm |

Based on your experience, you believe that the two reactors are more similar than
different, and that there is likely some useful information to be gained by modeling
them with a multi-task Gaussian process. Your goal is to use Honegumi to develop an
optimization script to help you identify a set of parameters for each reactor that
maximizes the uniformity of the films produced. Your experimental budget is limited to
40 total experiments for both reactors. A set of synthetic objective functions have
been provided that will serve as proxies for real experimental measurements.

### **TASK A:** Use Honegumi to help populate the optimization parameters below.

As we will be using a multi-task model, we need to include a few special
transforms to ensure that the model can differentiate between the two reactors.
You will also need to define an additional "task parameter" that codifies which
reactor is being used.

An example of how to specify a task parameter is shown below:
```python
        {
            "name": "Task",
            "type": "choice",
            "values": ["Base", "Shifted"],
            "is_task": True,
            "target_value": "Base",
        },
```

### **TASK B:** Run the optimization campaign, alternating between the two reactors.

Run the optimization loop for 40 total experiments, but alternate which reactor
uniformity is measured at each iteration using the provided synthetic objective
functions.

### **TASK C:** Report the optimal parameters for each reactor and associated uniformity.

Identify the optimal parameters for each reactor and assign them to variables called
`optimal_parameters_A` and `optimal_parameters_B`. Also, assign the associated
uniformity values to variables called `uniformity_A` and `uniformity_B`.

### **TASK D:** How do the reactors compare with one another?

Determine which reactor achieved the highest uniformity and assign the name (A or B)
as a string to a variable called `best_reactor`. Next find the absolute difference in
the temperature and pressure parameters between the optimal parameters for the
reactors and assign them to variables called `temp_diff` and `pressure_diff`.

### **TASK E:** Was there an advantage to using a multi-task model?

Run a simple single task optimization campaign for reactor A and determine how many
iterations it would take to match or exceed the `uniformity_A` found using the
multi-task model. Assign the number of iterations to a variable called
`num_iterations_single`. Assume that it would have taken the same number of iterations
to optimize reactor B using a single task model. Is the total number of iterations
for the single task models higher or lower than the multi-task model budget of 40?
Assign the string "higher" or "lower" to a variable called `higher_or_lower`.

## Setup command

See `postCreateCommand` from [`devcontainer.json`](.devcontainer/devcontainer.json).

## Run command
`pytest`

## Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be inaccessible.
