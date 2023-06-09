# Okul sistemi

print("Okul sistemine hoş geldiniz")


class Person():
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

class Student(Person): 
    all_notes = []

    def __init__(self, classroom, branch, name, surname, age, gender):
        super().__init__(name, surname, age, gender)
        self.classroom = classroom
        self.branch = branch

    def notes(self, *note):
        self.note = note
        self.all_notes.extend(note)
        return f"{self.name} {self.surname} dönemlik notlarınız = {self.all_notes}"

    def average(self):
        avg = sum(self.all_notes) / len(self.all_notes)
        return f"Sayın {self.name} {self.surname} Ortalamanız = {avg}" 

    def passed_away_control(self):
        avg = self.average()
        avg = float(avg.split()[-1])
        if avg >= 50 and avg <= 100:
            return f"{self.name} {self.surname} Tebrikler sınıfı geçtiniz."
        elif avg < 50 and avg > 0:
            return f"{self.name} {self.surname} Maalesef sınıfta kaldınız." 
        else:
            return "Yanlış giriş"
            
class Teacher(Person):
    plus_salary = 1.1
    five_salary = 1.7

    teacher = 3000
    ass_director = 5700
    manager = 7500

    def __init__(self, teacher_branch, profession, experience, name, surname, age, gender):
        super().__init__(name, surname, age, gender)
        self.teacher_branch = teacher_branch
        self.profession = profession
        self.experience = experience

    def salary(self):
        #total_exp = self.experience  7 = 7
        # total_salary = (self.teacher_branch)  3000

        total_salary = 0 

        if self.profession == "teacher" or "Teacher":
            total_salary = self.teacher
        elif self.profession == "assistan" or "Assistan" or "Assitan Director" or "Assitan director" or "Director" or "director":
            total_salary = self.ass_director
        elif self.profession == "Manager" or "manager":
            total_salary = self.manager
        else:
            return "Hatalı giriş"
        
        for year in range(1, self.experience + 1): # 1,2,3,4,5,6,7 = 7
                
            total_salary = round(total_salary, 2)
            # print(f"{year}. yıl maaşınız = {total_salary}")

            if year % 4 == 0:
                #  total_salary = round(total_salary, 2)
                 print(f"{year}. yıl maaşınız = {total_salary}")
                 total_salary *= self.five_salary #  3.993 * 1.7 = 6.788,1 / 9.938,45721 --> 16.895,377257
            elif year % 4 != 0:
                #  total_salary = round(total_salary, 2)
                 print(f"{year}. yıl maaşınız = {total_salary}")
                 total_salary *= self.plus_salary # 3000 * 1.1 = 3300 --> 3300 * 1.1 = 3630, 3.993, 6.788,1, 7.466,91, 8.213,601...8(9.034,9611, 9.938,45721, 18.584,9149827)   
            else: 
                print("Hata!")
                 
        return f"Sayın {self.name} {self.surname}, Meslek: {self.profession}. Alanınız {self.teacher_branch}. Yaşınız {self.age}. {self.experience} yıllık deneyiminiz sonucu maaşınız = {total_salary}"
        

       
def sayaç():
    x = 0 
    while x < 5:
        print("Merhaba")
        x += 1

sayaç()