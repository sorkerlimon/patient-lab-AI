import  pandas as pd
import matplotlib.pyplot as plt
patient  = pd.read_csv("./data-set/indian_liver_patient.csv")
# print(patient.head())
Total_Bilirubin = patient["Total_Bilirubin"].value_counts(sort=False)
print(Total_Bilirubin)
Total_Bilirubin.plot(title="Total_Bilirubin of players per  year")
plt.show()

