import pickle
from optparse import OptionParser
from prettytable import PrettyTable
from functools import reduce
from matrix import matrix, reader, worker




def app(filename):
    with open(filename, 'rb') as src:
        matrix = pickle.load(src)
        print('[*] Load and build table from src')

    table = PrettyTable()

    for row in matrix:
        table.add_row(row)
    print(table)

    table_result = PrettyTable()
    results = ['Result']
    for col in zip(*matrix):
        results.append(reduce(lambda a, x: a * x, col))
    table_result.add_row(results)
    print(table_result)


def app_oop(filename):
    my_matrix = matrix.StandartMatrix(reader.ReaderPickle(filename))
    print(my_matrix.matrix_size())

    table = PrettyTable()
    for row in my_matrix.get_matrix():
        table.add_row(row)
    print(table)

    my_matrix.set_worker(worker.MultiplicationColsWorker(my_matrix.get_matrix()))
    table_result = PrettyTable()
    results = ['Result']
    table_result.add_row(my_matrix.execute_worker())
    print(table_result)

    '''---------------Square Matrix---------------'''
    matrix_square = matrix.SquareMatrix(reader.ReaderPickle(filename))
    print(my_matrix.get_matrix())
    



    







if __name__ == '__main__':
    parse = OptionParser("""

        ./app.py [options]
     
    options:
     
    -f, --file    [::] File to read pickle src

        """)
  
    parse.add_option('-f','--file',dest='F',type='string', help='File to read')

    (opt,args) = parse.parse_args()
    if opt.F == None:
        print(parse.usage)
        exit(0)
    else:
        try:  
            app(opt.F)
            print('\n\n----------------------- OOP ---------------------------')
            app_oop(opt.F)                     
        except Exception as err:
            print('[-] {}'.format(err))