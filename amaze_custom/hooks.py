# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "amaze_custom"
app_title = "Amaze Custom"
app_publisher = "vautodesk"
app_description = "Custom script for customer and supplier primary contact"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vautodesk@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amaze_custom/css/amaze_custom.css"
# app_include_js = "/assets/amaze_custom/js/amaze_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/amaze_custom/css/amaze_custom.css"
# web_include_js = "/assets/amaze_custom/js/amaze_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amaze_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "amaze_custom.install.before_install"
# after_install = "amaze_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amaze_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }


override_doctype_class = {
	"Customer": "amaze_custom.amaze_custom.customize.ERPNextCustomer",
	"Contact": "amaze_custom.amaze_custom.customize.ERPNextContact"
}

doc_events = {
	"Supplier": {
		"after_insert": "amaze_custom.amaze_custom.customize.update_supplier_contact"
	}
}
# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"amaze_custom.tasks.all"
# 	],
# 	"daily": [
# 		"amaze_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"amaze_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"amaze_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"amaze_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "amaze_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "amaze_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "amaze_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

