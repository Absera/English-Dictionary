# English Dictionary
# Author: Absera Temesgen

import sys
from dictionary import *
from display import *

args = sys.argv[1:] if len(sys.argv) >= 2 else 0


if args:
    if args[0] == 'rand':
        rand = generateRandom()
        displayContent(rand["word"], rand["definition"])
    elif args[0] == "trans":
        if args[1]:
            for i in args[1:]:
                trans = translate(i)
                displayContent(trans['word'], trans['definition'])
        else: displayError("Enter a word after <trans>")
    else: displayError("Doesn't make sense!")
else: displayError("Enter Something!")


