#Distributes the xml files present in blogs dir to age based dirs
mkdir -p blogs/10s
mkdir -p blogs/20s
mkdir -p blogs/3040s

for filename in `ls blogs/| grep '\.1'`; do
    mv "blogs/$filename" blogs/10s
done

for filename in `ls blogs/| grep '\.2'`; do
    mv "blogs/$filename" blogs/20s
done

for filename in `ls blogs/| grep '\.3'`; do
    mv "blogs/$filename" blogs/3040s
done

for filename in `ls blogs/| grep '\.4'`; do
    mv "blogs/$filename" blogs/3040s
done

