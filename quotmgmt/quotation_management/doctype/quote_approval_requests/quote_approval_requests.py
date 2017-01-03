# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, time
from frappe import msgprint, _
from frappe.model.document import Document

class QuoteApprovalRequests(Document):
	def onload(self):
		frappe.msgprint(_("Loading"))
		pass
		
	#def autoname(self):
		
	def before_insert(self):
		frappe.msgprint(_("Inserting"))
		
	def validate(self):
		frappe.msgprint(_("Validating"))
		user = frappe.session.user
		if self.get("__islocal"):
			frappe.msgprint(_("Is Local"))
			self.req_by = frappe.utils.user.get_user_fullname (user);
		else:
			frappe.msgprint(_("Not Local"))
			if (self.workflow_state == "Draft" or self.workflow_state == "Returned"):
				self.req_approved_by = ""
				self.req_approval_date = ""
				self.approved_quote = ""
				self.approved_supplier = ""
				self.approved_value = ""
			elif (self.workflow_state == "Pending for Approval"):
				if (user == self.req_approver):
					if (not self.approved_quote or self.approved_quote == ""):
						frappe.throw(_("Approved Quotation is required. Please Select"), frappe.MandatoryError)
					else:
						self.req_approved_by = frappe.utils.user.get_user_fullname (user)
						self.req_approval_date = time.strftime("%d-%m-%Y")
			elif (self.workflow_state == "Approved"):
				self.req_acknowledged_by = frappe.utils.user.get_user_fullname (user)
				if (self.po_ref_no == ""):
					frappe.throw(_("PO Ref No is required. Please Enter"), frappe.MandatoryError)
				if (self.po_date == ""):
					frappe.throw(_("PO Date is required. Please enter"), frappe.MandatoryError)
			else:
				#Do Nothing
				self.req_approved_by = ""
				self.req_approval_date = ""

			#self.validate_mandatory_fields()
			#self.update_calculated_fields()
		
	def on_update(self):
		frappe.msgprint(_("Updating"))
		
	def on_submit(self):
		frappe.msgprint(_("Submiting"))
		
	def on_cancel(self):
		frappe.msgprint(_("Canceling"))
		
	def on_trash(self):
		frappe.msgprint(_("Trashing"))

