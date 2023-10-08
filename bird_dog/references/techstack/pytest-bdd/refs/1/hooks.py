import pytest

@pytest.hookimpl
def pytest_bdd_before_scenario(request, feature, scenario):
    if feature.name == 'Shopping Cart':
        print("Before scenario:", scenario.name)

@pytest.hookimpl
def pytest_bdd_after_scenario(request, feature, scenario, result):
    if feature.name == 'Shopping Cart':
        print("After scenario:", scenario.name)

@pytest.hookimpl
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    if feature.name == 'Shopping Cart':
        print("Before step:", step.name)

@pytest.hookimpl
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    if feature.name == 'Shopping Cart':
        print("After step:", step.name)
