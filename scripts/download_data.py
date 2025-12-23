import GEOparse
import pandas as pd

# Download the GEO series
gse = GEOparse.get_GEO("GSE280902")

# Get the expression matrix
expression_df = gse.pivot_samples('VALUE')

# Get phenotypes
phenotypes = {}
for gsm_name, gsm in gse.gsms.items():
    # Extract response from metadata
    # Assuming 'characteristics_ch1' has the response info
    chars = gsm.metadata['characteristics_ch1']
    response = None
    for char in chars:
        if 'response' in char.lower():
            if 'responder' in char.lower():
                response = 1
            elif 'non-responder' in char.lower():
                response = 0
    phenotypes[gsm_name] = response

# Create labels df
labels_df = pd.DataFrame.from_dict(phenotypes, orient='index', columns=['Response'])

# Save
expression_df.to_csv('processed/cleaned_expression.csv')
labels_df.to_csv('processed/labels.csv')

print("Data downloaded and processed.")