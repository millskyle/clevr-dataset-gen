
function ducksballs () {
    ducks=$1
    balls=$2
    for run in c; do 
#        for scene in vancouver mountains vancouver2 lake; do
            node=$(echo -e "bumblebee\nstarscream\nshockwave\nratchet\narcee" | shuf | head -n 1)
            sbatch -J ${run}${ducks}ducks -p cpu submit.s $ducks $balls $run
 #       done
    done
}



for pair in $(cat combos); do
    echo ducksballs $(echo $pair | sed  's|-| |')
    ducksballs $(echo $pair | sed  's|-| |')
done

