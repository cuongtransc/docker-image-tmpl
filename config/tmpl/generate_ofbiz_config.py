#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from __future__ import print_function
import os
from jinja2 import Template

def generate_entityengine(tmpl_file='entityengine_postgresql.tmpl',
            generated_file='entityengine.xml'):

    with open(tmpl_file) as f:
        tmpl_data = f.read()
    template = Template(tmpl_data)

    # config database
    db = dict()

    db['DB_OFBIZ_HOST'] = os.environ.get('DB_OFBIZ_HOST', 'postgres')
    db['DB_OFBIZ_PORT'] = os.environ.get('DB_OFBIZ_PORT', 5432)
    db['DB_OFBIZ_USERNAME'] = os.environ.get('DB_OFBIZ_USERNAME', 'coclab')
    db['DB_OFBIZ_PASSWORD'] = os.environ.get('DB_OFBIZ_PASSWORD', 'coclab@123')
    db['DB_OFBIZ_DATABASE'] = os.environ.get('DB_OFBIZ_DATABASE', 'coclab')

    db['DB_OLAP_HOST'] = os.environ.get('DB_OLAP_HOST', 'postgres')
    db['DB_OLAP_PORT'] = os.environ.get('DB_OLAP_PORT', 5432)
    db['DB_OLAP_USERNAME'] = os.environ.get('DB_OLAP_USERNAME', 'coclab')
    db['DB_OLAP_PASSWORD'] = os.environ.get('DB_OLAP_PASSWORD', 'coclab@123')
    db['DB_OLAP_DATABASE'] = os.environ.get('DB_OLAP_DATABASE', 'coclabolap')

    db['DB_TENANT_HOST'] = os.environ.get('DB_TENANT_HOST', 'postgres')
    db['DB_TENANT_PORT'] = os.environ.get('DB_TENANT_PORT', 5432)
    db['DB_TENANT_USERNAME'] = os.environ.get('DB_TENANT_USERNAME', 'coclab')
    db['DB_TENANT_PASSWORD'] = os.environ.get('DB_TENANT_PASSWORD', 'coclab@123')
    db['DB_TENANT_DATABASE'] = os.environ.get('DB_TENANT_DATABASE', 'coclabtenant')

    render_data = template.render(
        db=db
    )

    with open(generated_file, 'w') as f:
        f.write(render_data)


def generate_ant_build(tmpl_file='build.tmpl',
            generated_file='build.xml'):

    with open(tmpl_file) as f:
        tmpl_data = f.read()
    template = Template(tmpl_data)

    # config jvm
    config = dict()
    config['MEMORY_MAX'] = os.environ.get('MEMORY_MAX', 1024)

    render_data = template.render(
        config=config
    )

    with open(generated_file, 'w') as f:
        f.write(render_data)


if __name__ == '__main__':
    import sys

    # change directory to directory hosted current file
    os.chdir(os.path.dirname(sys.argv[0]))

    generate_entityengine()
    generate_ant_build()
