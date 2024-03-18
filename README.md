# Benchmarks for "Antichain with SAT and Tries" paper for SAT 2024

This repository contains the benchmarks used in the paper "Antichain with SAT and Tries" submitted to SAT 2024.
It directly contains the benchmarks in formats for all the tools used in the paper.
It also presents the scripts that were used to arrange and preprocess the benchmarks from https://github.com/VeriFIT/automata-bench

## Tools

### AntiSAT

It can be found at https://github.com/p4l1ly/antisat at `sat2024` tag, we have compiled it with flags

```
cmake -S . -B buildafa_clause_heap -DCMAKE_BUILD_TYPE=Release \
  -DMODE=AFA_CLAUSE_HEAP_HEAP \
  -DSTRENGTHENCC=ON \
  -DNO_POSNEG_OUTPUTS=ON \
  -DONE_ORDER=OFF \
  -DNO_OUTPUTS=OFF \
  -DCELL_CONTAINER=SET \
  -DNEW_ANALYZE=OFF \
  -DOPTIONAL_CLAUSES=OFF \
  -DNOGUESS_VARS=OFF \
  ;
cmake --build buildafa_clause_heap

cmake -S . -B buildafa_trie_heap -DCMAKE_BUILD_TYPE=Release \
  -DMODE=AFA_TRIE_HEAP_HEAP \
  -DSTRENGTHENCC=ON \
  -DNO_POSNEG_OUTPUTS=ON \
  -DONE_ORDER=OFF \
  -DNO_OUTPUTS=OFF \
  -DCELL_CONTAINER=SET \
  -DNEW_ANALYZE=OFF \
  -DOPTIONAL_CLAUSES=OFF \
  -DNOGUESS_VARS=OFF \
  -DALL_SOLO=OFF \
  ;
cmake --build buildafa_trie_heap
```

We have run it as

```
./buildafa_trie_heap < path/to/benchmark.antisat
```

### ABC using IC3/PDR

We have downloaded it from https://github.com/berkeley-abc/abc at commit `a747f46292ec06278d02fbb6bc785dbefba54d8c`. We were running it on AIGER benchmarks (converted as `.afa -> .smv -> .aig`).

We have run it as

```
./build/abc -c "read_aiger path/to/benchmark.aig; drw; rf; b; drw; rwz; b; rfz; rwz; b; pdr -T 60"
```

### Mata

The emp wrapper was downloaded from https://github.com/VeriFIT/nfa-program-parser at commit `442c47517d1c9dbc5350f6af223179e2b7b98ae8`

The libmata was downloaded from https://github.com/VeriFIT/mata at commit `7a521f20780c7474f4ffc809c5004b9deebcceb2`

We have run it as

```
./nfa-program-parser/build/src/cpp/mata-emp-interpreter path/to/benchmark.emp path/to/benchmark.nfas/0.mata path/to/benchmark.nfas/1.mata ...
```


## Resulting benchmarks

The preprocessed AFA from which further conversions for specific tools were made are in `./afacomp_push_pos_not.tgz` (the format is described in the README of `https://github.com/p4l1ly/automata-safa`)

The benchmarks formatted for AntiSAT are in `./afacomp_simpl_tseytin.tgz` (it is a special format - CNF with AFA-specific header, not documented anywhere yet, the only reference as for now is the code of `automata-safa-one` or `antisat`)

The benchmarks formatted for ABC (AIGER) are in `./afacomp_simpl_aig.tgz`

The benchmarks formatted for Mata are in `./afacomp_emp.tgz` (see the Mata repositories for the format description)

All the compressed directories share the same structure.
They contain subdirectories with benchmark class names, each of which contain numbered instances.

## Preprocessing scripts

### Requirements:

We have used `ghc-9.4.8` and `cabal-3.10.2.0` and `python-3.11`.

First of all, you'll have to install the dependency of `automata-safa-one` from `https://github.com/p4l1ly/inversion-of-control/` at tag `sat2024` (`cabal install`).

Then, you'll have to install the `automata-safa-one` executable from this repository `https://github.com/p4l1ly/automata-safa` at tag `sat2024` (`cabal install automata-safa-one`).

### Patching the base benchmark set

If you want to generate the benchmarks yourself or understand how it was generated, you can start with the base benchmark set from `https://github.com/VeriFIT/automata-bench` by cloning it into the root directory of this repo (at commit `f2e2f6d952d23de15a48f9b4cf73e2a6db34d0c7`). 

The base benchmark repo is unfortunately not completely up to date, so you'll have to apply the following patches.

Copy the patch scripts from `./automata-bench-patches` to `./automata-bench`.

```
cd ./automata-bench
zsh regenerate_ltl.sh
zsh fix_nfa.sh
```

### Preprocessing

From the root directory of this repo, run (it will take few hours, the preprocessing scripts are not too optimized):

```
python3 afacomp.py
python3 simplify_once.py
python3 push_pos_not.py
```

### Formatting

Then, run (it will take some time):

```
python3 emp.py
python3 tseytin.py
python3 smv.py
python3 aig.py
```
