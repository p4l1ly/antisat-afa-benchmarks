import subprocess

input_paths = subprocess.run(
    "ls afacomp_push_pos_not",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")

i = 0
for input_path in input_paths:
    # subprocess.run("rm -rf afacomp_simpl_tseytin/" + input_path, shell=True, check=True)
    subprocess.run("mkdir -p afacomp_simpl_tseytin/" + input_path, shell=True, check=True)

    input_paths2 = subprocess.run(
        "ls afacomp_push_pos_not/" + input_path,
        shell=True,
        stdout=subprocess.PIPE,
        check=True
    )
    input_paths2 = input_paths2.stdout.decode("utf8").strip().split("\n")
    for input_path2 in input_paths2:
        i += 1
        print(i)

        subprocess.run(
            "automata-safa-one addInit"
            f" < afacomp_push_pos_not/{input_path}/{input_path2}"
            "| automata-safa-one tseytin"
            f" > afacomp_simpl_tseytin/{input_path}/{input_path2[:-4]}.antisat",
            shell=True,
            check=True,
        )
