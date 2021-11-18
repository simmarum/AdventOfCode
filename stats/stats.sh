#/usr/bin/env bash

set -e

readme='README.md'

content="# Advent of Code\n\nhttps://adventofcode.com/\n\n# Table of contents\n"
content_toc=""
content_stats=""

for yeardir in ../20*; do
    year=${yeardir: -4}
    echo $yeardir
    content_toc=$content_toc"\n[$year](#$year)"
    content_stats=$content_stats"\n## $year\nYear | Day | LOC | \`flake8\` | \`for\` | \`while\`\n--- | --- | --- | --- | --- | ---\n"

    for dir in $yeardir/d*; do
        echo $dir
        main=$dir/main.py
        loc=$(wc -l < $main)
        flake=$(flake8 --max-line-length=99 $main | wc -l)
        fors=$(grep -E '(\s|^)for(\s|$)' $main | wc -l)
        whiles=$(grep -E '(\s|^)while(\s|$)' $main | wc -l)
        day_num=$(echo ${dir: -2} | bc)
        content_stats=$content_stats"$year | $day_num | $loc | $flake | $fors | $whiles\n"
    done
done

echo -e $content$content_toc"\n"$content_stats > $readme
