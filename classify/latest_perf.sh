for file in `ls -t perf` ; do 
    echo $file
    tail -1 perf/$file ;  
done
