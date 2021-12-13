import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sample', action='store_true')
    parser.add_argument('-f', '--file', type=str, nargs='?')
    parser.add_argument('input', type=str, nargs='*')
    return parser.parse_known_args()

def get_input(transform, parts=None, transform2=None):
    p = parse_args()[0]
    if p.input:
        return transform(p.input)
    inp = []
    inp2 = []
    if p.file:
        f = open(p.file)
    elif p.sample:
        f = open('data/sample.txt')
    else:
        f = open('data/data.txt')
    matched = False
    for line in f.readlines():
        if not matched and parts is not None:
            matched = parts(line)
            if matched:
                continue
        if not matched:
            inp.append(transform(line.strip()))
        else:
            tl = ''
            if transform2 is None:
                tl = transform(line.strip())
            else:
                tl = transform2(line.strip())
            inp2.append(tl)
    f.close()
    if len(inp) == 1 and parts is None:
        return inp[0]
    if parts is None:
        return inp
    return inp, inp2


def read_single_keypress():
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    ret = []
    try:
        ret.append(sys.stdin.read(1)) # returns a single character
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save | os.O_NONBLOCK)
        c = sys.stdin.read(1) # returns a single character
        while len(c) > 0:
            ret.append(c)
            c = sys.stdin.read(1)
    except KeyboardInterrupt:
        ret.append('\x03')
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return tuple(ret)
