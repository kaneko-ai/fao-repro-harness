nextflow.enable.dsl = 2

params.input_h5ad = "data/subsample_5pct.h5ad"
params.outdir     = "outputs"

process RUN_QC_AND_GATE {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path h5ad

    output:
    path "qc_summary.json"

    script:
    """
    python3 scripts/run_repro_qc.py --input ${h5ad} --out qc_summary.json
    """
}

workflow {
    Channel.fromPath(params.input_h5ad) | RUN_QC_AND_GATE
}
