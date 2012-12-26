mkdir csvs
mkdir perf
for file in `ls $1/*.dat` ; do
    filename=`basename $file`
    echo "Considering $filename"
    python ~/nlp_project/svm_to_csv.py $file > csvs/"$filename".csv 
#    python classify_scikit_ccf.py csvs/"$filename".csv > perf/"$filename"_perf &
    if [ $? -ne 0 ] ; then
        exit 1
    fi
done
