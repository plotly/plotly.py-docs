#!/bin/bash

rm -rf build
mkdir build

grep -l v4upgrade notebooks/*md | sed 's/^notebooks\///g' | sed 's/\.md$//g' | while read NB; do

  jupytext notebooks/$NB.md --to notebook --output build/$NB.ipynb
  PLOTLY_RENDERER=notebook_connected jupyter nbconvert build/$NB.ipynb --template nb.tpl --execute

done
