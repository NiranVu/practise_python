def body_mass_index(m, h):
    """
    Tính toán BMI của một người với cân nặng và chiều cao
    """
    bmi = m / (h * 2)
    return f"Chỉ số BMI của bạn là {bmi}"


def bmi_information(m, h):
    bmi = body_mass_index(m, h)
    if bmi < 18.5:
        return "Bạn gầy"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Cân nặng của bạn bình thường"
    else:
        if bmi >= 25:
            return "Bạn thừa cân"
        elif bmi >= 25 and bmi <= 29.9:
            return "Bạn tiền béo phì"
        else:
            if bmi >= 30 and bmi <= 34.9:
                return "Bạn béo phì độ I"
            elif bmi >= 35 and bmi <= 39.9:
                return "Bạn béo phì độ II"
            else:
                return "Bạn béo phì độ III"


# Bài 07: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h


def body_mass_index(m, h):
    return m / h ** 2


def bmi_information(m, h):
    bmi = body_mass_index(m, h)
    print(f"Your BMI: {round(bmi, 1)}")
    if bmi < 15:
        print("=>> Very severely underweight")
    elif 15 <= bmi < 16:
        print("=>> Severely underweight")
    elif 16 <= bmi < 18.5:
        print("=>> Underweight")
    elif 18.5 <= bmi < 25:
        print("=>> Normal (healthy weight)")
    elif 25 <= bmi < 30:
        print("=>> Overweight")
    elif 30 <= bmi < 35:
        print("=>> Obese Class I (Moderately obese)")
    elif 35 <= bmi < 40:
        print("=>> Obese Class II (Severely obese)")
    else:
        print("=>> Obese Class III (Very severely obese)")
