from graph_builder import GraphBuilder
from log_transform_exponential_distribution_generator import LogTransformExponentialDistributionGenerator
from python_normal_distribution_generator import PythonNormalDistributionGenerator

if __name__ == '__main__':
    exp = PythonNormalDistributionGenerator(5).sample(10000)
    exp_2 = LogTransformExponentialDistributionGenerator(5).sample(10000)
    bimodal = exp + exp_2
    graph_builder = GraphBuilder((bimodal,), ('Bimodal',))
    plot = graph_builder.make_plot()
    plot.savefig('C:\\Users\\lugia\\Desktop\\guaaaaph.png')
    plot.show()

    # Save bimodal to csv
    file = open('C:\\Users\\lugia\\Desktop\\jooj.csv', 'w')

    for i in bimodal:
        file.write(str(i)+"\n")

    file.close()



