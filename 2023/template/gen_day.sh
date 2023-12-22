#!/bin/bash
mkdir ../$1
cp step* ../$1
for f in ../$1/step*py; do
echo $f
sed -i '' "s/^_DAY = .*$/_DAY = $1/" $f
done
