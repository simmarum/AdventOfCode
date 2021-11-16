#/usr/bin/env bash

set -e

template='README.md.template'
readme='README.md'
stats_match='sed-day-stats'

cp $template $readme

for yeardir in ../20*; do
    year=${yeardir: -4}
    echo $yeardir
    for dir in $yeardir/d*; do
        echo $dir
        main=$dir/main.py
        loc=$(wc -l < $main)
        flake=$(flake8 $main | wc -l)
        fors=$(grep -E '(\s|^)for(\s|$)' $main | wc -l)
        whiles=$(grep -E '(\s|^)while(\s|$)' $main | wc -l)
        day_num=$(echo ${dir: -2} | bc)
        line="$year | $day_num | $loc | $flake | $fors | $whiles"
        gsed -i "/$stats_match/i $line" $readme
    done
done

gsed -i "s/$stats_match//g" $readme
