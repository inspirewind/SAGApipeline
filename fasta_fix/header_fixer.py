class fixer:
    # fix and optimize the fasta header and bam reference
    def __init__(self) -> None:
        pass

    def fix_contig_name(self, input_path : str, output_path : str):
        f = open(input_path, 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('>'):
                lines[i] = lines[i].split(' ')[0].replace(' ', '') + '\n'
        with open(output_path, 'w') as out:
            out.writelines(lines)


    def fix_bam_ref(self):
        pass

# fx = fixer()
# fx.fix_contig_name('D:\working_dir_fix\GCF_002220235.1\merge.fna')