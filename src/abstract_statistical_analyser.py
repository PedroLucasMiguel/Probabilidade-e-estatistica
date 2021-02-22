from abc import ABCMeta, abstractmethod


class AbstractStatisticalAnalyser(metaclass=ABCMeta):

    @staticmethod
    def validate_data(data: list[float]) -> None:
        if type(data) != list:
            raise TypeError
        if not data:
            raise AbstractStatisticalAnalyser.EmptyDataListError

    @staticmethod
    def get_available_measures() -> list[str]:
        return [
            # LOCATION
            'min', 'max', 'mean', 'mode', 'median', 'lower_quartile', 'upper_quartile',
            # VARIABILITY
            'amplitude', 'average_deviation', 'variance', 'standard_deviation',
            'percentage_within_one_std_dev', 'percentage_within_two_std_dev', 'percentage_within_three_std_dev',
            'interquartile_range', 'percentage_of_outliers', 'coefficient_of_variation',
            # SHAPE
            'pearson_asymmetry_coefficient', 'skewness', 'kurtosis'
        ]

    # TODO: Implement rest of statistical analysis measures
    # TODO: Put formulas in docstrings?

    # LOCATION

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def max(self):
        pass

    @abstractmethod
    def mean(self):
        pass

    @abstractmethod
    def mode(self):
        pass

    @abstractmethod
    def median(self):
        pass

    @abstractmethod
    def lower_quartile(self):
        pass

    @abstractmethod
    def upper_quartile(self):
        pass

    # VARIABILITY

    @abstractmethod
    def amplitude(self):
        pass

    @abstractmethod
    def average_deviation(self):
        pass

    @abstractmethod
    def variance(self):
        # Momento 2. Variância
        pass

    @abstractmethod
    def standard_deviation(self):
        pass

    @abstractmethod
    def percentage_within_one_std_dev(self):
        pass

    @abstractmethod
    def percentage_within_two_std_dev(self):
        pass

    @abstractmethod
    def percentage_within_three_std_dev(self):
        pass

    @abstractmethod
    def interquartile_range(self):
        pass

    @abstractmethod
    def percentage_of_outliers(self):
        pass

    @abstractmethod
    def coefficient_of_variation(self):
        pass

    # SHAPE

    @abstractmethod
    def pearson_asymmetry_coefficient(self):
        pass

    @abstractmethod
    def skewness(self):
        # Momento 3. Obliquidade
        pass

    @abstractmethod
    def kurtosis(self):
        # Momento 4. Curtose
        pass

    class EmptyDataListError(Exception):

        def __str__(self):
            return "Module requires non-empty collection of data for analysis"


if __name__ == '__main__':
    try:
        AbstractStatisticalAnalyser.validate_data([])
    except Exception as e:
        print(e)
