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

from Client import Client



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
        client = Client()
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
    pass

class SecondBackground(Widget):
    pass

class SecondScreen(Screen):
    pass


class CACapp(App):

    def build(self):
        Window.size=(950,700)
        self.icon = "favicon.png"
        self.title = "Sense Configuration"
        return Builder.load_file("Style.kv")

if __name__ == "__main__":
    CACapp().run()