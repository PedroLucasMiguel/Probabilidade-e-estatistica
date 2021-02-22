from random import uniform

from abstract_uniform_distribution_generator import AbstractUniformDistributionGenerator


class PythonUniformDistributionGenerator(AbstractUniformDistributionGenerator):
    """Uniform distribution generator using python's built-in random.uniform"""

    def __init__(self, interval_min: float = 0.0, interval_max: float = 1.0) -> None:
        self.validate_parameters(interval_min, interval_max)
        self.min: float = interval_min
        self.max: float = interval_max

    def sample(self, sample_size: int) -> list[float]:
        self.validate_sample_size(sample_size)
        return [uniform(self.min, self.max) for _ in range(sample_size)]
