from abc import ABC

from abstract_distribution_generator import AbstractDistributionGenerator


class AbstractExponentialDistributionGenerator(AbstractDistributionGenerator, ABC):
    """Abstract class for implementation of an exponential distribution generator
    Has a static method validate_alpha which raises if alpha is not as an exponential distribution parameter"""

    @staticmethod
    def validate_alpha(alpha) -> None:
        if not AbstractExponentialDistributionGenerator.is_valid_distribution_parameter_type(alpha):
            raise TypeError
        if alpha <= 0:
            raise AbstractExponentialDistributionGenerator.NonPositiveExponentialAlphaError

    class NonPositiveExponentialAlphaError(Exception):

        def __str__(self):
            return 'Exponential distribution generation requires alpha > 0'


if __name__ == '__main__':
    try:
        AbstractExponentialDistributionGenerator.validate_alpha(-5)
    except Exception as e:
        print(e)
