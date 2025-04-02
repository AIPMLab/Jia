
from sklearn.model_selection import train_test_split
import pandas as pd

dataPath = dataPath =  "D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/t1+t2+t1Gd+flair_all/s1_combined_modalities_965.csv"
data = pd.read_csv(dataPath)
# Split the dataset
train_df, test_df = train_test_split(data, test_size=0.3, random_state=42)

# Save the training set and test set as CSV files
train_df.to_csv(
    'D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/2_2_all_feature_divide_train_test/Total_GBM+LGG_t1+t2+t2Gd+flair_s1_all_feature_train_icc.csv', index=False)
test_df.to_csv(
    'D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/t1+t1Gd+t2+flair/2_2_all_feature_divide_train_test/Total_GBM+LGG_t1+t2+t2Gd+flair_s1_all_feature_test_icc.csv', index=False)
