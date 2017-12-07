#!/usr/bin/env python3

import os
from subprocess import check_call
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    for frame in range(50):
        h = (100 + (frame * 16))
        print(frame, h)
        check_call(['convert', 'frames/%05d.png' % (frame), '-modulate', '100,100,%d' % (h), 'output/%05d.png' % (frame)])
    os.system('convert -loop 0 output/*.png output.gif')


if __name__ == '__main__':
    main()

