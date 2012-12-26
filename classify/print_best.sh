for file in `ls perf/*trigram*` ; do
    echo $file
    cut -d" " -f 1 $file | sort -u | tail -1
done
