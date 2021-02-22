from random import normalvariate

from abstract_normal_distribution_generator import AbstractNormalDistributionGenerator


class PythonNormalDistributionGenerator(AbstractNormalDistributionGenerator):
    """Normal distribution generator using python's built-in random.normalvariate"""

    DEFAULT_MEAN = 0.0
    DEFAULT_STD_DEVIATION = 1.0

    def __init__(self, mean: float = DEFAULT_MEAN,
                 std_deviation: float = DEFAULT_STD_DEVIATION) -> None:
        self.validate_parameters(mean, std_deviation)
        self.mean: float = mean
        self.std_deviation: float = std_deviation

    def sample(self, sample_size: int) -> list[float]:
        self.validate_sample_size(sample_size)
        return [normalvariate(self.mean, self.std_deviation) for _ in range(sample_size)]
