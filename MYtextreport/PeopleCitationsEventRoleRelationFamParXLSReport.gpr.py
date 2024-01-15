#------------------------------------------------------------------------
#
# PeopleCitations Report
#
#------------------------------------------------------------------------

plg = newplugin()
plg.id    = 'PeopleCitationsEventRoleRelationFamParXLSReport'
plg.name  = _("People Event Fam and Parents Role Relation Excel Report")
plg.description =  _("Provides a Peoples report with citations Eventroles and Relation for Excel")
plg.version = '1.0'
plg.gramps_target_version = '5.2'
plg.status = STABLE
plg.fname = 'PeopleCitationsEventRoleRelationFamParXLSReport.py'
plg.ptype = REPORT
plg.authors = ["Uli22"]
plg.authors_email = ["hansulrich.frink@gmail.com"]
plg.category = CATEGORY_TEXT
plg.reportclass = 'PeopleCitationsEventRoleRelationParXLSReport'
plg.optionclass = 'PeopleCitationsEventRoleRelationParXLSOptions'
plg.report_modes = [REPORT_MODE_GUI, REPORT_MODE_BKI, REPORT_MODE_CLI]
plg.require_active = False
