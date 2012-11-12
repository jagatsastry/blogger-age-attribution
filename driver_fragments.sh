blog_dir=$1
if [ "" = "$blog_dir" ] ; then
    echo "Pass blog dir as an argument"
    exit 1
fi

mkdir -p treebanks
mkdir -p fragments
echo "Generating treebanks for the blog posts in $blog_dir"
python treegen.py $blog_dir
echo "Finished generating treebanks"
echo "Generating frequent fragments count now"
bash freq_fragment.sh treebanks
echo "Finished"

