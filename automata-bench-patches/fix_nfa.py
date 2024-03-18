import re
import sys

out = []

in_parens = re.compile(r"^(.*)\(([^\(]*)\)$")
is_q = re.compile(r"^q[0-9a-zA-Z]+$")
ltrue = re.compile(r"\btrue\b")
lfalse = re.compile(r"\bfalse\b")

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        modified = False

        line = ltrue.sub("\\\\true", line)
        line = lfalse.sub("\\\\false", line)

        if line.startswith("q") and line.endswith(")"):
            line_match = in_parens.match(line)
            if line_match:
                qs = line_match[2].split(" | ")
                if all(is_q.match(q) for q in qs):
                    modified = True
                    for q in qs:
                        out.append(line_match[1] + q)

        if not modified:
            out.append(line)

with open(sys.argv[1], "w") as f:
    for line in out:
        print(line, file=f)
