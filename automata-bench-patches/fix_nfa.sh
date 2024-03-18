for f in $(find . -type f | grep 'gen_aut.*\.mata$'); do python3 fix_nfa.py $f; done 
