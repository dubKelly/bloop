#!/usr/bin/env python3

from argparse import ArgumentParser
import sys


def main(args):
  parser = ArgumentParser(
    prog='bloop',
    description='Auto populate spreadsheet with .txtrpt data'
  )
  parser.add_argument(
    dest='filename',
    metavar='FILE',
    nargs=1,
    help='dump file location'
  )

  args = parser.parse_args()
  print(args.filename)


def run():
  sys.exit(main(sys.argv[1:]))

if __name__ == '__main__':
  run()
