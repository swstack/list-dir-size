import argparse
import os
import sys


def _get_args():
    """Parse command line arguments and return (Namespace) accessor"""

    parser = argparse.ArgumentParser(description='List directory size recursively')
    parser.add_argument('-d', '--directory',
                        default=os.getcwd(),
                        help='Which directory? (Default CWD)')
    parser.add_argument('-l', '--levels',
                        default=1,
                        help='How many directories deep? (Default 1)')
    parser.add_argument('-hr', '--human-readable',
                        action='store_true',
                        default=True,
                        help='e.g. display 1000 as 1KB, 10000 as 1MB, etc.')
    return parser.parse_args()


def _normalize_path(path):
    """Normalize and return an absolute path and make sure it's a directory

    Note: if '~' is the first part of the path it will be interpreted as the
    users home dir.
    """

    if path.startswith('~'):
        path = os.path.join(os.path.expanduser('~'), *path.strip('~').split('/'))

    absolute_path = os.path.abspath(path)
    if not os.path.isdir(absolute_path):
        print '{} is not a directory!'.format(absolute_path)
        sys.exit(1)

    return absolute_path


def _walkdirs(rootdir, level=1):
    """Generator implementation of os.walk that accepts a level argument"""

    rootdir = os.path.abspath(rootdir)
    desired_level = rootdir.count(os.path.sep) + level

    for root, dirs, files in os.walk(rootdir):
        if not dirs:
            break

        current_level = root.count(os.path.sep)
        if current_level >= desired_level:
            break

        for d in dirs:
            yield os.path.abspath(os.path.join(root, d))


def _calc_dir_size(directory):
    """Calculate the size of a directory in bytes"""

    total_size = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size


def _human_readable(size_in_bytes):
    """Convert an integer number of bytes into human readable form

    E.g.
            _human_readable(500)      == 500B
            _human_readable(1024)     == 1KB
            _human_readable(11500)    == 11.2KB
            _human_readable(1000000)  ==
    """

    if size_in_bytes < 1024:
        return "{}B".format(size_in_bytes)

    ctr = -1
    while True:
        if size_in_bytes / 1024.0 < 1:
            break
        size_in_bytes /= 1024.0
        ctr += 1
    size_grps = ['KB', 'MB', 'GB', 'TB', 'PB']
    return "{:.2f}{}".format(size_in_bytes, size_grps[ctr])


def main():
    args = _get_args()
    directory = _normalize_path(args.directory)
    for d in _walkdirs(directory, level=args.levels):
        size = _calc_dir_size(d)
        if args.human_readable:
            size = _human_readable(size)
        size_rjusted = "{}".format(size).rjust(80, '.')
        absolute_path = os.path.abspath(d)
        out = "{}{}".format(absolute_path, size_rjusted[-(80 - len(absolute_path)):])
        print out


if __name__ == "__main__":
    main()
