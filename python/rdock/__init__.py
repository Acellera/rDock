import os
import sys

RBT_ROOT = os.path.dirname(os.path.abspath(__file__))


def main():
    # Every console script points here; the script name selects the program in bin/
    name = os.path.basename(sys.argv[0])
    os.environ["RBT_ROOT"] = RBT_ROOT
    argv = [os.path.join(RBT_ROOT, "bin", name)] + sys.argv[1:]
    if name in ("sdrmsd", "sdtether"):
        argv.insert(0, sys.executable)
    os.execv(argv[0], argv)
