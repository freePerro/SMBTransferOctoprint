$(function () {
    function SMBTransferOctoprintViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];

        self.transferToSmb = function () {
            $.ajax({
                url: API_BASEURL + "plugin/smbtransfer_octoprint/transfer",
                type: "POST",
                dataType: "json",
                success: function () {
                    new PNotify({
                        title: "SMB Transfer Octoprint",
                        text: "File transfer started.",
                        type: "success",
                        hide: true,
                    });
                },
                error: function () {
                    new PNotify({
                        title: "SMB Transfer Octoprint",
                        text: "File transfer failed.",
                        type: "error",
                        hide: true,
                    });
                },
            });
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: SMBTransferOctoprintViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#sidebar_plugin_smbtransfer_octoprint"],
    });
});
