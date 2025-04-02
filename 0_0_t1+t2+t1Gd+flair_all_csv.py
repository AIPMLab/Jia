import pandas as pd
import os

def merge_modalities_and_save(output_path):
    # Load four modal files
    t1 = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/0_total_csv/Total_GBM+LGG_t1_s1_add_os_age_gender_label.csv")#change path
    t1gd = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/0_total_csv/Total_GBM+LGG_t1Gd_s1_add_os_age_gender_label.csv")
    t2 = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/0_total_csv/Total_GBM+LGG_t2_s1_add_os_age_gender_label.csv")
    flair = pd.read_csv("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/0_total_csv/Total_GBM+LGG_flair_s1_add_os_age_gender_label.csv")

    # Add a modality tag before the feature name to distinguish which modality the feature comes from
    t1 = t1.add_prefix('T1_')
    t1gd = t1gd.add_prefix('T1GD_')
    t2 = t2.add_prefix('T2_')
    flair = flair.add_prefix('FLAIR_')

    # Extract the label column and make sure the label column is consistent
    labels = t1[['T1_label', 'T1_OS', 'T1_OS.time', 'T1_index', 'T1_age_at_index', 'T1_gender']]
    labels = labels.rename(columns={
        'T1_label': 'label',
        'T1_OS': 'OS',
        'T1_OS.time': 'OS.time',
        'T1_index': 'index',
        'T1_age_at_index': 'age_at_index',
        'T1_gender': 'gender'
    })

    # Remove useless label columns to merge features
    t1 = t1.drop(columns=['T1_label', 'T1_OS', 'T1_OS.time', 'T1_index', 'T1_age_at_index', 'T1_gender'])
    t1gd = t1gd.drop(columns=['T1GD_label', 'T1GD_OS', 'T1GD_OS.time', 'T1GD_index', 'T1GD_age_at_index', 'T1GD_gender'])
    t2 = t2.drop(columns=['T2_label', 'T2_OS', 'T2_OS.time', 'T2_index', 'T2_age_at_index', 'T2_gender'])
    flair = flair.drop(columns=['FLAIR_label', 'FLAIR_OS', 'FLAIR_OS.time', 'FLAIR_index', 'FLAIR_age_at_index', 'FLAIR_gender'])

    # Merge features from all modeslities
    combined_features = pd.concat([t1, t1gd, t2, flair], axis=1)

    # Merging labels and features
    combined_data = pd.concat([labels, combined_features], axis=1)

    # Make sure the output path exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the merged file
    combined_data.to_csv(output_path, index=False)
    print(f"The merged file has been saved to: {output_path}")

# Call the function and set the output path
output_file_path = "D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/t1+t2+t1Gd+flair_all/s1_combined_modalities.csv"
merge_modalities_and_save(output_file_path)
