#!/bin/bash
echo -e "The pipeline of gene prediction and scanning protein domain"
echo -e "Author: inspirewind\ne-mail: Lr2001912@gmail.com\n"

echo -e "The default pipeline is:"
echo -e "1. gunzip *.fna.gz"
echo -e "2. RepeatMasker *.fna"
echo -e "3. augustus fna.masked.fa"
echo -e "4. extract_cds.py"
echo -e "5. hmmscan"
echo -e "You can specify specific parameters\n"

echo -e "Make sure the current dir has a 'genome' dir"
echo -e "searching genome dir:"
if [ -d "genome" ]
then
    echo -e "genome dir existed!"
    echo -e "working abspath is: $(pwd)""/genome\n"
    wdir="$(pwd)""/genome"
else
    echo "'genome' is not existed!"
    exit 1
fi

echo -e "Start running......"
echo -e "Start Time:" "$(date)\n"

echo -e "Traversing the folder......"
cdir=$(pwd)
wdir="$(pwd)""/genome"
genome_dir_cnt=0
function getdir(){
    # echo $1
    for dir in $1/*
    do
    if test -d $dir
    then
        # echo $dir
        ((genome_dir_cnt++))
        arr=(${arr[*]} $dir)
    fi
    done
}
getdir $wdir
echo -e "$genome_dir_cnt dir detected!"


ShowAllDir=""
read -p "Do you want to show ALL? [Y/n]: " ShowAllDir
case "${ShowAllDir}" in
[yY][eE][sS] | [yY])
    for dir in ${arr[@]}
    do
        echo $dir
    done
    ;;
[nN][oO] | [nN])
    echo "You choose do not show"
    ;;
*)
    echo "No input, dirs will not show"
    ;;
esac


StartThePipeline=""
echo -e "Do you want to continue pipeline?"
read -p "Default continue,Enter your choice [Y/n]: " StartThePipeline
case "${StartThePipeline}" in
[yY][eE][sS] | [yY])
    echo -e "\nYou choose Yes! Pipeline will run! "
    ;;
[nN][oO] | [nN])
    echo "exit!"
    ;;
*)
    echo "No input, will continue pipeline."
    ;;
esac

if [[ $StartThePipeline == 'n' ]]; then
    exit 1
fi


mkdir rec
echo -e "rec dir had made, all results are in ./rec"
echo -e "./ is the dir where run.sh in\n"
cd genome
working_cnt=1
for i in ${arr[@]}
do
    cd $i
    last_dir=$(basename $(pwd))
    echo -e "enter dir[$working_cnt]: $last_dir\t""total dirs: $genome_dir_cnt"
    # echo -e "pwd: $(pwd)"

    gunzip -kv *.fna.gz
    echo -e "gunzip finished!\n"

    echo -e "Starting RepeatMasker"
    mkdir repeat
    RepeatMasker -pa 4 -species "Arabidopsis thaliana" -poly -html -gff -dir repeat *.fna

    # cd repeat
    echo -e "Starting augustus"
    echo -e "Be patient, augustus has no comments"
    augustus --species=arabidopsis ./repeat/*.fna.masked > output.gff
    echo -e "augustus finished"

    echo -e "Starting merge cds by python......"
    cp $cdir/merge.py merge.py
    python3 merge.py
    echo -e "merged!\n"
    rm merge.py

    echo -e "starting hmmscan......"
    hmmscan -o hmmout.txt --tblout hmmout.tbl --domtblout hmmout.dom --noali -E 1e-5 ../../pfam/Pfam-A.hmm merge.fasta
    echo -e "scanning finished!\n"
    echo -e "------------------"
    echo -e "pipeline finished!"
    echo -e "------------------\n"
    ((working_cnt++))
done
