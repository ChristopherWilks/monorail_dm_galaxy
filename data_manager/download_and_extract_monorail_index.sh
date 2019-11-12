#!/bin/bash

target_dir=$1
#e.g. "hg38" or "ath10"
ref=$2

if [[ -z $ref ]]; then
   ref='ath10'
fi 

mkdir -p ${target_dir}/${ref}
for f in gtf.tar.gz unmapped_hisat2_idx.tar.gz salmon_index.tar.gz star_idx.tar.gz ; do
    curl http://snaptron.cs.jhu.edu/data/monorail/${ref}/${f} > ${target_dir}/${ref}/${f}
    pushd ${target_dir}/${ref}
    tar -zxvf ${f}
    popd
done 
