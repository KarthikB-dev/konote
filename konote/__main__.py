import re
import sys

# thank you to r2dev2 and kento nishi for this code
from konote import main

if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(main())
