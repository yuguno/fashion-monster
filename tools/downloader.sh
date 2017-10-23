#!/bin/sh

filename=$1
dirname=$2

mkdir "./${dirname}"
cat ${filename} | while read line
do
    wget ${line} -P "./${dirname}"
done