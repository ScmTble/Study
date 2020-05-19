import math
import argparse
parser = argparse.ArgumentParser(description='hello')
parser.add_argument('-r', '--radius', required=True, type=int)
parser.add_argument('-H', '--height', required=True, type=int)
args = parser.parse_args()


def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol


if __name__ == "__main__":
    print(cylinder_volume(args.radius, args.height))
