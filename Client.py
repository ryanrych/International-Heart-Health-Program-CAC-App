class Client:

    def __init__(self):
        self.CACdate = None
        self.gender = None
        self.race = None
        self.age = None
        self.paymentMethod = None
        self.refferalSource = None
        self.refferingProvider = None

    def firstPageConstructor(self, CACdate, gender, race, age, paymentMethod, refferalSource, referringProvider):
        self.CACdate = CACdate
        self.gender = gender
        self.race = race
        self.age = age
        self.paymentMethod = paymentMethod
        self.refferalSource = refferalSource
        self.refferingProvider = referringProvider

