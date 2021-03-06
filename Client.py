class Client:

    def __init__(self):
        self.year = None
        self.quarter = None
        self.gender = None
        self.race = None
        self.age = None
        self.paymentMethod = None
        self.refferalSource = None
        self.refferingProvider = None

        self.CADSymptoms = None
        self.knownCAD = None
        self.riskFactors = None
        self.radiationDose = None
        self.CACScore = None

        self.path = None

    def firstPageConstructor(self, year, quarter, gender, race, age, paymentMethod, refferalSource, referringProvider):
        self.year = year
        self.quarter = quarter
        self.gender = gender
        self.race = race
        self.age = age
        self.paymentMethod = paymentMethod
        self.refferalSource = refferalSource
        self.refferingProvider = referringProvider

    def secondPageConstructor(self, CADSypmtoms, knownCAD, riskFactors, radiationDose, CACScore):
        self.CADSymptoms = CADSypmtoms
        self.knownCAD = knownCAD
        self.riskFactors = riskFactors
        self.radiationDose = radiationDose
        self.CACScore = CACScore