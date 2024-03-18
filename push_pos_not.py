import subprocess

input_paths = subprocess.run(
    "ls afacomp_simplify_once",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")
input_paths.sort()

i = 0
for input_path in input_paths:
    # subprocess.run("rm -rf afacomp_push_pos_not/" + input_path, shell=True, check=True)
    subprocess.run("mkdir -p afacomp_push_pos_not/" + input_path, shell=True, check=True)

    input_paths2 = subprocess.run(
        "ls afacomp_simplify_once/" + input_path,
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
            f"python3 ../automata-safa-new/scripts/push_pos_not.py"
            f" < afacomp_simplify_once/{input_path}/{input_path2}"
            f" > afacomp_push_pos_not/{input_path}/{input_path2}",
            shell=True,
            check=True,
        )

