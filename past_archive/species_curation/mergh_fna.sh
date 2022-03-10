#!/bin/bash
path = `pwd`
ls $path | while read line
do
    if test -d $line
    then
        cat ./$line/*.fna > ./$line/merge.fna
        echo "$line merge finished!"
    fi
done
