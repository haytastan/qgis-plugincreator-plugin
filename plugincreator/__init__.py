
from qgis.PyQt.QtWidgets import QAction


def classFactory(iface):
    return PluginCreatorPlugin(iface)


class PluginCreatorPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(u'Create plugin skeleton', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Plugin Creator", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        from plugincreator.plugincreatordialog import PluginCreatorDialog
        dialog = PluginCreatorDialog()
        dialog.exec_()
