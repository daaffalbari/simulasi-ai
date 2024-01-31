# Existing inference functions
def age_junior(age):
    if age <= 22 or age >= 32:
        return 0
    elif 22 <= age <= 27:
        return (age - 22) / (27 - 22)
    elif 27 <= age <= 32:
        return (32 - age) / (32 - 27)

def age_juniorsenior(age):
    if age <= 30 or age >= 40:
        return 0
    elif 30 <= age <= 35:
        return (age - 30) / (35 - 30)
    elif 35 <= age <= 40:
        return (40 - age) / (40 - 35)

def age_senior(age):
    if age <= 38 or age >= 60:
        return 0
    elif 38 <= age <= 49:
        return (age - 38) / (49 - 38)
    elif 49 <= age <= 60:
        return (60 - age) / (60 - 49)

def travel_non(business_travel):
    return 0

def travel_rarely(business_travel):
    if business_travel <= 2 or business_travel >= 5:
        return 0
    elif 2 <= business_travel <= 3.5:
        return (business_travel - 2) / (3.5 - 2)
    elif 3.5 <= business_travel <= 5:
        return (5 - business_travel) / (5 - 3.5)

def travel_frequently(business_travel):
    if business_travel <= 3 or business_travel >= 8:
        return 0
    elif 3 <= business_travel <= 5.5:
        return (business_travel - 3) / (5.5 - 3)
    elif 5.5 <= business_travel <= 8:
        return (8 - business_travel) / (8 - 5.5)

def hourlyrate_low(hourlyRate):
    if hourlyRate <= 30 or hourlyRate >= 60:
        return 0
    elif 30 <= hourlyRate <= 45:
        return (hourlyRate - 30) / (45 - 30)
    elif 45 <= hourlyRate <= 60:
        return (60 - hourlyRate) / (60 - 45)

def hourlyrate_high(hourlyRate):
    if hourlyRate <= 50 or hourlyRate >= 80:
        return 0
    elif 50 <= hourlyRate <= 65:
        return (hourlyRate - 50) / (65 - 50)
    elif 65 <= hourlyRate <= 80:
        return (80 - hourlyRate) / (80 - 65)

def overtime_no(overtime):
    if overtime <= 5 or overtime >= 8:
        return 0
    elif 5 <= overtime <= 6.5:
        return (overtime - 5) / (6.5 - 5)
    elif 6.5 <= overtime <= 8:
        return (8 - overtime) / (8 - 6.5)

def overtime_yes(overtime):
    if overtime <= 6 or overtime >= 10:
        return 0
    elif 6 <= overtime <= 8:
        return (overtime - 6) / (8 - 6)
    elif 8 <= overtime <= 10:
        return (10 - overtime) / (10 - 8)

# Function to perform inference and determine the result
def perform_inference(age, business_travel, hourly_rate, overtime):
    age_junior_val = age_junior(age)
    age_juniorsenior_val = age_juniorsenior(age)
    age_senior_val = age_senior(age)

    travel_non_val = travel_non(business_travel)
    travel_rarely_val = travel_rarely(business_travel)
    travel_frequently_val = travel_frequently(business_travel)

    hourlyrate_low_val = hourlyrate_low(hourly_rate)
    hourlyrate_high_val = hourlyrate_high(hourly_rate)

    overtime_no_val = overtime_no(overtime)
    overtime_yes_val = overtime_yes(overtime)

    list_predicate_value = []
    list_z_value = []

    def inference_no_attration(age, business_travel, hourly_rate, overtime):
      pv = min(age, business_travel, hourly_rate, overtime)
      list_predicate_value.append(pv)

      if pv == 0:
        list_z_value.append(237)
      if pv == 1:
        list_z_value.append(1233)
      if 0 < pv < 1:
        value = 237 + (1233 - 237) * pv
        list_z_value.append(value)

    def inference_yes_attration(age, business_travel, hourly_rate, overtime):
        pv = min(age, business_travel, hourly_rate, overtime)
        list_predicate_value.append(pv)

        if pv == 0:
          list_z_value.append(237)
        if pv == 1:
          list_z_value.append(1233)
        if 0 < pv < 1:
          value = 237 + (1233 - 237) * pv
          list_z_value.append(value)

    # Rules 1
    inference_no_attration(age_junior_val, travel_non_val, hourlyrate_low_val, overtime_no_val)

    # Rules 2
    inference_no_attration(age_junior_val, travel_rarely_val, hourlyrate_low_val, overtime_no_val)

    # Rules 3
    inference_no_attration(age_junior_val, travel_frequently_val, hourlyrate_low_val, overtime_no_val)

    # Rules 4
    inference_yes_attration(age_junior_val, travel_rarely_val, hourlyrate_low_val, overtime_yes_val)

    # Rules 5
    inference_no_attration(age_junior_val, travel_frequently_val, hourlyrate_low_val, overtime_yes_val)

    # Rules 6
    inference_no_attration(age_junior_val, travel_non_val, hourlyrate_high_val, overtime_no_val)

    # Rules 7
    inference_no_attration(age_junior_val, travel_rarely_val, hourlyrate_high_val, overtime_no_val)

    # Rules 8
    inference_yes_attration(age_junior_val, travel_frequently_val, hourlyrate_high_val, overtime_no_val)

    # Rules 9
    inference_no_attration(age_junior_val, travel_non_val, hourlyrate_high_val, overtime_yes_val)

    # Rules 10
    inference_yes_attration(age_junior_val, travel_rarely_val, hourlyrate_high_val, overtime_yes_val)

    # Rules 11
    inference_no_attration(age_junior_val, travel_frequently_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 12
    inference_no_attration(age_juniorsenior_val, travel_non_val, hourlyrate_low_val, overtime_no_val)

    # Rule 13
    inference_no_attration(age_juniorsenior_val, travel_rarely_val, hourlyrate_low_val, overtime_no_val)

    # Rule 14
    inference_no_attration(age_juniorsenior_val, travel_frequently_val, hourlyrate_low_val, overtime_no_val)

    # Rule 15
    inference_no_attration(age_juniorsenior_val, travel_non_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 16
    inference_no_attration(age_juniorsenior_val, travel_rarely_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 17
    inference_yes_attration(age_juniorsenior_val, travel_frequently_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 18
    inference_no_attration(age_juniorsenior_val, travel_non_val, hourlyrate_high_val, overtime_no_val)

    # Rule 19
    inference_no_attration(age_juniorsenior_val, travel_rarely_val, hourlyrate_high_val, overtime_no_val)

    # Rule 20
    inference_no_attration(age_juniorsenior_val, travel_frequently_val, hourlyrate_high_val, overtime_no_val)

    # Rule 21
    inference_no_attration(age_juniorsenior_val, travel_non_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 22
    inference_no_attration(age_juniorsenior_val, travel_rarely_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 23
    inference_no_attration(age_juniorsenior_val, travel_frequently_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 24
    inference_no_attration(age_senior_val, travel_non_val, hourlyrate_low_val, overtime_no_val)

    # Rule 25
    inference_no_attration(age_senior_val, travel_rarely_val, hourlyrate_low_val, overtime_no_val)

    # Rule 26
    inference_no_attration(age_senior_val, travel_frequently_val, hourlyrate_low_val, overtime_no_val)

    # Rule 27
    inference_no_attration(age_senior_val, travel_non_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 28
    inference_no_attration(age_senior_val, travel_rarely_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 29
    inference_no_attration(age_senior_val, travel_frequently_val, hourlyrate_low_val, overtime_yes_val)

    # Rule 30
    inference_no_attration(age_senior_val, travel_non_val, hourlyrate_high_val, overtime_no_val)

    # Rule 31
    inference_no_attration(age_senior_val, travel_rarely_val, hourlyrate_high_val, overtime_no_val)

    # Rule 32
    inference_no_attration(age_senior_val, travel_frequently_val, hourlyrate_high_val, overtime_no_val)

    # Rule 33
    inference_no_attration(age_senior_val, travel_non_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 34
    inference_no_attration(age_senior_val, travel_rarely_val, hourlyrate_high_val, overtime_yes_val)

    # Rule 35
    inference_no_attration(age_senior_val, travel_frequently_val, hourlyrate_high_val, overtime_yes_val)

    hasil = 0
    jumlah_value = 0

    for i in range(len(list_predicate_value)):
        hasil += list_predicate_value[i] * list_z_value[i]
        jumlah_value += list_predicate_value[i]

    if jumlah_value == 0:
        nilai_setara = 0
    else:
        nilai_setara = hasil / jumlah_value

    return nilai_setara