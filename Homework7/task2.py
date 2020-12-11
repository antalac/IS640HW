import pandas as pd 

def set_gpa(score):
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0

df = pd.read_csv("scores.csv") 
del df['Unnamed: 0']
df = df.applymap(lambda x: set_gpa(int(x)))
#print(df.mean())
all_means = []
for col in df.columns: 
    m = df[col].mean()
    print(f'{col}: {m:.2f}') 
    all_means.append(m)
class_gpa = sum(all_means) / len(all_means)
print()
print(f'The class GPA is {class_gpa:.2f}')
