from abc import ABC

from abstract_distribution_generator import AbstractDistributionGenerator


class AbstractUniformDistributionGenerator(AbstractDistributionGenerator, ABC):
    """Abstract class for implementation of an uniform distribution generator
    Has a static method validate_parameters which raises if values are not if as uniform distribution parameters"""

    @staticmethod
    def validate_parameters(interval_min, interval_max):
        if not AbstractUniformDistributionGenerator.is_valid_distribution_parameter_type(
                interval_min) or not AbstractUniformDistributionGenerator.is_valid_distribution_parameter_type(interval_max):
            raise TypeError
        if interval_min > interval_max:
            raise AbstractUniformDistributionGenerator.InvalidUniformIntervalBoundariesError

    class InvalidUniformIntervalBoundariesError(Exception):

        def __str__(self):
            return 'Uniform distribution generation requires interval minimum <= interval maximum'
