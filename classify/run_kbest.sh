mkdir perf
for file in `ls csvs/*trigram*.csv` ; do
    filename=`basename $file`
    echo "Considering $filename"
    python classify_scikit_ccf.py csvs/"$filename" > perf/"$filename".perf &
    if [ $? -ne 0 ] ; then
        exit 1
    fi
done
