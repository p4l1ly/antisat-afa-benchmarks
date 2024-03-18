zsh ltls_to_afas.sh ./ltl_afa/random_ltl/{ltls,afas}
zsh ltls_to_afas.sh ./ltl_afa/parametric_ltl/{lift,lift_afas}
zsh ltls_to_afas.sh ./ltl_afa/parametric_ltl/{counter,counter_afas}
for f in $(find . -type f | grep '\.ltlf$'); do echo $f; cat $f | ltl-translators-exe ltlf | automata-safa-one ltlToPretty > /tmp/afa && mv /tmp/afa ${f:0:-4}afa; done
for f in $(find . -type f | grep '\.pltl$'); do echo $f; cat $f | ltl-translators-exe pltl | automata-safa-one ltlToPretty > /tmp/afa && mv /tmp/afa ${f:0:-4}afa; done
