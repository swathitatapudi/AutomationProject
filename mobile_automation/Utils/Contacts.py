
from mobile_automation.Libraries import adb_library
from mobile_automation.Libraries import ui_library
from mobile_automation.Resources import mydata
import time

obj1=adb_library.adbLibrary()
obj2=ui_library.uiLibrary()
#C:\Users\sisindri\PycharmProjects\Automation\MobileAutomation\Testscripts\launchContact1.py

class Contacts():
    def _init_(self):
        pass
    def launchContact(self):
        #obj1.launchApp("com.android.contacts/.activities.PeopleActivity")
        obj1.launchApp(mydata["contactPkname"])
        #time.sleep(2)
        # obj1.launchApp(mydata["settingsPkname"])
    def launchContactui(self):
        obj2.clickOnText("Contacts")
    def clickOnPlus(self):
        obj2.clickOnPlus()
    def clickOnPlus1(self):
        obj2.clickOnPlus1()#off2ndph
    def nameEntryAdb(self):
        obj1.nameEntryAdb()
    def clickOnMobile(self):
        obj2.clickOnMobile()
    def phoneNumberEntryAdb(self):
        obj1.phoneNumberEntryAdb()
    def saveContact(self):
        obj2.saveContact()
    def editContact(self):
        obj2.editContact()
    def editContact1(self):
        obj2.editContact1()
    def editName(self):
        obj1.editName()
    def editMoreName(self):
        obj2.editMoreName()
    def pressBack(self):
        obj1.pressBack()
    def deleteContact(self):
        obj2.deleteContact()
    def seltoBlock(self):
        obj2.seltoBlock()
    def blockContact(self):
        obj2.blockContact()
    def selContacttoUnblock(self):
        obj2.selContacttoUnblock()
    def unBlockContact(self):
        obj2.unBlockContact()
    def selForMore(self):
        obj2.selForMore()
    def swipeUp(self):
        obj1.swipeUp()
    def lockScreen(self):
        obj1.lockScreen()
    def pressBack2(self):
        obj2.pressBack2()