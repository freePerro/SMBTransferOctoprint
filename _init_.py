import os
import tempfile
from smbprotocol import SMBConnection
from smbprotocol import smb2

from octoprint.filemanager.storage import LocalFileStorage
from octoprint.plugin import FileManagerPlugin

class SMBTransferOctoprintPlugin(FileManagerPlugin):

    def get_action_commands(self):
        return dict(transfer_smb=["python", os.path.join(os.path.dirname(os.path.realpath(__file__)), "transfer_smb.py")])

    def initialize(self):
        self._logger.info("SMB Transfer Octoprint Plugin initialized.")

    def on_event(self, event, payload):
        pass

    def on_shutdown(self):
        pass

__plugin_name__ = "SMB Transfer Octoprint"
__plugin_version__ = "0.1.0"
__plugin_description__ = "A plugin for OctoPrint to enable transfer of files to an SMB share."
__plugin_pythoncompat__ = ">=3.8,<4"
__plugin_implementation__ = SMBTransferOctoprintPlugin()
