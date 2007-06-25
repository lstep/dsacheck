# -*- coding: latin-1 -*-
"""
Copyright (C) 2007 Adelux <contact@adelux.fr>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from deblib import deblib
from dsalib import dsalib
import sys,os,ConfigParser


default_conf ="""\
[main]
# Put here some packages names without the version
# to not be reported, separated by a ','
packages_exceptions =

"""

def main():
    conf_path = '/etc/dsacheck.conf'
    return_code = 0

    if not os.path.exists(conf_path):
        print "Configuration file not present, creating it"
        f=open(conf_path,'w')
        f.write(default_conf)
        f.close()

    conf = ConfigParser.ConfigParser()
    conf.read(conf_path)
    exceptions = conf.get('main','packages_exceptions') .split(',')

    dsaBase = dsalib.DSABase()
    dsaBase.update_base()

    p = deblib.DebPackages()

    for advisory,e in dsaBase.dsa_advisories.items():
        for package_version in e['fixedIn']:
            if p.is_installed('<'+package_version):
                package = package_version.split('_',2)[0]
                if package not in exceptions:
                    return_code = 1
                    version = p.find_package(package)
                    print '%s is an old version (%s), %s is available.' % (package,version,package_version)
    sys.exit(return_code)

if __name__ == '__main__':
    main()
