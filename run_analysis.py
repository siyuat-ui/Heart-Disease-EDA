"""
Full pipeline script for Heart dataset EDA.
- Handles preprocessing, feature renaming, and filtering
- Generates numerical and categorical feature plots
- Computes correlations (Pearson, point-biserial, Cramer's V)
- Saves all outputs to results folder
- Includes progress indicators
"""

import subprocess
import sys
import warnings
warnings.filterwarnings('ignore')

# -------------------------------
# Step 0: Install dependencies
# -------------------------------
def install_dependencies():
    print("Installing dependencies from requirements.txt ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed.\n")

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
except ImportError:
    install_dependencies()
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

# -------------------------------
# Step 1: Load & preprocess data
# -------------------------------
print("Step 1/5: Loading and preprocessing data...")
data = pd.read_csv('data/raw/heart.csv')

# Filter faulty points
data = data[data['ca'] < 4]
data = data[data['thal'] > 0]

# Rename columns
data = data.rename(columns={
    'cp':'chest_pain_type',
    'trestbps':'resting_blood_pressure',
    'chol': 'cholesterol',
    'fbs': 'fasting_blood_sugar',
    'restecg' : 'resting_electrocardiogram',
    'thalach': 'max_heart_rate_achieved',
    'exang': 'exercise_induced_angina',
    'oldpeak': 'st_depression',
    'slope': 'st_slope',
    'ca':'num_major_vessels',
    'thal': 'thalassemia'
})

# Map categorical values
data.loc[data['sex'] == 0, 'sex'] = 'female'
data.loc[data['sex'] == 1, 'sex'] = 'male'

data.loc[data['chest_pain_type'] == 0, 'chest_pain_type'] = 'typical angina'
data.loc[data['chest_pain_type'] == 1, 'chest_pain_type'] = 'atypical angina'
data.loc[data['chest_pain_type'] == 2, 'chest_pain_type'] = 'non-anginal pain'
data.loc[data['chest_pain_type'] == 3, 'chest_pain_type'] = 'asymptomatic'

data.loc[data['fasting_blood_sugar'] == 0, 'fasting_blood_sugar'] = 'lower than 120mg/ml'
data.loc[data['fasting_blood_sugar'] == 1, 'fasting_blood_sugar'] = 'greater than 120mg/ml'

data.loc[data['resting_electrocardiogram'] == 0, 'resting_electrocardiogram'] = 'normal'
data.loc[data['resting_electrocardiogram'] == 1, 'resting_electrocardiogram'] = 'ST-T wave abnormality'
data.loc[data['resting_electrocardiogram'] == 2, 'resting_electrocardiogram'] = 'left ventricular hypertrophy'

data.loc[data['exercise_induced_angina'] == 0, 'exercise_induced_angina'] = 'no'
data.loc[data['exercise_induced_angina'] == 1, 'exercise_induced_angina'] = 'yes'

data.loc[data['st_slope'] == 0, 'st_slope'] = 'upsloping'
data.loc[data['st_slope'] == 1, 'st_slope'] = 'flat'
data.loc[data['st_slope'] == 2, 'st_slope'] = 'downsloping'

data.loc[data['thalassemia'] == 1, 'thalassemia'] = 'fixed defect'
data.loc[data['thalassemia'] == 2, 'thalassemia'] = 'normal'
data.loc[data['thalassemia'] == 3, 'thalassemia'] = 'reversable defect'

# Save processed data
data.to_csv('data/processed/heart_processed.csv', index=False)
print("Data preprocessing completed.")

# -------------------------------
# Step 2: Load processed data
# -------------------------------
data = pd.read_csv('data/processed/heart_processed.csv')

num_feats = ['age', 'cholesterol', 'resting_blood_pressure', 'max_heart_rate_achieved', 'st_depression', 'num_major_vessels']
bin_feats = ['sex', 'fasting_blood_sugar', 'exercise_induced_angina', 'target']
nom_feats= ['chest_pain_type', 'resting_electrocardiogram', 'st_slope', 'thalassemia']
cat_feats = nom_feats + bin_feats

mypal = ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA']
mypal_1= ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA', '#FC05FB', '#FEAEFE', '#FCD2FC']

# -------------------------------
# Step 3: Numerical features plots
# -------------------------------
print("Step 2/5: Generating numerical feature plots...")
L = len(num_feats)
ncol = 2
nrow = int(np.ceil(L / ncol))
fig, axes = plt.subplots(nrow, ncol, figsize=(16, 14), facecolor='#F6F5F4')
axes = axes.flatten()

for i, col in enumerate(num_feats):
    ax = axes[i]
    if col == 'num_major_vessels':
        sns.countplot(data=data, x=col, hue='target', palette=mypal[1::4], ax=ax)
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x() + p.get_width()/2., height + 0.5, f'{int(height)}', ha='center', fontsize=10,
                    bbox=dict(facecolor='none', edgecolor='black', boxstyle='round', linewidth=0.5))
        ax.set_ylabel('Count', fontsize=14)
    else:
        sns.kdeplot(data=data, x=col, hue='target', multiple='stack', palette=mypal[1::4], ax=ax)
        ax.set_ylabel('Density', fontsize=14)
    ax.set_xlabel(col, fontsize=14)
    sns.despine(ax=ax, right=True)

for j in range(L, nrow*ncol):
    fig.delaxes(axes[j])

plt.suptitle('Distribution of Numerical Features', fontsize=24)
plt.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig('results/figures/numerical_features_distribution.png', dpi=300, bbox_inches='tight')
plt.close(fig)

# Pairplot
g = sns.pairplot(data[num_feats + ['target']], hue="target", corner=True, diag_kind='hist', palette=mypal[1::4])
g.savefig('results/figures/pairplot_numerical_features.png', dpi=300, bbox_inches='tight')
plt.close()

# -------------------------------
# Step 4: Categorical features plots
# -------------------------------
print("Step 3/5: Generating categorical feature plots...")
def count_plot(data, cat_feats):    
    L = len(cat_feats)
    ncol = 2
    nrow = int(np.ceil(L/ncol))
    remove_last = (nrow * ncol) - L
    fig, axes = plt.subplots(nrow, ncol, figsize=(18, 24), facecolor='#F6F5F4')    
    fig.subplots_adjust(top=0.92)
    if nrow == 1 and ncol == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    if remove_last > 0:
        for j in range(remove_last):
            axes[-(j+1)].set_visible(False)
    for i, col in enumerate(cat_feats):
        ax = axes[i]
        sns.countplot(data=data, x=col, hue="target", palette=mypal[1::4], ax=ax)
        ax.set_xlabel(col, fontsize=20)
        ax.set_ylabel("count", fontsize=20)
        sns.despine(right=True, ax=ax)
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.text(p.get_x() + p.get_width()/2., height + 3, '{:1.0f}'.format(height), ha="center",
                       bbox=dict(facecolor='none', edgecolor='black', boxstyle='round', linewidth=0.5))
    plt.suptitle('Distribution of Categorical Features', fontsize=24)
    plt.tight_layout()
    fig.savefig('results/figures/categorical_features_distribution.png', dpi=300, bbox_inches='tight')
    plt.close(fig)

count_plot(data, cat_feats[:-1])

# -------------------------------
# Step 5: Correlations
# -------------------------------
print("Step 4/5: Generating correlation plots...")

# Numerical correlations (Pearson)
df_ = data[num_feats]
corr = df_.corr(method='pearson')
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(8, 5), facecolor=None)
cmap = sns.color_palette(mypal, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1.0, vmin=-1.0, center=0, annot=True,
            square=False, linewidths=.5, cbar_kws={"shrink": 0.75})
ax.set_title("Numerical features correlation (Pearson's)", fontsize=20, y= 1.05)
f.savefig('results/figures/numerical_features_correlation.png', dpi=300, bbox_inches='tight')
plt.close(f)

# Point-biserial correlations
feats_ = ['age', 'cholesterol', 'resting_blood_pressure', 'max_heart_rate_achieved', 'st_depression', 'num_major_vessels', 'target']

def point_biserial(x, y):
    pb = stats.pointbiserialr(x, y)
    return pb[0]

rows= []
for x in feats_:
    col = []
    for y in feats_ :
        pbs =point_biserial(data[x], data[y]) 
        col.append(round(pbs,2))  
    rows.append(col)  
    
pbs_results = np.array(rows)
DF = pd.DataFrame(pbs_results, columns = data[feats_].columns, index =data[feats_].columns)

mask = np.triu(np.ones_like(DF, dtype=bool))
corr = DF.mask(mask)

f, ax = plt.subplots(figsize=(8, 5), facecolor=None)
cmap = sns.color_palette(mypal, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1.0, vmin=-1, center=0, annot=True,
            square=False, linewidths=.5, cbar_kws={"shrink": 0.75})
ax.set_title("Cont feats vs target correlation (point-biserial)", fontsize=20, y= 1.05)
f.savefig('results/figures/point_biserial_correlation.png', dpi=300, bbox_inches='tight')
plt.close(f)

# Categorical correlations (Cramer's V)
def cramers_v(x, y): 
    confusion_matrix = pd.crosstab(x,y)
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))

# calculate the correlation coefficients using the above function
data_ = data[cat_feats]
rows= []
for x in data_:
    col = []
    for y in data_ :
        cramers =cramers_v(data_[x], data_[y]) 
        col.append(round(cramers,2))
    rows.append(col)
    
cramers_results = np.array(rows)
df = pd.DataFrame(cramers_results, columns = data_.columns, index = data_.columns)

# plot the heat map
mask = np.triu(np.ones_like(df, dtype=bool))
corr = df.mask(mask)
f, ax = plt.subplots(figsize=(10, 6), facecolor=None)
cmap = sns.color_palette(mypal_1, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1.0, vmin=0, center=0, annot=True,
            square=False, linewidths=.01, cbar_kws={"shrink": 0.75})
ax.set_title("Categorical Features Correlation (Cramer's V)", fontsize=20, y= 1.05)
f.savefig('results/figures/categorical_features_cramersv.png', dpi=300, bbox_inches='tight')
plt.close(f)

print("Step 5/5: Pipeline completed. All figures saved in 'results/figures/'")
