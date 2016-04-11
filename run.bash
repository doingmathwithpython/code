#!/bin/bash

set -e

python3 -c "import sys;print(sys.version)"
python3 -c "import sympy;print(sympy.__version__)"
python3 -c "import matplotlib; print(matplotlib.__version__)"

for dir in 'chapter1' 'chapter2' 'chapter3' 'chapter4' 'chapter5' 'chapter6' 'chapter7'; do
    pushd $dir/solutions
    ./run.bash
    popd
done
