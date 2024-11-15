#/usr/bin/env bash

set -e

readme='README.md'

content="# Advent of Code\n\nhttps://adventofcode.com/\n\n# Table of contents\n"
content_toc=""
content_stats=""

get_stat() {
    dir=$1
    year=$2
    day_num=$(echo ${dir: -2} | bc)
    main=$dir/main.py
    loc=$(wc -l <$main)
    flake=$(flake8 --max-line-length=120 $main | wc -l)
    fors=$(grep -E '(\s|^)for(\s|$)' $main | wc -l)
    whiles=$(grep -E '(\s|^)while(\s|$)' $main | wc -l)

    mkdir -p tmp/
    echo "$year | $day_num | $loc | $flake | $fors | $whiles" >>tmp/$year.stats
}
for yeardir in ../20*; do
    year=${yeardir: -4}
    echo $yeardir
    content_toc=$content_toc"\n[$year](#$year)"
    content_stats=$content_stats"\n## $year\nYear | Day | LOC | \`flake8\` | \`for\` | \`while\`\n--- | --- | --- | --- | --- | ---\n"

    rm -rf tmp/$year.stats
    for dir in $yeardir/d*; do
        get_stat $dir $year &
    done
    wait

    content_stats="$content_stats""$(cat tmp/$year.stats | sort -V)"

done

echo -e $content$content_toc"\n""$content_stats" >$readme
