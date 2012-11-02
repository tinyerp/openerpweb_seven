openerp.web_seven = function(instance) {

if (!instance.web.OldWidget) {
    // declare an alias for addons 6.1 (example: edi)
    instance.web.OldWidget = instance.web.Widget;

    instance.web.form.FieldOne2Many.include({
        // field one2many does not support view_type "form"
        load_views: function() {
            var modes = this.node.attrs.mode;
            var idx = !!modes ? modes.indexOf("form") : -1;
            if (idx == 0) {
                this.node.attrs.mode = modes.slice(5);
            } else if (idx > 0) {
                this.node.attrs.mode = modes.slice(0, idx - 1) + modes.slice(idx + 4);
            }
            this._super();
        },
        // fix a missing view when switching to Edit mode
        // (could be related to the issue above)
        reload_current_view: function() {
            if (this.viewmanager.views[this.viewmanager.active_view]) {
                return this._super();
            }
        }
    });
}

};
