import frappe
from frappe import _
from erpnext.selling.doctype.customer.customer import Customer
from frappe.contacts.doctype.contact.contact import Contact

class ERPNextCustomer(Customer):
	def create_primary_contact(self):
		if not self.customer_primary_contact and not self.lead_name:
			if self.mobile_no or self.email_id or self.contact_name:
				contact = frappe.get_doc({
					'doctype': 'Contact',
					'first_name': self.contact_name,
					'is_primary_contact': 1,
					'links': [{
						'link_doctype': self.doctype,
						'link_name': self.name
					}]
				})
				if self.email_id:
					contact.add_email(self.email_id, is_primary=True)
				if self.mobile_no:
					contact.add_phone(self.mobile_no, is_primary_mobile_no=True)
				contact.insert()
				self.db_set('customer_primary_contact', contact.name)
				self.db_set('mobile_no', self.mobile_no)
				self.db_set('email_id', self.email_id)

class ERPNextContact(Contact):
	def autoname(self):
		self.name = self.first_name

def update_supplier_contact(doc, action):
	if doc.mobile_no or doc.email_id or doc.contact_name:
		contact = frappe.get_doc({
			'doctype': 'Contact',
			'first_name': doc.contact_name,
			'is_primary_contact': 1,
			'links': [{
				'link_doctype': doc.doctype,
				'link_name': doc.name
			}]
		})
		if doc.email_id:
			contact.add_email(doc.email_id, is_primary=True)
		if doc.mobile_no:
			contact.add_phone(doc.mobile_no, is_primary_mobile_no=True)
		contact.insert()