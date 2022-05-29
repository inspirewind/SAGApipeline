uniport_seed = r'D:\new_ncbi_dataset\protein\seed_algae_mix.fasta'
uniport_total = r'D:\new_ncbi_dataset\protein\total_algae_mix.fasta'
nr_extract = r'D:\new_ncbi_dataset\protein\nr_extract.fasta'
busco_mix = r'D:\new_ncbi_dataset\protein\busco_mix.fasta'


seed_out = "seed.out"
out = open("busco_mix.out", 'w')
with open(busco_mix) as f:
    for line in f:
        if line.startswith(">"):
            out.writelines(line)
out.close()
