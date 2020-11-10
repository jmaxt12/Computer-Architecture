# This file is running eveything from within

#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load()
#print(cpu.ram)
cpu.run()
print(sys.argv[0]) 