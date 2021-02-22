from functools import cache
from math import sqrt, floor, nan

from abstract_statistical_analyser import AbstractStatisticalAnalyser
from frequency_calculator import FrequencyCalculator


class PythonStatisticalAnalyser(AbstractStatisticalAnalyser):

    def __init__(self, data: list[float]):
        self.validate_data(data)
        self.data: list[float] = sorted(data)
        self.data_size: int = len(data)

    @cache
    def min(self) -> float:
        return self.data[0]

    @cache
    def max(self) -> float:
        return self.data[-1]

    @cache
    def mean(self) -> float:
        return sum(self.data) / self.data_size

    @cache
    def mode(self) -> tuple[float, float]:
        calc = FrequencyCalculator((self.data,))
        buckets, frequencies = calc.count_frequencies()
        max_frequency_index = frequencies.index(max(frequencies))
        return buckets[max_frequency_index], buckets[max_frequency_index + 1]

    @cache
    def median(self) -> float:
        return self.percentile(0.5)

    @cache
    def lower_quartile(self):
        return self.percentile(0.25)

    @cache
    def upper_quartile(self):
        return self.percentile(0.75)

    @cache
    def percentile(self, p: float):
        if p < 0 or p > 1:
            raise ValueError

        np = self.data_size * p
        k = floor(np)
        if np == k:
            return (self.data[k - 1] + self.data[k]) / 2
        else:
            return self.data[k]

    @cache
    def amplitude(self):
        return self.max() - self.min()

    @cache
    def average_deviation(self) -> float:
        total_deviation = sum([abs(value - self.mean()) for value in self.data])
        return total_deviation / self.data_size

    @cache
    def variance(self) -> float:
        return self.normalized_sum_of_to_the_nth_deviations(2)

    @cache
    def standard_deviation(self) -> float:
        return sqrt(self.variance())

    @cache
    def percentage_within_one_std_dev(self):
        return self.proportion_within_n_std_dev(1) * 100

    @cache
    def percentage_within_two_std_dev(self):
        return self.proportion_within_n_std_dev(2) * 100

    @cache
    def percentage_within_three_std_dev(self):
        return self.proportion_within_n_std_dev(3) * 100

    def proportion_within_n_std_dev(self, n):
        mean = self.mean()
        std_dev = self.standard_deviation()
        return self.proportion_within_interval((mean - n * std_dev, mean + n * std_dev))

    @staticmethod
    def value_in_interval(value, interval):
        return interval[0] <= value <= interval[1]

    @cache
    def interquartile_range(self):
        return self.upper_quartile() - self.lower_quartile()

    @cache
    def percentage_of_outliers(self):
        return 100 - self.proportion_within_interval((self.lower_quartile() - 1.5 * self.interquartile_range(),
                                                      self.upper_quartile() + 1.5 * self.interquartile_range())) * 100

    def proportion_within_interval(self, interval):
        within_interval_count = 0
        for value in self.data:
            if self.value_in_interval(value, interval):
                within_interval_count += 1
        return within_interval_count / self.data_size

    @cache
    def coefficient_of_variation(self):
        return (self.standard_deviation() / self.mean()) * 100 if self.mean() else float(nan)

    @cache
    def pearson_asymmetry_coefficient(self):
        return 3.0 * (self.mean() - self.median()) / self.standard_deviation() if self.standard_deviation() else 0.0

    @cache
    def skewness(self):
        return self.normalized_sum_of_to_the_nth_deviations(
            3) / self.standard_deviation() ** 3 if self.standard_deviation() != 0.0 else 0.0

    @cache
    def kurtosis(self):
        return self.normalized_sum_of_to_the_nth_deviations(
            4) / self.standard_deviation() ** 4 - 3 if self.standard_deviation() != 0.0 else 0.0

    def normalized_sum_of_to_the_nth_deviations(self, n):
        sum_of_to_the_nth_deviations = sum([(value - self.mean()) ** n for value in self.data])
        return sum_of_to_the_nth_deviations / (self.data_size - 1) if self.data_size != 1 else 0.0
