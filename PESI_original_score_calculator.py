'''Ask user questions from pesi table:'''

Age = int(input("What is the patient's age?: "))

Male = input("Is the patient male? (yes/NO): ")
if Male == "yes":
     Male_score = 10
else:
     Male_score = 0

Cancer = input("Does the patient have cancer? (yes/NO): ")
if Cancer == "yes":
     Cancer_score = 30
else:
     Cancer_score = 0

Chronic_Heart_Failure = input("Does the patient have Chronic Heart Failure? (yes/NO): ")
if Chronic_Heart_Failure == "yes":
     Chronic_Heart_Failure_score = 10
else:
     Chronic_Heart_Failure_score = 0
     
Chronic_pulmonary_disease = input("Does the patient have Chronic pulmonary diseasre? (yes/NO):")
if Chronic_pulmonary_disease == "yes":
     Chronic_pulmonary_disease_score = 10
else:
     Chronic_pulmonary_disease_score = 0

Pulse_rate_more_equal_110_bpm = input("Is the pulse rate more or equal to 110 bpm? (yes/NO):")
if Pulse_rate_more_equal_110_bpm == "yes":
     Pulse_rate_more_equal_110_bpm_score = 20
else:
     Pulse_rate_more_equal_110_bpm_score = 0
     
Systolic_blood_pressure_less_100_mmHg = input("Is the systolic blood pressure < 100mm/Hg? (yes/NO):")
if Systolic_blood_pressure_less_100_mmHg == "yes":
     Systolic_blood_pressure_less_100_mmHg_score = 30
else:
     Systolic_blood_pressure_less_100_mmHg_score = 0

Respiratory_rate_more_than_30_breaths_min = input("Is the respiration rate > 30 breaths/minute? (yes/NO): ")
if Respiratory_rate_more_than_30_breaths_min == "yes":
     Respiratory_rate_more_than_30_breaths_min_score = 20
else:
     Respiratory_rate_more_than_30_breaths_min_score = 0

Temperature_less_than_36_C = input("Is the temperature < 36°C? (yes/NO):")
if Temperature_less_than_36_C == "yes":
     Temperature_less_than_36_C_score = 20
else:
     Temperature_less_than_36_C_score = 0

Altered_mental_status = input("Is the mental status altered? (yes/NO):")
if Altered_mental_status == "yes":
     Altered_mental_status_score = 60
else:
     Altered_mental_status_score = 0

Arterial_oxyhaemoglobin_saturation_less_than_90_percent = input("Is arterial oxyhaemoglobin saturation < 90%? (yes/NO): ")
if Arterial_oxyhaemoglobin_saturation_less_than_90_percent == "yes":
     Arterial_oxyhaemoglobin_saturation_less_than_90_percent_score = 20
else:
     Arterial_oxyhaemoglobin_saturation_less_than_90_percent_score = 0



'''Add all the points for a total'''

Total = Age + Male_score + Cancer_score + Chronic_Heart_Failure_score + Chronic_pulmonary_disease_score + Pulse_rate_more_equal_110_bpm_score + Systolic_blood_pressure_less_100_mmHg_score + Respiratory_rate_more_than_30_breaths_min_score + Temperature_less_than_36_C_score + Altered_mental_status_score + Arterial_oxyhaemoglobin_saturation_less_than_90_percent_score

'''Output and print the risk class'''
print("Total points:" +Total)

if Total <= 65:
     print("Class I: Very low 30 day mortality risk (0–1.6%)")

elif 66 <= Total <=85:
     print("Class II: 66–85 points Low mortality risk (1.7–3.5%)")

elif 86 <= Total <= 105:
     print("Class III: 86–105 points Moderate mortality risk (3.2–7.1%)")

elif 106 <= Total <= 125:
     print("Class IV: 106–125: points High mortality risk (4.0–11.4%)")

elif Total >= 125:
     print("Class V: >125 points Very high mortality risk (10.0–24.5%)")

else:
     print("error")

'''       
Class I: ≤65 points
Very low 30-day
mortality risk
(0–1.6%)

Class II: 66–85 points
Low mortality risk
(1.7–3.5%)

Class III: 86–105
points
Moderate mortality
risk (3.2–7.1%)

Class IV: 106–125:
points
High mortality risk
(4.0–11.4%)

Class V: >125 points
Very high mortality risk
(10.0–24.5%)  '''

Disclaimer = "This script is for educational purposes only!"

print(Disclaimer)