$(function () {
    function SmbTransferViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];

        self.transferToSmb = function () {
            $.ajax({
                url: API_BASEURL + "plugin/smb_transfer/transfer",
                type: "POST",
                dataType: "json",
                success: function () {
                    new PNotify({
                        title: "SMB Transfer",
                        text: "File transfer started.",
                        type: "success",
                        hide: true,
                    });
                },
                error: function () {
                    new PNotify({
                        title: "SMB Transfer",
                        text: "File transfer failed.",
                        type: "error",
                        hide: true,
                    });
                },
            });
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: SmbTransferViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#sidebar_plugin_smb_transfer"],
    });
});
