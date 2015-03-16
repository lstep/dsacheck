# General description #

dsacheck is a python program that will check all the packages on a Debian system. Dsacheck will download dynamically the DSA (Debian Security Alert) news from the security webpage and build a list that will be compared to the locally installed packages.

You can use it easily in a CRON job.

# Requirements #

  * Python 2.4+  (we're using decorators)

# How to install dsacheck #

The easiest way is to use easy\_install (from setuptools). If you don't have it on your OS (if you have it already isntalled as a package, I recommend you to remove it first), you can get it by running the following commands as root:

```
user@machine / # cd /tmp
user@machine /tmp # wget http://peak.telecommunity.com/dist/ez_setup.py
user@machine /tmp # python ez_setup.py
```

This will install a program named `easy_install` that you can run to install dsacheck :
```
user@machine /tmp # easy_install dsacheck
```

This command will connect to the [Python Cheeseshop](http://cheeseshop.python.org/pypi) and download `dsacheck` and all its dependencies (`dsalib` and `deblib`). It will then install the in your global `site-packages` directory.

That's all. You're now ready to use dsacheck!

The following script can be used to run `dsacheck` from CRON, for example in /etc/cron.daily/dsacheck:
```
#!/bin/sh
/usr/bin/dsaCheck | /usr/bin/mail -s "DSA Check Daily Run on `hostname -f`" administator@myhost.com
```