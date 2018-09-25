# Replace Text

replace OPT (from) (to) -- filename...

A simple command-line looks for all occurrences of string (from) and replaces it with string (to).
It is possible to specify one or more files on which to perform the replace
operation(s) in a single replace command.

Where OPT can be zero or more of
-b
-f
-l
-i

COMMAND-LINE ARGUMENTS AND OPTIONS
1. from: string to be replaced with string to.
2. to: string that will replace string from.
3. filename: the file(s) on which the replace operation has to be performed.
4. -b: if specified, the replace utility creates a backup copy of each file on
5. which a replace operation is performed before modifying it.
6. -f: if specified, the replace utility only replaces the first occurrence of string
from in each file.
7. -l: if specified, the replace utility only replaces the last occurrence of string 
from in each file.
8. -i: if specified, the rep
