// Copyright (c) 2016, DGSOL InfoTech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quote Approval Requests', {
	refresh: function(frm) {
		var doc = frm.doc;
		var user_fields = ["req_subject"]
		frm.fields_dict['approved_quote'].get_query = function(doc) {
			return {
				filters: {
					"parent": doc.name
				}
			}
		}
		/*
		frm.fields_dict['req_approver'].get_query = function(doc) {
			return {
				filters: {
					"parent": doc.name
				}
			}
		}
		*/
		//if (!doc.req_by || doc.req_by != "") {
			//doc.req_by = frappe.user_info().fullname;
		//}
		if (!doc.workflow_state || doc.workflow_state == "Draft" || doc.workflow_state == "Returned") {
			frm.toggle_display("sb_approval_details", false);
			frm.toggle_display("sb_po_details", false);
		}
		if (doc.workflow_state == "Pending for Approval") {
			frm.toggle_display("sb_approval_details", true);
			frm.toggle_display("sb_po_details", false);
			frm.toggle_enable("sb_req_details", false);

			//frm.get_field("req_quotes").grid.grid_rows[0].columns.qtn_value.df.read_only = 1;
			frm.get_field("req_quotes").grid.toggle_enable("qtn_value", true);
		}
		if (doc.workflow_state == "Approved") {
			frm.toggle_display("sb_po_details", true);

		}

	}
});
