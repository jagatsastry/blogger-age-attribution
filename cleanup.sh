dir=$1
for file in `ls $dir` ; do
    filename="$dir/$file"
    echo "handling $filename"
    dos2unix $filename
#    sed -i "s/&/_and_/g" $filename
#    sed -i "s/<3/_HEART_/g" $filename
    #perl -pi -e 's/[[:^ascii:]]//g'  $filename
done

