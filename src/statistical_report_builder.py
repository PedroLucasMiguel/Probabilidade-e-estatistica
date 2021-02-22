from pprint import pprint

from python_statistical_analyser import PythonStatisticalAnalyser


class StatisticalAnalysisReportBuilder(object):
    # TODO: Use ordered_dict

    def __init__(self, samples: tuple[list[float], ...],
                 titles: tuple[str, ...], analysis_tool=PythonStatisticalAnalyser):
        self.samples = samples
        self.titles = titles
        self.analysis_tool = analysis_tool

    def make_report(self, measures: tuple[str, ...] = None):

        if measures is None:
            measures = self.analysis_tool.get_available_measures()

        return_dict = {}
        for title, sample in zip(self.titles, self.samples):
            analysis = self.analysis_tool(sample)
            return_dict[title] = {measure: getattr(analysis, measure)() for measure in measures}
        return return_dict


if __name__ == '__main__':
    small_sample = [1.0, 2.0, 3.0, 4.0]
    report_builder = StatisticalAnalysisReportBuilder((small_sample,), ('Test',))
    pprint(report_builder.make_report())
    small_sample = [1.0, 3.0, 5.0, 8.0]
    report_builder = StatisticalAnalysisReportBuilder((small_sample,), ('2est',))
    pprint(report_builder.make_report())
