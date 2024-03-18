import subprocess

input_paths = subprocess.run(
    "ls automata-bench-inputs/*",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")

for input_path in input_paths:
    folder = '.'.join(input_path.split('/')[-1].split('.')[:-1])
    subprocess.run(f"mkdir -p afacomp/{folder}", shell=True, check=True)

    subprocess.run(f"wc -l {input_path}", shell=True, check=True)

    with open(input_path, "r") as f:
        for i, bench_base in enumerate(f):
            bench_base = bench_base.strip()
            subprocess.run(
                f"cp {bench_base}.afa afacomp/{folder}/{i}.afa",
                shell=True,
                check=True,
            )
            if (i + 1) % 1000 == 0:
                print(i)
