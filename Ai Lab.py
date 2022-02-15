import  pandas as pd
import matplotlib.pyplot as plt
patient  = pd.read_csv("./data-set/indian_liver_patient.csv")
# print(patient.head())
Total_Bilirubin = patient["Total_Bilirubin"].value_counts(sort=False)
# print(Total_Bilirubin)
Total_Bilirubin.plot(title="Total_Bilirubin of players per  year")
# plt.show()

grupBy= patient.groupby("Gender")["Total_Bilirubin"].value_counts()
# print(grupBy)
grupBy.plot(title="Patient by  per  Gender")
plt.xlabel("Gender")
plt.ylabel("Total Bilurubin")
plt.legend("Male")
plt.legend("FeMale")
plt.show()
