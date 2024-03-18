import subprocess

input_paths = subprocess.run(
    "ls afacomp",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")

i = 0
for input_path in input_paths:
    subprocess.run("rm -rf afacomp_simple/" + input_path, shell=True, check=True)
    subprocess.run("mkdir afacomp_simple/" + input_path, shell=True, check=True)

    input_paths2 = subprocess.run(
        "ls afacomp/" + input_path,
        shell=True,
        stdout=subprocess.PIPE,
        check=True
    )
    input_paths2 = input_paths2.stdout.decode("utf8").strip().split("\n")
    for input_path2 in input_paths2:
        i += 1
        print(i)

        subprocess.run(
            f"python3 ../automata-safa-new/scripts/simplify.py"
            f" < afacomp/{input_path}/{input_path2}"
            f" > afacomp_simple/{input_path}/{input_path2}",
            shell=True,
            check=True,
        )
