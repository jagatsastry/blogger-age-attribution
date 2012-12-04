#dir="treebanks"
#mkdir all_processed_tb
res=`ls treebanks/*tb`
for treebank in $res; do
    python discodop/fragments.py  $treebank > fragments/`basename $treebank`.frag
    if [ $? -eq 0 ] ; then
        mv $treebank all_processed_tb
        sed -i "s/  */ /g" fragments/`basename $treebank`.frag
    fi
done
