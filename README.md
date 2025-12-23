# Breast Cancer Gene Expression Dataset

This dataset contains RNA-seq gene expression data from 58 breast cancer patients treated with neoadjuvant chemotherapy (NAC). The data is derived from GSE280902 on NCBI GEO.

## Files

- `cleaned_expression.csv`: Gene expression matrix with 58 samples (rows) and 28,278 genes (columns). The last column is 'Response' (1 for responder, 0 for non-responder).
- `labels.csv`: Sample labels with response to NAC.
- `notebooks/exploration.ipynb`: Jupyter notebook for data exploration, including EDA and PCA visualization.

## Data Description

- **Samples**: 58 breast cancer patients (29 responders, 29 non-responders to NAC).
- **Genes**: 28,278 protein-coding genes.
- **Response**: 1 = Pathological Complete Response (pCR), 0 = No Response.

## Source

- GEO Accession: GSE280902
- Paper: Guevara-Nieto HM et al. Identification of predictive pretreatment biomarkers for neoadjuvant chemotherapy response in Latino invasive breast cancer patients. Mol Med 2025.
- GitHub Repository: [Breast Cancer Gene Expression Processed Data](https://github.com/mubashir1837/Breast_Cancer_Gene_Expression_Processed_Data)

## Usage

This dataset can be used for machine learning models to predict NAC response in breast cancer based on gene expression profiles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.