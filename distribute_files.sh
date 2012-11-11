#Distributes the xml files present in blogs dir to age based dirs

for filename in `ls | grep '\.1'`; do
    mv "$filename" 10s
done

for filename in `ls | grep '\.2'`; do
    mv "$filename" 20s
done

for filename in `ls | grep '\.3'`; do
    mv "$filename" 3040s
done

for filename in `ls | grep '\.4'`; do
    mv "$filename" 3040s
done

    
