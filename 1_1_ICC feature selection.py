import pandas as pd

# Read train.csv file
train_df = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/1_files/Total_GBM+LGG_t1Gd_s1_add_os_age_gender_label.csv")

# Read train_t2_icc.csv file
icc_df = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/2_1_calculate icc/Total_GBM+LGG_t1Gd_s+s1_ICC_965.csv")

# Filter selected features based on ICC values greater than 0.8
selected_feature_names = icc_df.loc[icc_df['icc'] >= 0.8, 'FeatureName']

# Keep only selected features along with label from train.csv
train_icc_selection_df = train_df[list(selected_feature_names)+["label","index","OS","OS.time","age_at_index","gender"]]

# Save the DataFrame with label as train_t2_icc_selection.csv
train_icc_selection_df.to_csv(
    "D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/2_2_select icc/Total_GBM+LGG_t1Gd_s1_secect_icc.csv", index=False)