import csv


class CSV_Reader:
    def read_user_data(self, path: str):

        with open(path, 'r') as file: # Abre o arquivo
            csv_file = csv.reader(file)
            data_list = []

            for row in csv_file: # Percorre a coluna guardando todos sos dados dentro da lista
                data_list.append(float(row[0]))

            print("CSV Len: ", len(data_list))

            return data_list


if __name__ == "__main__":
    reader = CSV_Reader()
    #print(reader.read_user_data('test.csv'))
