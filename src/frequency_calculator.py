from math import isclose, floor
from pprint import pprint


class FrequencyCalculator:

    def __init__(self, samples: tuple[list[float], ...]):
        self.samples = samples
        self.lengths = tuple([len(sample) for sample in samples])

    @staticmethod
    def get_recommended_bucket_count_for_sample(sample: list[float]) -> int:
        return_values = [
            (20, 5),
            (100, 7),
            (200, 9),
            (500, 11),
            (1000, 15),
            (5000, 21),
            (10000, 31),
        ]

        for gatekeeper, return_value in return_values:
            if len(sample) < gatekeeper:
                return return_value

        return 41  # default value

    def count_frequencies(self, bucket_count: int = None,
                          offset: float = None) -> tuple[list, ...]:
        if bucket_count is None:
            bucket_count = max(self.get_recommended_bucket_count_for_sample(sample) for sample in self.samples)

        # TODO: validate bucket_count

        minimum = min(min(sample) for sample in self.samples)
        maximum = max(max(sample) for sample in self.samples)

        if isclose(minimum, maximum) or bucket_count == 1:
            only_interval = [minimum, maximum]
            all_the_lengths_in_tuples = [[length] for length in self.lengths]
            return tuple([only_interval] + all_the_lengths_in_tuples)

        # TODO: validate offset

        if offset is None:
            offset = (maximum - minimum) / (2 * bucket_count - 2)

        minimum -= offset
        maximum += offset
        bucket_size = (maximum - minimum) / bucket_count

        bucket_ranges = [minimum + i * bucket_size for i in range(bucket_count + 1)]

        frequencies_list = []

        for sample in self.samples:
            sample_frequency_list = [0] * bucket_count
            for value in sample:
                bucket_index = floor((value - minimum) // bucket_size)
                if bucket_index == bucket_count:  # Edge values
                    bucket_index -= 1
                sample_frequency_list[bucket_index] += 1
            frequencies_list.append(sample_frequency_list)

        return tuple([bucket_ranges] + frequencies_list)


if __name__ == '__main__':
    test_sample = [1.0, 1.0 + 10 ** (-10)]
    # test_sample_2 = [2.0, 3.0, 4.0, 4.0, 4.0, 4.0, 3.9]
    calc = FrequencyCalculator((test_sample,))
    freqs = calc.count_frequencies()
    pprint(freqs)
