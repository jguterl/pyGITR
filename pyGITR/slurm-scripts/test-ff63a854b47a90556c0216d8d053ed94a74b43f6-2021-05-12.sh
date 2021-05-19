#!/bin/bash

#SBATCH -e logs/test-ff63a854b47a90556c0216d8d053ed94a74b43f6-2021-05-12.%J.err
#SBATCH -o logs/test-ff63a854b47a90556c0216d8d053ed94a74b43f6-2021-05-12.%J.out
#SBATCH -J test-ff63a854b47a90556c0216d8d053ed94a74b43f6-2021-05-12

#SBATCH --partition=preemptable
#SBATCH --time=00:00:01

set -eo pipefail -o nounset


###
rm -f aaa; sleep 1000; echo 213 > aaa