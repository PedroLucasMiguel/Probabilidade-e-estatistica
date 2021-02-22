# {
#  'generation': {
#   'sample_size': ?
#   'alpha': ?
#   'mean': ?
#   'std_deviation': ?
#   'population': ?
#  }
#  'user_data': []
# }
from copy import deepcopy
from math import sqrt

from log_transform_exponential_distribution_generator import \
    LogTransformExponentialDistributionGenerator
from population_sample_distribution_generator import PopulationSampleDistributionGenerator
from python_normal_distribution_generator import PythonNormalDistributionGenerator
from frequency_calculator import FrequencyCalculator
from squared_chi_calculator import SquaredChiCalculator, squared_chi_tabled_values
from graph_builder import GraphBuilder
from statistical_report_builder import StatisticalAnalysisReportBuilder


class RequestInterpreter:

    def __init__(self, request_dict=None):

        print('Request Dict: ', request_dict)

        generation_dict = request_dict['generation']

        self.main_generator = None
        if 'alpha' in generation_dict.keys():
            alpha = generation_dict['alpha']
            self.main_generator = LogTransformExponentialDistributionGenerator(alpha)
        else:
            mean = generation_dict['mean']
            std_deviation = generation_dict['std_deviation']
            self.main_generator = PythonNormalDistributionGenerator(mean, std_deviation)

        print('Generator: ', self.main_generator)

        self.user_data = request_dict['user_data']
        if self.user_data is not None:
            print('User haz sum deytah')
            self.sample_size = len(self.user_data)
        else:
            print('User haz no deytah. Poor user.',
                  'For juzt $1 a day, u can halp users all around the globe (if you\'re a flat earther, I\'m so sorry',
                  'to get some data to analyse.',
                  'Join our cause :)')
            self.sample_size = generation_dict['sample_size']

        self.random_population = self.main_generator.sample(self.sample_size)

        print('Random population: ', self.random_population[:20])

        self.sampling_population = None
        if type(self.main_generator) == PythonNormalDistributionGenerator:
            print('Am generating sampling population')
            population_sampling_size = generation_dict['population']
            population_sampler = PopulationSampleDistributionGenerator(self.random_population, population_sampling_size)
            self.sampling_population = population_sampler.sample(self.sample_size)
            pass

        print('Population sampling: ', self.sampling_population[:20] if self.sampling_population else 'None generated')

        report_builder = None
        self.graph = None
        if self.sampling_population is None:
            if self.user_data is None:
                report_builder = StatisticalAnalysisReportBuilder((self.random_population,), ('Gerador',))
                graph_builder = GraphBuilder((self.random_population,))
                self.graph = graph_builder.make_plot()
            else:
                report_builder = StatisticalAnalysisReportBuilder((self.user_data, self.random_population),
                                                                  ('Usuario', 'Gerador'))
                graph_builder = GraphBuilder((self.user_data, self.random_population))
                self.graph = graph_builder.make_plot()
        else:
            print("2 samples 1 report")
            report_builder = StatisticalAnalysisReportBuilder((self.random_population, self.sampling_population),
                                                              ('Populacao', 'Amostras'))
            print("pls no crash")
            graph_builder = GraphBuilder((self.random_population, self.sampling_population))
            self.graph = graph_builder.make_plot()
            print("pls no crash 2")

        self.report = report_builder.make_report()
        print("report machine broke")
        print('Report: ', self.report)
        print('Graph Obj: ', self.graph)


class RequestInterpreterTest(RequestInterpreter):

    def __init__(self, request_dict=None):

        # print('Got request', request_dict)

        self.request_dict = deepcopy(request_dict)  # TODO: Apagar se possivel
        user_data = request_dict['user_data']
        generation_dict = request_dict['generation']
        exponential_mode = 'alpha' in generation_dict
        normal_mode = 'mean' in generation_dict
        titles = []
        sample_sets = []
        squared_chi_sets = []

        if user_data is not None:
            titles.append('Dados no Arquivo')
            sample_sets.append(user_data)
            squared_chi_sets.append(user_data)
            generation_dict['sample_size'] = len(user_data)

        self.sample_size = generation_dict['sample_size']

        if exponential_mode:
            titles.append(u'X ~ Exp(α)')
            alpha = generation_dict['alpha']
            generator = LogTransformExponentialDistributionGenerator(alpha)
            sample = generator.sample(self.sample_size)
            sample_sets.append(sample)
            squared_chi_sets.append(sample)
            # print('Sets for squared chi', len(squared_chi_sets))

        if normal_mode:
            titles.append(u'X ~ N(μ, σ)')
            mean = generation_dict['mean']
            std_deviation = generation_dict['std_deviation']
            generator = PythonNormalDistributionGenerator(mean, std_deviation)
            sample_sets.append(generator.sample(self.sample_size))

            # Teorema do Limite Central Tiem
            titles.append(f'Amostrado de {titles[0]}')
            population_sampling_size = generation_dict['population']
            generator = PopulationSampleDistributionGenerator(sample_sets[0], population_sampling_size)
            generator_sample = generator.sample(self.sample_size)
            sample_sets.append(generator_sample)
            squared_chi_sets.append(generator_sample)

            titles.append(u'X ~ N(μ, (σ/√n))')
            std_deviation = std_deviation / sqrt(population_sampling_size)
            generator = PythonNormalDistributionGenerator(mean, std_deviation)
            generator_sample = generator.sample(self.sample_size)
            sample_sets.append(generator_sample)
            squared_chi_sets.append(generator_sample)

        titles = tuple(titles)
        # print("Titles!", titles)
        sample_sets = tuple(sample_sets)

        report_builder = StatisticalAnalysisReportBuilder(sample_sets, titles)
        self.report = report_builder.make_report()

        graph_builder = GraphBuilder(sample_sets, titles)
        self.graph = graph_builder.make_plot()

        # print('Sets for squared chi', len(squared_chi_sets))

        self.squared_chi_report = None

        # SQUARED CHI TIME
        if len(squared_chi_sets) < 2:
            # print('NO CHI')
            return

        # squared_chi_sets = squared_chi_sets[-2:]
        expected = squared_chi_sets[-1]
        observed = squared_chi_sets[-2]

        calc = FrequencyCalculator((expected, observed))
        ranges, expected_freq, observed_freq = calc.count_frequencies(offset=0.0)
        # print('squared_chi_debug', ranges, expected_freq, observed_freq, sep='\n')

        try:
            calc = SquaredChiCalculator(expected_freq, observed_freq)
            squared_chi = calc.calculate()
            # print('Squared chi result', squared_chi)

            liberty_degrees = len(ranges) - 2
            # print('Liberty degress', liberty_degrees)

            max_allowed_chi = squared_chi_tabled_values[liberty_degrees]
            statistical_significance = squared_chi > max_allowed_chi

            self.squared_chi_report = (squared_chi, max_allowed_chi, statistical_significance)
        except (KeyError, Exception) as e:
            # print('We don\'t have this key fam, so sorry',
            #       'For just $1 a day, you can help programmer like us get more table squared chi values'
            #       'Join our cause :)')
            # print('THERE WAS EXCEPTION')
            # print(e)
            self.squared_chi_report = None


class Model:
    def __init__(self):
        self.requestInterpreter = None

    def sendRequest(self, request_dict):
        self.requestInterpreter = RequestInterpreterTest(request_dict)

    def getResults(self):
        return {
            'Report': self.requestInterpreter.report,
            'Graph': self.requestInterpreter.graph,
            'Squared_Chi': self.requestInterpreter.squared_chi_report,
        }


if __name__ == '__main__':
    test_dict = {}
