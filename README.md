# Aarskog–Scott Syndrome Trio Genomics

This repository contains the computational workflow and project documentation for genomic analysis of an Aarskog–Scott syndrome family trio.

The analysis is performed using Illumina sequencing data and focuses on:

- SNVs and small indels
- copy-number variants
- structural variants
- trio inheritance patterns
- X-linked inheritance
- candidate variants in `FGD1`
- splice-effect prediction and functional interpretation

## Workflow

Primary variant calling is performed using:

- Nextflow
- nf-core/sarek
- Seqera Platform / Tower
- AWS Batch

Planned variant calling and annotation include:

- GATK HaplotypeCaller
- DeepVariant
- Manta
- TIDDIT
- CNV analysis
- Ensembl VEP
- SpliceAI

Candidate variants may undergo additional interpretation using AlphaGenome, IGV inspection, segregation analysis, and Sanger validation.

## Study design

The project contains sequencing data from three related individuals analysed jointly as a family.

Family relationships and phenotype information are recorded separately in the project metadata.

## Repository structure

```text
aarskog-scott-syndrome/
├── config/       # nf-core/sarek and Seqera configuration
├── metadata/     # sample sheets and pedigree files
├── scripts/      # downstream analysis scripts
├── docs/         # analysis notes and manuscript documentation
├── results/      # derived analysis outputs
└── logs/         # pipeline and analysis logs