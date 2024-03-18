IFILE=$1
ODIR=$2

i=1
cat $IFILE | while read -r ltl; do
  echo $i
  automata-safa-one ltlToPretty <<< "$ltl" > $ODIR/$i.afa
  i=$(($i + 1))
done
