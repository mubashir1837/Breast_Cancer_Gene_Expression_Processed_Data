import pandas as pd

# Mapping from GSM to response (1: responder, 0: non-responder)
gsm_to_response = {
    'GSM8607304': 0, 'GSM8607305': 1, 'GSM8607306': 1, 'GSM8607307': 0, 'GSM8607308': 1,
    'GSM8607309': 1, 'GSM8607310': 1, 'GSM8607311': 0, 'GSM8607312': 1, 'GSM8607313': 0,
    'GSM8607314': 0, 'GSM8607315': 1, 'GSM8607316': 0, 'GSM8607317': 1, 'GSM8607318': 0,
    'GSM8607319': 0, 'GSM8607320': 1, 'GSM8607321': 1, 'GSM8607322': 1, 'GSM8607323': 1,
    'GSM8607324': 1, 'GSM8607325': 0, 'GSM8607326': 0, 'GSM8607327': 1, 'GSM8607328': 0,
    'GSM8607329': 1, 'GSM8607330': 0, 'GSM8607331': 1, 'GSM8607332': 0, 'GSM8607333': 0,
    'GSM8607334': 1, 'GSM8607335': 0, 'GSM8607336': 0, 'GSM8607337': 0, 'GSM8607338': 0,
    'GSM8607339': 0, 'GSM8607340': 1, 'GSM8607341': 1, 'GSM8607342': 0, 'GSM8607343': 0,
    'GSM8607344': 1, 'GSM8607345': 1, 'GSM8607346': 1, 'GSM8607347': 1, 'GSM8607348': 1,
    'GSM8607349': 0, 'GSM8607350': 1, 'GSM8607351': 1, 'GSM8607352': 0, 'GSM8607353': 1,
    'GSM8607354': 0, 'GSM8607355': 0, 'GSM8607356': 0, 'GSM8607357': 0, 'GSM8607358': 0,
    'GSM8607359': 1, 'GSM8607360': 1, 'GSM8607361': 0
}

# Mapping from GSM to raw sample name
gsm_to_title = {
    'GSM8607304': '014B-Tn_S14', 'GSM8607305': '018B-Bp-C_S12', 'GSM8607306': '047B-Bn-C_S3',
    'GSM8607307': '050B-A_S9', 'GSM8607308': '051B-Bn-C_S4', 'GSM8607309': '058-B_S1',
    'GSM8607310': '065BBn-C_S9', 'GSM8607311': '066-B_S3', 'GSM8607312': '069B_S4',
    'GSM8607313': '084B-Bn_S10', 'GSM8607314': '090B-Bn_S6', 'GSM8607315': '108-B_S4',
    'GSM8607316': '115-B_S7', 'GSM8607317': '116BBp-C_S11', 'GSM8607318': '117B-Bp_S3',
    'GSM8607319': '125B-Bn_S10', 'GSM8607320': 'B138_S11', 'GSM8607321': '142B-Bp-C_S2',
    'GSM8607322': '145B-Bp-C_S1', 'GSM8607323': '146BBp-C_S7', 'GSM8607324': '155B-Bn-C_S1',
    'GSM8607325': '160B-A_S11', 'GSM8607326': '163B_S11', 'GSM8607327': '175B-Bp-C_S11',
    'GSM8607328': '187B-Bn_S14', 'GSM8607329': '188B-Bn-C_S16', 'GSM8607330': '189B_S12',
    'GSM8607331': '200B-Tn-C_S4', 'GSM8607332': 'B205_S12', 'GSM8607333': '208B-Bp_S8',
    'GSM8607334': '213B-H2-C_S5', 'GSM8607335': '219B-Bn_S16', 'GSM8607336': '226B-Tn_S12',
    'GSM8607337': '239B-Bn_S1', 'GSM8607338': '247B-A_S1', 'GSM8607339': '255B-H2_S9',
    'GSM8607340': '260B-Bp-C_S5', 'GSM8607341': '261B-Bp-C_S15', 'GSM8607342': '275B-A_S6',
    'GSM8607343': '277B-Bp_S13', 'GSM8607344': '293BA-C_S15', 'GSM8607345': '295-B_S8',
    'GSM8607346': '300B_S6', 'GSM8607347': '307-B_S7', 'GSM8607348': '309B_S5',
    'GSM8607349': '314B-Bn_S9', 'GSM8607350': '315B-Tn-C_S4', 'GSM8607351': 'F07B-Tn-C_S3',
    'GSM8607352': 'F08B-Bn_S8', 'GSM8607353': 'F20B-Bn-C_S13', 'GSM8607354': 'F31B-Bn_S10',
    'GSM8607355': 'F34-B_S9', 'GSM8607356': 'F51B-Bn_S7', 'GSM8607357': 'F58B-Tn_S2',
    'GSM8607358': 'F70B-Bn_S15', 'GSM8607359': 'F71B-Tn-C_S2', 'GSM8607360': 'F80-B_S2',
    'GSM8607361': 'F81-B_S3'
}

# Create labels dict for raw sample names
labels = {}
for gsm, title in gsm_to_title.items():
    raw_name = ('X' + title) if title[0].isdigit() else title
    labels[raw_name] = gsm_to_response[gsm]

# --- STEP 1: Load raw expression data ---
file_path = "raw/GSE280902_RawData.txt"
df = pd.read_csv(file_path, sep="\t", index_col=0)

# --- STEP 2: Check shape & head ---
print("Original shape:", df.shape)
print(df.head())

# --- STEP 3: Transpose expression matrix to have samples as rows ---
X = df.T
print("Transposed shape:", X.shape)

# --- STEP 4: Create labels DataFrame ---
label_df = pd.DataFrame.from_dict(labels, orient="index", columns=["Response"])

# --- STEP 5: Merge expression with labels ---
final_df = X.merge(label_df, left_index=True, right_index=True)

# --- STEP 6: Save cleaned data ---
final_df.to_csv("processed/cleaned_expression.csv")
label_df.to_csv("processed/labels.csv")

print("Data cleaning complete: cleaned_expression.csv and labels.csv saved in processed folder")
