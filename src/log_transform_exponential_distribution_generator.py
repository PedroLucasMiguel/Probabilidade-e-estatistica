from math import log

from abstract_exponential_distribution_generator import AbstractExponentialDistributionGenerator
from python_uniform_distribution_generator import PythonUniformDistributionGenerator


class LogTransformExponentialDistributionGenerator(AbstractExponentialDistributionGenerator):
    """Exponential distribution generator using logarithmic transformation of a uniform distribution"""

    DEFAULT_ALPHA = 1.0

    def __init__(self, alpha: float = DEFAULT_ALPHA) -> None:
        self.validate_alpha(alpha)
        self.alpha: float = alpha

    def sample(self, sample_size: int) -> list[float]:
        self.validate_sample_size(sample_size)
        uniform_sample = PythonUniformDistributionGenerator().sample(sample_size)
        return [-log(1 - x) / self.alpha for x in uniform_sample]
