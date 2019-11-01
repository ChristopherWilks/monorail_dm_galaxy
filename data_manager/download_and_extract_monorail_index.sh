#!/bin/bash

target_dir=$1
ref='hg38'

mkdir -p ${target_dir}/${ref}
for f in gtf.tar.gz unmapped_hisat2_idx.tar.gz salmon_index.tar.gz star_idx.tar.gz ; do
    curl http://snaptron.cs.jhu.edu/data/monorail/${ref}/${f} > ${target_dir}/${ref}/${f}
    pushd ${target_dir}/${ref}
    tar -zxvf ${f}
    popd
done 
