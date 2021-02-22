import matplotlib.pyplot as plt

from log_transform_exponential_distribution_generator import \
    LogTransformExponentialDistributionGenerator
from python_normal_distribution_generator import PythonNormalDistributionGenerator

# Caso A: Exponencial sem arquivo

# self.graph, (box, hist) = plt.subplots(1, 2, figsize=(10, 3))
# box.boxplot(self.random_population, vert=False)
# hist.hist(self.random_population, bins=30)

# Caso B: Exponencial com arquivo

# self.graph, (box, hist_user, hist_random) = plt.subplots(1, 3, figsize=(10, 3))
# box.boxplot([self.user_data, self.random_population], vert=False)
# hist_user.hist(self.user_data, bins=30)
# hist_random.hist(self.random_population, bins=30)

# Caso C : Normal sem arquivo

# self.graph, (box, hist_random, hist_sampler) = plt.subplots(1, 3, figsize=(10, 3), sharex='none')
# box.boxplot([self.random_population, self.sampling_population], vert=False)
# hist_random.hist(self.random_population, bins=30)
# hist_sampler.hist(self.sampling_population, bins=30)

# Caso D: To be continued...
from frequency_calculator import FrequencyCalculator


class GraphBuilder(object):

    def __init__(self, samples: tuple[list[float], ...],
                 labels: tuple[str, ...] = None,
                 dimensions: tuple[int, int] = (13.5, 3)):
        self.histogram_count = len(samples)
        # print(self.histogram_count)
        default_labels = ('Foo', 'Bar', 'Baz')
        self.labels = labels if labels is not None else default_labels[:self.histogram_count]
        # print(self.labels)
        self.graph_obj = None
        self.graph_obj, self.subplots = plt.subplots(1, self.histogram_count + 1, figsize=dimensions)
        # print(self.graph_obj)
        boxplot = self.subplots[0]
        boxplot.set_yticklabels(labels[::-1], fontsize=6)
        histograms = self.subplots[1:]

        # print(boxplot)
        # print(histograms)
        boxplot.boxplot(samples[::-1], vert=False, flierprops={'marker': '.', 'markersize': 3})
        # hist_random.hist(self.random_population, bins=30)

        for i, histogram in enumerate(histograms):
            bins = FrequencyCalculator.get_recommended_bucket_count_for_sample(samples[i])
            histogram.hist(samples[i], edgecolor='black', bins=bins)
            histogram.set_title(labels[i], fontsize=6)

    def make_plot(self):
        return self.graph_obj


if __name__ == '__main__':
    try:
        default_normal_distribution = PythonNormalDistributionGenerator().sample(100)
        spread_normal_distribution = PythonNormalDistributionGenerator(std_deviation=10).sample(100)
        default_exponential_distribution = LogTransformExponentialDistributionGenerator().sample(100)
        gb = GraphBuilder((default_normal_distribution, spread_normal_distribution, default_exponential_distribution),
                          ('Title', 'Another', 'Card'))
        graph = gb.make_plot()
        graph.show()
    except Exception as e:
        print('Agr eu vou debuggar, olê olê olá')
        print(e)
