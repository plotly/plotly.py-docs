#!/bin/bash

rm -rf build
mkdir build
mkdir build/html
mkdir build/failures

grep -l v4upgrade notebooks/*md | sed 's/^notebooks\///g' | sed 's/\.md$//g' | while read NB; do

  jupytext notebooks/$NB.md --to notebook --output build/$NB.ipynb
  PLOTLY_RENDERER=notebook_connected jupyter nbconvert build/$NB.ipynb \
    --to html --output html/2019-07-03-$NB.html --template nb.tpl --execute \
    &> build/failures/$NB && rm build/failures/$NB

done
