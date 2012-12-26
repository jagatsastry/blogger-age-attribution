blog_dir=$1
if [ "" = "$blog_dir" ] ; then
    echo "Pass blog dir as an argument"
    exit 1
fi

mkdir -p treebanks
mkdir -p fragments
exitStatus=1
echo "Generating treebanks for the blog posts in $blog_dir"
while [ $exitStatus -ne 0 ] ; do
    sleep 5
    echo "Trying (possibly again)"
    python treegen.py $blog_dir
    exitStatus=$?
    if [ $exitStatus -eq 0 ] ; then
        echo "Finished generating treebanks"
        echo "Generating frequent fragments count now"
#        bash freq_fragment.sh treebanks
        echo "Finished"
    fi

done
