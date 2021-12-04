from argparse import ArgumentParser
import os.path

def depth_length(filename):
    h = 0; d = 0
    with open(filename) as f:
        for line in f:
            direction, amp = line.split()
            amp = int(amp)
            if direction == 'forward':
                h += amp

            if direction == 'up':
                d -= amp

            if direction == 'down':
                d += amp

    print("Horizontal position is %d and depth is %d, resulting in %d" % (h,d, h*d))
    return h, d

def depth_length_aim(filename):
    h = 0; d = 0; a = 0
    with open(filename) as f:
        for line in f:
            direction, amp = line.split()
            amp = int(amp)
            if direction == 'forward':
                h += amp
                d += a*amp

            if direction == 'up':
                a -= amp

            if direction == 'down':
                a += amp

    print("Horizontal position is %d and depth is %d, resulting in %d" % (h,d, h*d))
    return h, d

def extant_file(x):
    if not os.path.exists(x):
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

if __name__ == '__main__':
    parser = ArgumentParser(description="Submarine input")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=extant_file,
        help="input file with sonar sweep measurements", metavar="FILE")
    args = parser.parse_args()

    depth_length(args.filename)
    depth_length_aim(args.filename)
