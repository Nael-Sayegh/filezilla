import core
import os
import urllib.request
import addonHandler
import globalPluginHandler
import gui
import wx
import datetime
import scriptHandler
from logHandler import log
import config
import globalVars
import ui
addonHandler.initTranslation()
confSpecs = {
	"nbWeek": "integer(default=60)",
	"autoUpdate": "boolean(default=True)",
	"updateEveryStart": "boolean(default=False)",
}
config.conf.spec["FileZilla"] = confSpecs
time=datetime.datetime.now()
week= int(time.strftime("%W"))
baseDir = os.path.dirname(__file__) 
addon = os.path.join(baseDir, "..") 
addonInfos = addonHandler.Addon(addon).manifest
sitename="filezilla"
configSectionName="FileZilla"

def updateAvailable():
	title = _("Update of %s version %s") %(addonInfos["summary"], oversion)
	msg = _("%s version %s is available. Would you like to update now? You can view the changes by clicking on the What's New button and scrolling down to Changes.") %(addonInfos["summary"], oversion)
	updateDialog(title=title, msg=msg).ShowModal()

def installupdate():
#	global addon
	temp=os.environ.get('TEMP')
	#temp=temp.encode('UTF-8')
	file=temp + "\\filezilla_" + oversion + ".nvda-addon"
	url=f"https://module.nael-accessvision.com/addons/addons/filezilla/filezilla-{oversion}.nvda-addon"
	urllib.request.urlretrieve(url, file)
	urllib.request.urlopen("https://module.nael-accessvision.com/addons/addons/filezilla/compteur.php")
	curAddons = []
	for addon in addonHandler.getAvailableAddons():
		curAddons.append(addon)
	bundle = addonHandler.AddonBundle(file)
	prevAddon = None
	bundleName = bundle.manifest['name']
	for addon in curAddons:
		if not addon.isPendingRemove and bundleName == addon.manifest["name"]:
			prevAddon = addon
			break
	if prevAddon:
		prevAddon.requestRemove()
	addonHandler.installAddonBundle(bundle)
	os.remove(file)
	config.conf["FileZilla"]["nbWeek"] = week
	core.restart()

def verifUpdate(gesture=False):
	global oversion
	version = addonInfos["version"]
	rversion = urllib.request.urlopen("https://module.nael-accessvision.com/addons/addons/filezilla/version_filezilla.txt")
	tversion = rversion.read().decode()
	oversion=tversion.replace("\n", "")
	if version != oversion:
		wx.CallAfter(updateAvailable)
	else:
		if gesture:
			ui.message(_("No update is available."))

def Param(param,message):
	if not config.conf[configSectionName][param]:
		config.conf[configSectionName][param]= True
		ui.message(_("%s is enabled.") %(message))
	else:
		config.conf[configSectionName][param] = False
		ui.message(_("%s is disabled.") %(message))

if not globalVars.appArgs.secure and config.conf["FileZilla"]["autoUpdate"] and (config.conf["FileZilla"]["nbWeek"] != week or config.conf["FileZilla"]["updateEveryStart"]):
	verifUpdate()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@scriptHandler.script(gesture="kb:nvda+control+alt+F",description=_("""FileZilla: checks for module updates manually"""),category="FileZilla")
	def script_gestureUpdate(self, gesture):
		verifUpdate(True)
	
	@scriptHandler.script(gesture="kb:nvda+control+alt+shift+F",description=_("""FileZilla: enable/disable automatic update checking"""),category="FileZilla")
	def script_autoUpdate(self, gesture):
		Param("autoUpdate",_("Automatic update"))

class updateDialog(wx.Dialog):
	def __init__(self, parent=None, title=None, msg=None):
		super().__init__(parent, title=title)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: message to user to report a new version.
		text = sHelper.addItem(wx.StaticText(self))
		text.SetLabel(msg)
		bHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: This is a label of a button appearing
		yes = bHelper.addButton(self, wx.ID_YES, label=_("&Yes"))
		yes.Bind(wx.EVT_BUTTON, lambda evt: installupdate())
		yes.SetFocus()
		# Translators: This is a label of a button appearing
		no = bHelper.addButton(self, wx.ID_NO, label=_("&No"))
		no.Bind(wx.EVT_BUTTON, self.onNo)
		releaseNotes = bHelper.addButton(self, label=_("Wha&t's new"))
		releaseNotes.Bind(wx.EVT_BUTTON, self.onReleaseNotes)
		sHelper.addDialogDismissButtons(bHelper)
		self.EscapeId = wx.ID_NO
		mainSizer.Add(
			sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CentreOnScreen()

	def onNo(self, evt):
		config.conf[addonInfos["name"]]["nbWeek"] = week
		self.Destroy()

	def onReleaseNotes(self, evt):
		url=f"https://module.nael-accessvision.com/addons/addons/{addonInfos['name']}/doc/"
		remoteLanguage = os.listdir(os.path.join(addon, "locale"))
		localLanguage = languageHandler.getLanguage()
		localLanguage= localLanguage.split("_")[0]
		if localLanguage in remoteLanguage:
			os.startfile(url+localLanguage+"/readme.html")
		else:
			os.startfile(url+"en/readme.html")

