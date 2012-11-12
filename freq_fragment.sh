dir=$1
for treebank in `ls $dir/*tb`; do
    python discodop/fragments.py --numproc 0 $treebank > fragments/`basename $treebank`.frag
done
