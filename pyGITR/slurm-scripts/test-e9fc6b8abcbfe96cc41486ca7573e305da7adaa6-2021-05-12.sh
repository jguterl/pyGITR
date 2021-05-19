#!/bin/bash

#SBATCH -e logs/test-e9fc6b8abcbfe96cc41486ca7573e305da7adaa6-2021-05-12.%J.err
#SBATCH -o logs/test-e9fc6b8abcbfe96cc41486ca7573e305da7adaa6-2021-05-12.%J.out
#SBATCH -J test-e9fc6b8abcbfe96cc41486ca7573e305da7adaa6-2021-05-12

#SBATCH --partition=preemptable
#SBATCH --time=00:00:01

set -eo pipefail -o nounset


###
rm -f aaa; sleep 10; echo 213 > aaa