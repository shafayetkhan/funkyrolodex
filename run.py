from funkyrolodex import FunkyRolodex
import time

start_time = time.time()

parser = FunkyRolodex()


if __name__ == '__main__':
    parser.process_entries('sample-shafayet.in')
    parser.jsonify('result.out')

    print time.time() - start_time, 'seconds'
