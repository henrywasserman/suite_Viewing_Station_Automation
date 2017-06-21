#!/bin/sh

#usage [classpath] [image1] [image2] [expectDifference]

echo Here is \$1 $1
echo Here is \$2 $2
echo Here is \$3 $3
echo Here is \$4 $4

java -cp $1 image.compare.CompareImages $2 $3 $4
