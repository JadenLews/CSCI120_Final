# object oriented programming class name is Nutri_info

# defines the variables height, weight, age and waist circumference and facilitates the computation of Body Mass Index, Skeletal Muscle Mass and Body Adiposity Index

class Nutri_info:

    def __init__(self, height_param, weight_param, age_param, waist_circum_param):
        
        self._height = height_param
        self._weight = weight_param
        self._age = age_param
        self._waist_circum = waist_circum_param 

    @property 
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        height = f'{(height):.2}'
        height = float(height)
        if not height > 0.00:
            raise ValueError (f'({height}) must be greater 0.00 meters') #height is in meters
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        weight = f'{(weight):.2}'
        weight = float(weight)
        if not weight > 0.00: # weight is in kilograms
            raise ValueError (f'({weight}) must be greater than 0.00 kilograms')
        self._weight = weight

    @property
    def waist_circum(self):
        return self._waist_circum

    @waist_circum.setter
    def waist_circum(self, waist_circum):
        waist_circum = f'{(waist_circum):.2}'
        waist_circum = float(waist_circum)
        if not waist_circum > 0.00:
            raise ValueError (f'({waist_circum}) must be greater than 0.00 cm')
        self._waist_circum = waist_circum

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        age_result = int(age)
        if not age_result > 0:
            raise ValueError (f'one must be of at least {(age_result)} years of age')
        self._age = age_result

    def BMI(self):
        BMI = (self.weight / (self.height ** 2))
        BMI_result = f'{(BMI):.5}'
        BMI_result = float(BMI_result)
        return BMI_result

    def skeletal_muscle_mass(self):
        height_2 = 100 * self.height
        weight_2 = self.weight
        skeletal_muscle_mass = (0.407 * weight_2) + (0.267 * height_2) - 19.2
        skeletal_musc_mass_result = f'{(skeletal_muscle_mass):.5}'
        skeletal_musc_mass_result = float(skeletal_musc_mass_result)
        return skeletal_musc_mass_result

    def body_adiposity_index(self):
        body_adiposity_ind_res = (self.waist_circum / self.height ** 1.5) - 18
        ind_res_2 = f'{(body_adiposity_ind_res):.5}'
        ind_res_3 = float(ind_res_2)
        return ind_res_3

    def age_method(self):
        age_res = (self.age // 5) ** 3
        return age_res

test = Nutri_info(1.72, 55.24, 20, 68.58)
variable_A = test.BMI()
print(variable_A)
variable_B = test.skeletal_muscle_mass()
print(variable_B)
variable_C = test.body_adiposity_index()
print(variable_C)
variable_alpha = test.age_method()
print(variable_alpha)
variable_beta = (test.BMI() ** (test.skeletal_muscle_mass() // (1.6 * test.body_adiposity_index())))
print(variable_beta)