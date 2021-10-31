GEN_WITH_BAM_INDEX = ['GCA_001275005.1', 'GCA_001430745.1', 'GCA_002005505.1', 'GCA_002049455.2', 
'GCA_002205965.3', 'GCA_002245815.2', 'GCA_002284615.2', 'GCA_002891735.1', 'GCA_003116995.1', 
'GCA_003130725.1', 'GCA_003346895.1', 'GCA_003613005.1', 'GCA_003970955.1', 'GCA_004138255.1', 
'GCA_004431415.1', 'GCA_006384855.1', 'GCA_007859695.1', 'GCA_008690995.1', 'GCA_008729055.1', 
'GCA_009720205.1', 'GCA_009829735.1', 'GCA_011316045.1', 'GCA_012295225.1', 'GCA_013995675.1', 
'GCA_015473125.1', 'GCA_015712045.1', 'GCA_016834595.1', 'GCA_016834605.1', 'GCA_016858145.1', 
'GCA_018136815.1', 'GCA_018697155.1', 'GCA_019155205.1', 'GCA_900108755.1', 'GCA_900538255.1', 
'GCA_902809745.2', 'GCF_000002595.1', 'GCF_000090985.2', 'GCF_000147415.1', 'GCF_000214015.3', 
'GCF_000341285.1', 'GCF_000350225.1', 'GCF_000611645.1', 'GCF_000733215.1', 'GCF_002220235.1']
rule all:
    input:
        expand("test_etmode/{gen}/braker/", gen=GEN_WITH_BAM_INDEX)

rule braker2:
    input:
        fna="test_etmode/{gen}/merge_fix.fna",
        bam="test_etmode/{gen}/VARUS.bam"
    output:
        directory("test_etmode/{gen}/braker/")
    threads: 6
    shell:
        "braker.pl --genome={input.fna} --species=com_1030et_{wildcards.gen} --bam={input.bam} --cores {threads} --min_contig=200 --workingdir=test_etmode/{wildcards.gen}/braker"

