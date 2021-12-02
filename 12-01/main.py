from argparse import ArgumentParser
import os.path

def sonar_sweep(input_file):
    with open(input_file) as f:
        measurements = f.readlines()

    # convert string to int
    measurements = [int(i) for i in measurements]

    count = 0
    # loop through current measurement and next with zip as pairs
    for c, n in zip(measurements, measurements[1:]):
        if c < n:
            count += 1

    print("Sonar sweep found %d measurements that are larger than the previous measurement" % count)

def extant_file(x):
    if not os.path.exists(x):
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

if __name__ == '__main__':
    parser = ArgumentParser(description="Sonar Sweep")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=extant_file,
        help="input file with sonar sweep measurements", metavar="FILE")

    args = parser.parse_args()
    sonar_sweep(args.filename)
