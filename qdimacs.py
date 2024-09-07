import subprocess

input_paths = subprocess.run(
    "ls afacomp_simpl_qcir",
    shell=True,
    stdout=subprocess.PIPE,
    check=True
)
input_paths = input_paths.stdout.decode("utf8").strip().split("\n")

i = 0
for input_path in input_paths:
    subprocess.run("rm -rf afacomp_simpl_qdimacs/" + input_path, shell=True, check=True)
    subprocess.run("mkdir -p afacomp_simpl_qdimacs/" + input_path, shell=True, check=True)

    input_paths2 = subprocess.run(
        "ls afacomp_simpl_qcir/" + input_path,
        shell=True,
        stdout=subprocess.PIPE,
        check=True
    )
    input_paths2 = input_paths2.stdout.decode("utf8").strip().split("\n")
    for input_path2 in input_paths2:
        if not input_path2:
            continue
        i += 1
        print(i)

        bad_trivial = False
        with open(f"afacomp_simpl_qcir/{input_path}/{input_path2}", "r") as f:
            f = iter(f)
            next(f)
            if next(f) == "exists(x)\n":
                bad_trivial = True

        if bad_trivial:
            with open(f"afacomp_simpl_qcir/{input_path}/{input_path2}", "w") as f:
                f.write("#QCIR-14\n")
                f.write("exists(x)\n")
                f.write("output(y)\n")
                f.write("y = or(x, -x)\n")

        print(f"afacomp_simpl_qcir/{input_path}/{input_path2}")
        subprocess.run(
            "../booleguru/build/booleguru"
            f" afacomp_simpl_qcir/{input_path}/{input_path2} --qdimacs"
            f" > afacomp_simpl_qdimacs/{input_path}/{input_path2[:-5]}.qdimacs",
            shell=True,
            check=True,
        )
