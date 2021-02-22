
# alpha: value
squared_chi_tabled_values = {
    1: 3.841,
    2: 5.991,
    3: 7.815,
    4: 9.488,
    5: 11.070,
    6: 12.592,
    7: 14.067,
    8: 15.507,
    9: 16.919,
    10: 18.307,
    11: 19.675,
    12: 21.026,
    13: 22.362,
    14: 23.685,
    15: 24.996,
    16: 26.296,
    17: 27.587,
    18: 28.869,
    19: 30.144,
    20: 31.410,
    21: 32.671,
    22: 33.924,
    23: 35.172,
    24: 36.415,
    25: 37.652,
    26: 38.885,
    27: 40.113,
    28: 41.337,
    29: 42.557,
    30: 43.773,
    40: 55.758,
    50: 67.505,
    60: 79.082,
    70: 90.531,
    80: 101.879,
    90: 113.145,
    100: 124.342,
}


class SquaredChiCalculator(object):

    def __init__(self, expected_frequencies, observed_frequencies):
        self.validate_frequencies(expected_frequencies, observed_frequencies)
        self.expected = expected_frequencies
        self.observed = observed_frequencies

    @staticmethod
    def validate_frequencies(expected_frequencies, observed_frequencies):
        if (type(expected_frequencies), type(observed_frequencies)) != (list, list):
            raise TypeError
        if not all(type(value) == int for value in expected_frequencies):
            raise TypeError
        if not all(type(value) == int for value in observed_frequencies):
            raise TypeError
        if len(expected_frequencies) < 2 or len(observed_frequencies) < 2:
            raise SquaredChiCalculator.LowCategoryCountError
        if sum(expected_frequencies) != sum(observed_frequencies):
            raise SquaredChiCalculator.DiscrepantTotalFrequencyCountsError

    def calculate(self):
        return sum(self.normalized_squared_difference_at_index(i) for i in range(len(self.expected)))

    def normalized_squared_difference_at_index(self, index):
        return (self.squared_difference_at_index(index) / self.expected[index]) if self.expected[index] != 0 else 0.0

    def squared_difference_at_index(self, index):
        return (self.expected[index] - self.observed[index]) ** 2

    class LowCategoryCountError(Exception):
        def __str__(self):
            return 'Hello I am not enough buckets'

    class DiscrepantTotalFrequencyCountsError(Exception):
        def __str__(self):
            return 'Hello I am Discrepancy'
