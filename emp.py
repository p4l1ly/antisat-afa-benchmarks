import re
import os
import subprocess

input_paths = subprocess.run(
    "ls automata-bench/*.input",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")
input_paths.sort()

LOAD_CMD = "load_automaton "
LOAD_CMD_LEN = len(LOAD_CMD)

for input_path in input_paths:
    folder = '.'.join(input_path.split('/')[-1].split('.')[:-1])
    subprocess.run(f"mkdir -p afacomp_emp/{folder}", shell=True, check=True)

    subprocess.run(f"wc -l {input_path}", shell=True, check=True)

    with open(input_path, "r") as f:
        for i, bench_base in enumerate(f):
            bench_base = bench_base.strip()
            gen_aut = os.path.dirname(bench_base) + "/gen_aut"
            try:
                with open(f"{bench_base}.emp", "r") as f:
                    emptxt = f.read()

            except FileNotFoundError:
                subprocess.run(
                    f"echo miss {folder} {i} && touch afacomp_emp/{folder}/{i}.emp",
                    shell=True,
                    check=True,
                )
            else:
                nfas = [
                    line[LOAD_CMD_LEN:]
                    for line in emptxt.strip().split("\n")
                    if line.startswith(LOAD_CMD)
                ]

                with open(f"afacomp_emp/{folder}/{i}.emp", "w") as f2:
                    f2.write(emptxt)

                gen_aut2 = f"afacomp_emp/{folder}/{i}.nfas"
                os.mkdir(gen_aut2)

                for j, nfa in enumerate(nfas):
                    subprocess.run(
                        f"cp {gen_aut}/{nfa}.mata {gen_aut2}/{j}.mata",
                        shell=True,
                        check=True,
                    )

            if (i + 1) % 1000 == 0:
                print(i)
