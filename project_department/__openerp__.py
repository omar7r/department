# -*- coding: utf-8 -*-
{
    "name": "Project Department Categorization",
    "version": "1.0",
    "author": "Camptocamp, Daniel Reis",
    "license": "AGPL-3",
    "category": "Generic Modules/Projects & Services",
    "description": """\
Add Department to Projects and task to corresponding tree, search and form
views.
""",
    "website": "http://camptocamp.com",
    "depends": [
        "analytic_base_department",
        "project",
    ],
    "data": ["project_view.xml"],
    "auto_install": True,
    "installable": True,
}
