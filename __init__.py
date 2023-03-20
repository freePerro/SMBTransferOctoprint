import os
import tempfile
from smbprotocol import SMBConnection
from smbprotocol import smb2

from octoprint.filemanager.storage import LocalFileStorage
from octoprint.plugin import FileManagerPlugin

class SmbTransferPlugin(FileManagerPlugin):

    def get_action_commands(self):
        return dict(transfer_smb=["python", os.path.join(os.path.dirname(os.path.realpath(__file__)), "transfer_smb.py")])

    def initialize(self):
        self._logger.info("SMB Transfer Plugin initialized.")

    def on_event(self, event, payload):
        pass

    def on_shutdown(self):
        pass

    def get_assets(self):
        return {
            "js": ["js/smbtransfer.js"],
            "less": ["less/smbtransfer.less"],
            "css": ["css/smbtransfer.min.css"],
    }

    def get_template_configs(self):
        return [
            {
                "type": "sidebar",
                "custom_bindings": True,
                "template": "smb_transfer_sidebar.jinja2",
            }
        ]


__plugin_name__ = "SMB Transfer"
__plugin_version__ = "0.1.0"
__plugin_description__ = "A plugin for OctoPrint to enable transfer of files to an SMB share."
__plugin_pythoncompat__ = ">=3.8,<4"
__plugin_implementation__ = SmbTransferPlugin()
