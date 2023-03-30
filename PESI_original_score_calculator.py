def answer_is_yes(answer):
    return answer.lower().startswith('y')

disclaimer = "This script is for educational purposes only and clinical corelation is required!"

questions_and_score = [
    ('Is the patient male? (yes/NO):', 10),
    ('Does the patient have cancer? (yes/NO):', 30),
    ('Does the patient have Chronic Heart Failure? (yes/NO):', 10),
    ('Does the patient have Chronic pulmonary diseasre? (yes/NO):', 10),
    ('Is the pulse rate more or equal to 110 bpm? (yes/NO):', 20),
    ('Is the systolic blood pressure < 100mm/Hg? (yes/NO):', 30),
    ('Is the respiration rate > 30 breaths/minute? (yes/NO):', 20),
    ('Is the temperature < 36°C? (yes/NO):', 20),
    ('Is the mental status altered? (yes/NO):', 60),
    ('Is arterial oxyhaemoglobin saturation < 90%? (yes/NO):', 20),
]

score_and_class_type = [
    (66, 'Class I: Very low 30 day mortality risk (0–1.6%)'),
    (86, 'Class II: 66–85 points Low mortality risk (1.7–3.5%)'),
    (106, 'Class III: 86–105 points Moderate mortality risk (3.2–7.1%)'),
    (126, 'Class IV: 106–125: points High mortality risk (4.0–11.4%)'),
    (float('inf'), 'Class V: >125 points Very high mortality risk (10.0–24.5%)')
]

total_score = int(input("What is the patient's age?: "))

for question, score in questions_and_score:
    if answer_is_yes(input(question)):
        total_score += score

for score, class_type in score_and_class_type:
    if total_score < score:
        print(f'Score: {total_score} - {class_type}')
        print(disclaimer)
        break
