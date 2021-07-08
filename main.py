from kivy.config import Config
Config.set("graphics", "resizable", False)
Config.set("graphics", "position", "custom")
Config.set("graphics", "left", 300)
Config.set("graphics", "top", 75)

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import NoTransition

import xlwt
from xlwt import Workbook

from Client import Client

client = Client()

class WindowManager(ScreenManager):
    pass

class MainInterface(Widget):

    genderChecked = False
    raceChecked = False
    paymentMethodChecked = False
    referralSourceChecked = False
    providerChecked = False

    clientGender = None
    clientRace = None
    clientPaymentMethod = None
    clientReferralSource = None
    clientProvider = None

    def checkMale(self):
        if not self.ids.maleBox.active:
            self.genderChecked = False
            return
        self.ids.femaleBox.active = False
        self.genderChecked = True
        self.clientGender = "Male"

    def checkFemale(self):
        if not self.ids.femaleBox.active:
            self.genderChecked = False
            return
        self.ids.maleBox.active = False
        self.genderChecked = True
        self.clientGender = "Female"

    def checkCaucasian(self):
        if not self.ids.caucasianBox.active:
            self.raceChecked = False
            return
        self.ids.africanAmericanBox.active = False
        self.ids.hispanicBox.active = False
        self.ids.asianBox.active = False
        self.ids.otherBox.active = False
        self.raceChecked = True
        self.clientRace = "Caucasian"

    def checkAfricanAmerican(self):
        if not self.ids.africanAmericanBox.active:
            self.raceChecked = False
            return
        self.ids.caucasianBox.active = False
        self.ids.hispanicBox.active = False
        self.ids.asianBox.active = False
        self.ids.otherBox.active = False
        self.raceChecked = True
        self.clientRace = "African American"

    def checkHispanic(self):
        if not self.ids.hispanicBox.active:
            self.raceChecked = False
            return
        self.ids.africanAmericanBox.active = False
        self.ids.caucasianBox.active = False
        self.ids.asianBox.active = False
        self.ids.otherBox.active = False
        self.raceChecked = True
        self.clientRace = "Hispanic"

    def checkAsian(self):
        if not self.ids.asianBox.active:
            self.raceChecked = False
            return
        self.ids.africanAmericanBox.active = False
        self.ids.hispanicBox.active = False
        self.ids.caucasianBox.active = False
        self.ids.otherBox.active = False
        self.raceChecked = True
        self.clientRace = "Asian"

    def checkOther(self):
        if not self.ids.otherBox.active:
            self.raceChecked = False
            return
        self.ids.africanAmericanBox.active = False
        self.ids.hispanicBox.active = False
        self.ids.asianBox.active = False
        self.ids.caucasianBox.active = False
        self.raceChecked = True
        self.clientRace = "Other"

    def checkPrivate(self):
        if not self.ids.privateBox.active:
            self.paymentMethodChecked = False
            return
        self.ids.medicareBox.active = False
        self.ids.selfPayBox.active = False
        self.ids.employerPaymentBox.active = False
        self.paymentMethodChecked = True
        self.clientPaymentMethod = "Private Carrier"

    def checkMedicare(self):
        if not self.ids.medicareBox.active:
            self.paymentMethodChecked = False
            return
        self.ids.privateBox.active = False
        self.ids.selfPayBox.active = False
        self.ids.employerPaymentBox.active = False
        self.paymentMethodChecked = True
        self.clientPaymentMethod = "Medicare/Medicaid"

    def checkSelfPay(self):
        if not self.ids.selfPayBox.active:
            self.paymentMethodChecked = False
            return
        self.ids.medicareBox.active = False
        self.ids.privateBox.active = False
        self.ids.employerPaymentBox.active = False
        self.paymentMethodChecked = True
        self.clientPaymentMethod = "Self Pay"

    def checkEmployerPayment(self):
        if not self.ids.employerPaymentBox.active:
            self.paymentMethodChecked = False
            return
        self.ids.medicareBox.active = False
        self.ids.selfPayBox.active = False
        self.ids.privateBox.active = False
        self.paymentMethodChecked = True
        self.clientPaymentMethod = "Employer"

    def checkSelfReferral(self):
        if not self.ids.selfReferralBox.active:
            self.referralSourceChecked = False
            return
        self.ids.employerReferralBox.active = False
        self.ids.physicianReferralBox.active = False
        self.referralSourceChecked = True
        self.clientReferralSource = "Self"

    def checkEmployerReferral(self):
        if not self.ids.employerReferralBox.active:
            self.referralSourceChecked = False
            return
        self.ids.selfReferralBox.active = False
        self.ids.physicianReferralBox.active = False
        self.referralSourceChecked = True
        self.clientReferralSource = "Employer"

    def checkPhysicianReferral(self):
        if not self.ids.physicianReferralBox.active:
            self.referralSourceChecked = False
            return
        self.ids.employerReferralBox.active = False
        self.ids.selfReferralBox.active = False
        self.referralSourceChecked = True
        self.clientReferralSource = "Physician"

    def checkPrimaryCareProvider(self):
        if not self.ids.primaryCarePhysicianProviderBox.active:
            self.providerChecked = False
            return
        self.ids.cardiologistProviderBox.active = False
        self.ids.midLevelProviderBox.active = False
        self.ids.obgynProviderBox.active = False
        self.providerChecked = True
        self.clientProvider = "Primary Care Physician"

    def checkCardiologistProvider(self):
        if not self.ids.cardiologistProviderBox.active:
            self.providerChecked = False
            return
        self.ids.primaryCarePhysicianProviderBox.active = False
        self.ids.midLevelProviderBox.active = False
        self.ids.obgynProviderBox.active = False
        self.providerChecked = True
        self.clientProvider = "Cardiologist"

    def checkMidLevelProvider(self):
        if not self.ids.midLevelProviderBox.active:
            self.providerChecked = False
            return
        self.ids.primaryCarePhysicianProviderBox.active = False
        self.ids.cardiologistProviderBox.active = False
        self.ids.obgynProviderBox.active = False
        self.providerChecked = True
        self.clientProvider = "Mid-Level Provider"

    def checkOBGYNProvider(self):
        if not self.ids.obgynProviderBox.active:
            self.providerChecked = False
            return
        self.ids.primaryCarePhysicianProviderBox.active = False
        self.ids.midLevelProviderBox.active = False
        self.ids.cardiologistProviderBox.Active = False
        self.providerChecked = True
        self.clientProvider = "OB-GYN"

    def startError(self):
        self.ids.errorMessage.text = "Please fill out all sections"

    def startAgeError(self):
        self.ids.errorMessage.text = "Please enter an integer for the client's age"

    def endError(self, dt):
        self.ids.errorMessage.text = ""

    def nextPage(self):
        if self.genderChecked and self.referralSourceChecked and self.providerChecked and self.raceChecked and self.paymentMethodChecked and self.ids.dateInput.text != "":
            try:
                CACdate = self.ids.dateInput.text
                clientAge = int(self.ids.ageInput.text)

                client.firstPageConstructor(CACdate ,self.clientGender, self.clientRace, clientAge, self.clientPaymentMethod, self.clientReferralSource, self.clientProvider)

                App.get_running_app().root.transition = NoTransition()
                App.get_running_app().root.current = "SecondScreen"
            except:
                self.startAgeError()
                Clock.schedule_once(self.endError, 3)
        else:
            self.startError()
            Clock.schedule_once(self.endError, 3)


class MainBackground(Widget):
    pass

class MainScreen(Screen):
    pass



class SecondInterface(Widget):

    symptomsChecked = False
    knownCADChecked = False
    unitChecked = False

    clientSymptoms = None
    clientKnownCAD = None
    riskFactors = {"hypertension":False,"hyperlipidemia":False,"low hdl":False,"tobacco use":False,"diabetes":False,"family hx":False,"obesity":False,"none":False}
    clientUnit = None

    def checkSymptomsYes(self):
        if not self.ids.symptomsYesBox.active:
            self.symptomsChecked = False
            return
        self.ids.symptomsNoBox.active = False
        self.symptomsChecked = True
        self.clientSymptoms = "Yes"

    def checkSymptomsNo(self):
        if not self.ids.symptomsNoBox.active:
            self.symptomsChecked = False
            return
        self.ids.symptomsYesBox.active = False
        self.symptomsChecked = True
        self.clientSymptoms = "No"

    def checkKnownCADYes(self):
        if not self.ids.knownYesBox.active:
            self.knownCADChecked = False
            return
        self.ids.knownNoBox.active = False
        self.knownCADChecked = True
        self.clientKnownCAD = "Yes"

    def checkKnownCADNo(self):
        if not self.ids.knownNoBox.active:
            self.knownCADChecked = False
            return
        self.ids.knownYesBox.active = False
        self.knownCADChecked = True
        self.clientKnownCAD = "No"

    def checkHypertension(self):
        self.riskFactors["hypertension"] = self.ids.hypertensionBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkHyperlipidemia(self):
        self.riskFactors["hyperlipidemia"] = self.ids.hyperlipidemiaBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkLowHDL(self):
        self.riskFactors["low hdl"] = self.ids.lowHDLBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkTobaccoUse(self):
        self.riskFactors["tobacco use"] = self.ids.tobaccoBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkDiabetes(self):
        self.riskFactors["diabetes"] = self.ids.diabetesBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkFamilyHx(self):
        self.riskFactors["family hx"] = self.ids.familyHxBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkObesity(self):
        self.riskFactors["obesity"] = self.ids.obesityBox.active

        self.riskFactors["none"] = False
        self.ids.noRiskBox.active = False

    def checkNone(self):
        self.riskFactors["none"] = self.ids.noRiskBox.active
        if self.ids.noRiskBox.active:
            self.ids.hypertensionBox.active = False
            self.ids.hyperlipidemiaBox.active = False
            self.ids.lowHDLBox.active = False
            self.ids.tobaccoBox.active = False
            self.ids.diabetesBox.active = False
            self.ids.familyHxBox.active = False
            self.ids.obesityBox.active = False

            self.riskFactors["hypertension"] = False
            self.riskFactors["hyperlipidemia"] = False
            self.riskFactors["low hdl"] = False
            self.riskFactors["tobacco use"] = False
            self.riskFactors["diabetes"] = False
            self.riskFactors["family hx"] = False
            self.riskFactors["obesity"] = False

    def checkMSV(self):
        if not self.ids.mSvBox.active:
            self.unitChecked = False
            return
        self.ids.dlpBox.active = False
        self.ids.ctdiBox.active = False
        self.unitChecked = True
        self.clientUnit = "mSv"

    def checkDLP(self):
        if not self.ids.dlpBox.active:
            self.unitChecked = False
            return
        self.ids.mSvBox.active = False
        self.ids.ctdiBox.active = False
        self.unitChecked = True
        self.clientUnit = "DLP"

    def checkCTDI(self):
        if not self.ids.ctdiBox.active:
            self.unitChecked = False
            return
        self.ids.dlpBox.active = False
        self.ids.mSvBox.active = False
        self.unitChecked = True
        self.clientUnit = "CTDI"

    def startError(self):
        self.ids.errorMessage.text = "Please fill out all sections"

    def startDoseError(self):
        self.ids.errorMessage.text = "Please enter an number for the client's Radiation Dose"

    def startScoreError(self):
        self.ids.errorMessage.text = "Please enter an integer for the client's CAC Score"

    def endError(self, dt):
        self.ids.errorMessage.text = ""

    def exportData(self):
        if self.symptomsChecked and self.knownCADChecked and self.ids.radiationDoseInput.text != "" and self.ids.cacInput.text != "":
            flag = False
            for x in self.riskFactors:
                if x:
                    flag = True
            if not flag:
                self.startError()
                Clock.schedule_once(self.endError, 3)
                return

            try:
                radiationDose = float(self.ids.radiationDoseInput.text)
            except:
                self.startDoseError()
                Clock.schedule_once(self.endError, 3)
                return
            try:
                CACScore = int(self.ids.cacInput.text)
            except:
                self.startScoreError()
                Clock.schedule_once(self.endError, 3)
                return

            client.secondPageConstructor(self.clientSymptoms, self.clientKnownCAD, self.riskFactors, radiationDose, CACScore)

            wb = Workbook()

            sheet = wb.add_sheet("Patient Data")
            sheet.write(0, 0, "Study Date")
            sheet.write(0, 1, client.CACdate)
            sheet.write(1, 0, "Gender")
            sheet.write(1, 1, client.gender)
            sheet.write(2, 0, "Race")
            sheet.write(2, 1, client.race)
            sheet.write(3, 0, "Age")
            sheet.write(3, 1, client.age)
            sheet.write(4, 0, "Payment Method")
            sheet.write(4, 1, client.paymentMethod)
            sheet.write(5, 0, "Referral Source")
            sheet.write(5, 1, client.refferalSource)
            sheet.write(6, 0, "Referring Provider")
            sheet.write(6, 1, client.refferingProvider)
            sheet.write(7, 0, "CAD Symptoms")
            sheet.write(7, 1, client.CADSymptoms)
            sheet.write(8, 0, "Known CAD")
            sheet.write(8, 1, client.knownCAD)
            sheet.write(9, 0, "CAD Risk Factors")
            sheet.write(9, 1, str(client.riskFactors))
            sheet.write(10, 0, "Radiation Dose")
            sheet.write(10, 1, client.radiationDose)
            sheet.write(11, 0, "CAC Score")
            sheet.write(11, 1, client.CACScore)
            sheet.write(12, 0, "Risk Category")
            if client.CACScore == 0:
                sheet.write(12, 1, "No Disease")
            elif client.CACScore < 100:
                sheet.write(12, 1, "Early Stage Disease")
            elif client.CACScore < 400:
                sheet.write(12, 1, "Moderate Disease")
            elif client.CACScore < 1000:
                sheet.write(12, 1, "Likely Obstuctrive Disease")
            else:
                sheet.write(12, 1, "Critical Finding")

            client.path = "Patient-CAC-Scores/" + client.CACdate.replace('/','-') + ".xls"
            wb.save(client.path)

            lastScreen = App.get_running_app().root.get_screen("ThirdScreen").ids.background.ids.interface

            lastScreen.ids.pathLabel.text = "Your patient's data has been analyzed and stored here: " + client.path

            App.get_running_app().root.current = "ThirdScreen"

        else:
            self.startError()
            Clock.schedule_once(self.endError, 3)

class SecondBackground(Widget):
    pass

class SecondScreen(Screen):
    pass



class ThirdInterface(Widget):
    pass

class ThirdBackground(Widget):
    pass

class ThirdScreen(Screen):
    pass



class CACapp(App):

    def build(self):
        Window.size=(950,700)
        self.icon = "favicon.png"
        self.title = "International Cardiology Consultants Calcium Scoring App"
        return Builder.load_file("Style.kv")

if __name__ == "__main__":
    CACapp().run()