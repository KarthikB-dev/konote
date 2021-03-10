import re
import sys

from samepack import main
#thank you to @r2dev2 for this program
if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(main())
