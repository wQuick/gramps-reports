#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Nick Hall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
# $Id: CensusReport.gpr.py 1899 2013-09-12 13:09:22Z vassilii $

#------------------------------------------------------------------------
#
# Census Report
#
#------------------------------------------------------------------------

register(REPORT,
         id = 'census_report',
         name = _("Census Report"),
         description =  _("Report of census events for a person."),
         version = '1.0.28',
         gramps_target_version = '5.2',
         status = STABLE, # not yet tested with python 3
         fname = 'CensusReport.py',
         authors = ["Nick Hall"],
         authors_email = ["nick__hall@hotmail.com"],
         category = CATEGORY_TEXT,
         reportclass = 'CensusReport',
         optionclass = 'CensusOptions',
         report_modes = [REPORT_MODE_GUI, REPORT_MODE_CLI]
        )
