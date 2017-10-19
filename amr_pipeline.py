#!/usr/bin/env python
import argparse
from fabric.operations import local


TRIMMOMATIC_PATH = "/home/ksnavely/programming/emily/java/Trimmomatic-0.36"
INPUT_DATA_PATH = TRIMMOMATIC_PATH


def parse_args():
    parser = argparse.ArgumentParser(description='Runs trimmomatic')
    parser.add_argument("prefix", help="The input file prefix; also the output file prefix")
    args = parser.parse_args()
    return args


def trim(prefix):
    file1 = "{}_R1.fastq.gz".format(prefix)
    file2 = "{}_R2.fastq.gz".format(prefix)
    trimlog = "{}.trimlog"
    local(
        "java -jar {}/trimmomatic-0.36.jar PE -phred33 {} {} -trimlog {} -baseout {}.fq.gz ILLUMINACLIP:{}/adapters/NexteraPE-PE.fa:2:30:10:8:true HEADCROP:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36".format(
            TRIMMOMATIC_PATH,
            "{}/{}".format(INPUT_DATA_PATH, file1),
            "{}/{}".format(INPUT_DATA_PATH, file2),
            trimlog,
            prefix,
            TRIMMOMATIC_PATH
        )
    )


if __name__ == "__main__":
    args = parse_args()
    trim(args.prefix)
