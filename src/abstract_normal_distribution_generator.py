from abc import ABC

from abstract_distribution_generator import AbstractDistributionGenerator


class AbstractNormalDistributionGenerator(AbstractDistributionGenerator, ABC):
    """Abstract class for implementation of a normal distribution generator
    Has static methods which raise if values are not fit as normal distribution parameters"""

    @staticmethod
    def validate_parameters(mean, std_deviation):
        AbstractNormalDistributionGenerator.validate_mean(mean)
        AbstractNormalDistributionGenerator.validate_std_deviation(std_deviation)

    @staticmethod
    def validate_mean(mean):
        if not AbstractNormalDistributionGenerator.is_valid_distribution_parameter_type(mean):
            raise TypeError

    @staticmethod
    def validate_std_deviation(std_deviation):
        if not AbstractNormalDistributionGenerator.is_valid_distribution_parameter_type(std_deviation):
            raise TypeError
        if std_deviation < 0:
            raise AbstractNormalDistributionGenerator.NegativeNormalStandardDeviationError

    class NegativeNormalStandardDeviationError(Exception):

        def __str__(self):
            return 'Normal distribution generation requires standard deviation >= 0'
