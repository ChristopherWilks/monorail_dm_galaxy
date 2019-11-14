#!/bin/bash

target_dir=$1
#e.g. http://snaptron.cs.jhu.edu/data/monorail/1.0.0/ath10 or http://snaptron.cs.jhu.edu/data/monorail/1.0.0/hg38
ref=$2

if [[ -z $ref ]]; then
   ref='http://snaptron.cs.jhu.edu/data/monorail/1.0.0/ath10'
fi 

url=$ref
ref=$(basename $url)

mkdir -p ${target_dir}/${ref}
for f in gtf.tar.gz unmapped_hisat2_idx.tar.gz salmon_index.tar.gz star_idx.tar.gz ; do
    curl ${url}/${f} > ${target_dir}/${ref}/${f}
    pushd ${target_dir}/${ref}
    tar -zxvf ${f}
    popd
done 
