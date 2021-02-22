import random

from abstract_distribution_generator import AbstractDistributionGenerator


class PopulationSampleDistributionGenerator(AbstractDistributionGenerator):
    DEFAULT_POPULATION_SAMPLING_SIZE = 10

    def __init__(self, population: list[float],
                 population_sampling_size: int = DEFAULT_POPULATION_SAMPLING_SIZE):
        self.validate_population(population)
        self.validate_population_sampling_size(population_sampling_size, len(population))
        self.population = population
        self.population_sampling_size = population_sampling_size

    @staticmethod
    def validate_population(population):
        if type(population) != list:
            raise TypeError
        if not all(AbstractDistributionGenerator.is_valid_distribution_parameter_type(member) for member in population):
            raise TypeError

    @staticmethod
    def validate_population_sampling_size(population_sampling_size, population_size):
        if type(population_sampling_size) != int:
            raise TypeError
        if population_sampling_size <= 0:
            raise PopulationSampleDistributionGenerator.NonPositivePopulationSamplingSizeError
        if population_sampling_size > population_size:
            raise PopulationSampleDistributionGenerator.PopulationSamplingSizeLargerThanPopulationSizeError

    def sample(self, sample_size: int) -> list[float]:
        self.validate_sample_size(sample_size)
        return [sum(random.sample(self.population, self.population_sampling_size))
                / self.population_sampling_size for _ in range(sample_size)]

    class NonPositivePopulationSamplingSizeError(Exception):
        def __str__(self):
            return 'Population-sampling distribution generation requires population sample size > 0'

    class PopulationSamplingSizeLargerThanPopulationSizeError(Exception):
        def __str__(self):
            return 'Population-sampling distribution generation requires population sample size <= population size'
