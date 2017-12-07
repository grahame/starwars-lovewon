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
    colours = [(255,0,0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211), (255, 0, 0)]
    nframes = (7, 7, 7, 7, 7, 7, 8)

    def interp(a, b, i, t):
        g = (b - a) / t
        return int(round(a + g * i, 0))

    print(sum(nframes))
    # extrapolate to 50 frames
    upto = 0
    for (c1, c2), (nframes) in zip(pairwise(colours), nframes):
        for frame in range(nframes):
            r = interp(c1[0], c2[0], frame, nframes)
            g = interp(c1[1], c2[1], frame, nframes)
            b = interp(c1[2], c2[2], frame, nframes)
            target = "#%0.2X%0.2X%0.2X" % (r, g, b)
            print(upto, target)
            check_call(['convert', 'frames/%05d.png' % (upto), '-fuzz', '30%', '-fill', target, '-opaque', '#f8038e', 'output/%05d.png' % (upto)])
            upto += 1
    os.system('convert -loop 0 output/*.png output.gif')


if __name__ == '__main__':
    main()

