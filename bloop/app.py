#!/usr/bin/env python3

from argparse import ArgumentParser
import openpyxl
import os
import sys

def scrape(path):
  for filename in os.listdir(path[0]):
    location = f'{path[0]}/{filename}'
    with open(location, 'r') as dump:
      text = dump.read()
      print(text)

def main(args):
  parser = ArgumentParser(
    prog='bloop',
    description='Auto populate spreadsheet with .txtrpt data'
  )
  parser.add_argument(
    dest='filepath',
    metavar='FILE',
    nargs=1,
    help='dump file location'
  )

  args = parser.parse_args()
  scrape(args.filepath)

def run():
  sys.exit(main(sys.argv[1:]))

if __name__ == '__main__':
  run()
