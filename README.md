# fao-repro-harness

Autonomous reproducibility & QC gating harness for cancer immunology / fatty acid oxidation (FAO) scRNA-seq and CRISPR screening papers, built for `@BioReproBot` (Devin Bots).

## Architecture
1. **Policy / Verification Separation**: Raw datasets are read-only; statistical gating (missing rate, positive-control gene direction, FDR threshold) is enforced deterministically via `pytest` (`tests/test_qc_gate.py`), never by LLM visual inspection.
2. **Hybrid Execution**: Devin Bot handles dependency repair (`Dockerfile` / `renv.lock`), 5% stratified subsample smoke tests, and PR generation; full-scale jobs dispatch to a local Nextflow node (`main.nf`).
3. **Failure Triage**: Unreproducible papers due to missing raw data or undocumented hyperparameters trigger a structured Reproducibility Audit Card instead of burning compute in infinite retry loops.
