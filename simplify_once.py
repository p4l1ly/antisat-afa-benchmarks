import subprocess

input_paths = subprocess.run(
    "ls afacomp",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")
input_paths.sort()

i = 0
for input_path in input_paths:
    # subprocess.run("rm -rf afacomp_simplify_once/" + input_path, shell=True, check=True)
    subprocess.run("mkdir -p afacomp_simplify_once/" + input_path, shell=True, check=True)

    input_paths2 = subprocess.run(
        "ls afacomp/" + input_path,
        shell=True,
        stdout=subprocess.PIPE,
        check=True
    )
    input_paths2 = input_paths2.stdout.decode("utf8").strip().split("\n")
    input_paths2.sort()
    for input_path2 in input_paths2:
        i += 1
        print(i)
        print(f"{input_path}/{input_path2}")
        subprocess.run(
            f"python3 ../automata-safa-new/scripts/simplify_once.py"
            f" < afacomp/{input_path}/{input_path2}"
            f" > afacomp_simplify_once/{input_path}/{input_path2}",
            shell=True,
            check=True,
        )

