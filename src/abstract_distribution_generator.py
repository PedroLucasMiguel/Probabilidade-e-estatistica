from abc import ABCMeta, abstractmethod


class AbstractDistributionGenerator(metaclass=ABCMeta):
    """Abstract class for implementation of any distribution generator, which will be called via method 'sample'
    Has static methods which raise if values are not fit as generic distribution parameters or samples sizes"""

    @abstractmethod
    def sample(self, sample_size: int) -> list[float]:
        pass

    @staticmethod
    def validate_sample_size(sample_size) -> None:
        if type(sample_size) != int:
            raise TypeError
        if sample_size < 0:
            raise AbstractDistributionGenerator.NegativeSampleSizeError

    VALID_DISTRIBUTION_PARAMETER_TYPES = (int, float)

    @staticmethod
    def is_valid_distribution_parameter_type(value):
        return type(value) in AbstractDistributionGenerator.VALID_DISTRIBUTION_PARAMETER_TYPES

    class NegativeSampleSizeError(Exception):

        def __str__(self):
            return 'Distribution generator sampling requires sample size >= 0'
