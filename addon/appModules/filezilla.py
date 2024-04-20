# -*- coding: utf-8 -*-
import api
import controlTypes
import appModuleHandler
import ui
import scriptHandler
import addonHandler
import keyboardHandler
from NVDAObjects.IAccessible import IAccessible
import keyboardHandler
from logHandler import log
import globalVars

addonHandler.initTranslation()
class AppModule(appModuleHandler.AppModule):
	@scriptHandler.script(gesture="kb:control+f6",description=_("FileZilla: Switch between local and remote file lists; when not in a list, navigate to the remote file list."),category="FileZilla")
	def script_switchList(self, gesture):
		try:
			globalVars.foregroundObject.appModule.productVersion
			fo = api.getNavigatorObject()
			if fo.role == controlTypes.Role.LISTITEM:
				fo=fo.parent
			if fo.role == controlTypes.Role.LIST and fo.windowClassName == 'SysListView32' and (fo.windowControlID == -31811 or fo.windowControlID == -31813):
				log.info("vérification passée")
				goRemoteList()
			elif fo.role == controlTypes.Role.LIST and fo.windowClassName == 'SysListView32' and (fo.windowControlID == -31806 or fo.windowControlID == -31808):
				goLocalList()
			else:
				goRemoteList()
		except RuntimeError:
			ui.message(_("Unable to access the list because the FileZilla version is not detected"))
	
	@scriptHandler.script(gesture="kb:control+shift+h",description=_("FileZilla: go to the connections history button"),category="FileZilla")
	def script_clickHistory(self, gesture):
		fg = api.getForegroundObject()
		o=getChildByID(fg, ID=-31834, nb=1)
		o=getChildByID(o, ID=-31944, nb=2)
		o = getChildByID(o, ID = -31944, nb=3)
		o.setFocus()
	
	def event_NVDAObject_init(self, obj):
		if obj.role == controlTypes.Role.BUTTON and obj.windowControlID == -31944:
			obj.name = _("Connection history")
		if obj.role == controlTypes.Role.BUTTON and obj.windowControlID == -31900:
			obj.name = _("Search options")
		if obj.role == controlTypes.Role.BUTTON and obj.windowControlID == -31899:
			obj.name = _("Close the search.")
	
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == 'RICHEDIT50W' and obj.windowControlID == -31819 and obj.role == controlTypes.Role.EDITABLETEXT:
			clsList.insert(0, StatusText)

class StatusText(IAccessible):
	@scriptHandler.script(gesture="kb:tab")
	def script_nextAfterText(self, gesture):
		obj=api.getNavigatorObject()
		obj=obj.parent.parent.parent.previous
		if obj.role == controlTypes.Role.WINDOW and obj.windowClassName == 'wxWindowNR' and obj.windowControlID == -31827:
			obj=obj.firstChild.firstChild.next
		if obj.role == controlTypes.Role.WINDOW and obj.windowControlID == -31818:
			obj=obj.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.firstChild.next
		if obj.role == controlTypes.Role.WINDOW and obj.windowControlID == -31790:
			obj=obj.firstChild.firstChild.firstChild.firstChild.firstChild
		if obj.role == controlTypes.Role.EDITABLETEXT and obj.windowClassName == 'Edit' and obj.windowControlID == 1001:
			obj.setFocus()
	
	@scriptHandler.script(gesture="kb:shift+tab")
	def script_previousText(self, gesture):
		#Je récupère l'objet en avant plan
		fg = api.getForegroundObject()
		#Je parcours l'arborescence des objets pour arriver à la liste.
		o = getChildByID(fg, ID = -31832, nb=1)
		o = getChildByID(o, ID = -31832, nb=2)
		o = getChildByID(o, ID = -31943, nb=3)
		o = getChildByID(o, ID = -31943, nb=4)
		o.setFocus()
	


def getChildByID(o, ID, nb):
	o = o.firstChild
	if not o: return _(f"Not found {nb}")
	while o:
		if o.windowControlID == ID :
			break
		o = o.next
	return o

def goLocalList():
	fg=api.getForegroundObject()
	if int(globalVars.foregroundObject.appModule.productVersion.split(",")[1]) >= 67:
		log.info("Version 67")
		o=getChildByID(fg, ID=-31813, nb=1)
		o.setFocus()
	elif int(globalVars.foregroundObject.appModule.productVersion.split(",")[1]) < 65:
		o = getChildByID(fg, ID = -31828, nb=1)
		o = getChildByID(o, ID = -31828, nb=2)
		o = getChildByID(o, ID = -31827, nb=3)
		o = getChildByID(o, ID = -31827, nb=4)
		o = getChildByID(o, ID = -31817, nb=5)
		o = getChildByID(o, ID = -31817, nb=6)
		o = getChildByID(o, ID = -31816, nb=7)
		o = getChildByID(o, ID = -31816, nb=8)
		o = getChildByID(o, ID = -31815, nb=9)
		o = getChildByID(o, ID = -31815, nb=10)
		o = getChildByID(o, ID = -31812, nb=11)
		o = getChildByID(o, ID = -31812, nb=12)
		o = getChildByID(o, ID = -31810, nb=13)
		o = getChildByID(o, ID = -31810, nb=14)
		#Je vérifie si l'objet dans la liste qui indique que l'on est pas connecté est là
		o.setFocus()
	else:
		fg = api.getForegroundObject()
		o = getChildByID(fg, ID=-31828, nb=1)
		o = getChildByID(o, ID=-31828, nb=2)
		o=getChildByID(o, ID=-31827, nb=3)
		o=getChildByID(o, ID=-31827, nb=4)
		o=getChildByID(o, ID=-31818, nb=5)
		o=getChildByID(o, ID=-31818, nb=6)
		o=getChildByID(o, ID=-31817, nb=7)
		o=getChildByID(o, ID=-31817, nb=8)
		o=getChildByID(o, ID=-31816, nb=9)
		o=getChildByID(o, ID=-31816, nb=10)
		o=getChildByID(o, ID=-31813, nb=11)
		o=getChildByID(o, ID=-31813, nb=12)
		o=getChildByID(o, ID=-31811, nb=13)
		o=getChildByID(o, ID=-31811, nb=14) 
		o.setFocus()

def goRemoteList():
	fg=api.getForegroundObject()
	if int(globalVars.foregroundObject.appModule.productVersion.split(",")[1]) >= 67:
		log.info("Version 67")
		o = getChildByID(fg, ID = -31808, nb=1)
		o.setFocus()
	elif int(globalVars.foregroundObject.appModule.productVersion.split(",")[1]) < 65:
		o = getChildByID(fg, ID = -31828, nb=1)
		o = getChildByID(o, ID = -31828, nb=2)
		o = getChildByID(o, ID = -31827, nb=3)
		o = getChildByID(o, ID = -31827, nb=4)
		o = getChildByID(o, ID = -31817, nb=5)
		o = getChildByID(o, ID = -31817, nb=6)
		o = getChildByID(o, ID = -31816, nb=7)
		o = getChildByID(o, ID = -31816, nb=8)
		o = getChildByID(o, ID = -31814, nb=9)
		o = getChildByID(o, ID = -31814, nb=10)
		o = getChildByID(o, ID = -31807, nb=11)
		o = getChildByID(o, ID = -31807, nb=12)
		o = getChildByID(o, ID = -31805, nb=13)
		o = getChildByID(o, ID = -31805, nb=14)
		#Je vérifie si l'objet dans la liste qui indique que l'on est pas connecté est là
		contentList = getChildByID(o, ID = -31804, nb=15)
		if contentList:
			ui.message(_("The list of remote files cannot be found"))
		#Sinon on y place le focus
		else:
			o.setFocus()
	else:
		o = getChildByID(fg, ID = -31828, nb=1)
		o = getChildByID(o, ID = -31828, nb=2)
		o = getChildByID(o, ID = -31827, nb=3)
		o = getChildByID(o, ID = -31827, nb=4)
		o = getChildByID(o, ID = -31818, nb=5)
		o = getChildByID(o, ID = -31818, nb=6)
		o = getChildByID(o, ID = -31817, nb=7)
		o = getChildByID(o, ID = -31817, nb=8)
		o = getChildByID(o, ID = -31815, nb=9)
		o = getChildByID(o, ID = -31815, nb=10)
		o = getChildByID(o, ID = -31808, nb=11)
		o = getChildByID(o, ID = -31808, nb=12)
		o = getChildByID(o, ID = -31806, nb=13)
		o = getChildByID(o, ID = -31806, nb=14)
		contentList = o.firstChild.windowClassName
		if contentList == 'SysHeader32':
			ui.message(_("The list of remote files cannot be found."))
	#Sinon on y place le focus
		else:
			o.setFocus()
