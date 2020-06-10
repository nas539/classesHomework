class Skincare:
    product = "Skincare"

    def __init__(self, face_wash, moisturizer, eye_cream):
        self.face_wash = face_wash
        self.moisturizer = moisturizer
        self.eye_cream = eye_cream

    def __str__(self):
        return f"This is all about{self.product}"

    def list_some_products(self):
        return f"Most skincare lines carry a {self.face_wash}, a {self.moisturizer}, and an {self.eye_cream}..."


class Kate_Somerville(Skincare):
    brand = "Kate Somerville"

    def list_some_products(self):
        return f"{self.brand} has a face wash called: {self.face_wash}, a moisturizer called: {self.moisturizer}, a top rated eye cream: {self.eye_cream}"


class Chanel(Skincare):
    brand = "Chanel"

    def list_some_products(self):
        return f"{self.brand} has a face wash called: {self.face_wash}, a moisturizer called: {self.moisturizer}, a top rated eye cream: {self.eye_cream}"

    def __repr__(self):
        return f"{self.face_wash}, {self.moisturizer}, {self.eye_cream}"


sc = Skincare("face wash", "moisturzer", "eye cream")
ks = Kate_Somerville("Exfolicate Daily Face Wash", "Age Arrest", "UncompliKated")
chl = Chanel("La Mousse", "Sublimage", "Le Lift")

print(str(sc))
print(sc.list_some_products())
print(ks.list_some_products())
print(chl.list_some_products())
print(repr(chl))
