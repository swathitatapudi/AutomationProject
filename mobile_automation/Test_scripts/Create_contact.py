from mobile_automation.Utils import Contacts

obj=Contacts.Contacts()
#obj.swipeUp()
# for i in range(3):
obj.launchContactui()
obj.clickOnPlus()
obj.nameEntryAdb()
obj.clickOnMobile()
obj.phoneNumberEntryAdb()
obj.saveContact()
obj.pressBack2()