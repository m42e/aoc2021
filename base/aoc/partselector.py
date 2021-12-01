import argparse
import logging

logging.basicConfig(level=logging.WARNING)
_logger = logging.getLogger(__name__)

args = None
def parse_args():
    global args
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('-A', action='store_true')
        parser.add_argument('-B', action='store_true')
        parser.add_argument('-G', action='store_true')
        parser.add_argument('-q', action='store_true')
        parser.add_argument('-v', "--verbose", dest="verbose_count",
                            action="count", default=0,
                            help="increases log verbosity for each occurence.")
        args = parser.parse_known_args()
    return args

def get_logger(*args, **kwargs):
    p = parse_args()[0]
    log = logging.getLogger(*args, **kwargs)
    log.setLevel(max(3 - p.verbose_count, 1) * 10)
    return log

def part_one():
    p = parse_args()[0]
    if p.B:
        return False
    if not p.q:
        print('==== PART I ====')
    return True

def part_two():
    p = parse_args()[0]
    if p.A:
        return False
    if not p.q:
        print('==== PART II ====')
    return True

def draw():
    p = parse_args()[0]
    if p.G:
        return True
    return False

