#
# VoidyBootstrap 
# A theme for Pelican
# by Robert Iwancz
# www.voidynullness.net
#
# This makefile merely automates some dev stuff that I have found
# convenient to have automated, your mileage may vary.  It doesn't do
# anything earthshatteringly important.
#
BSVER=3.3.1
FA_VER=4.2.0
DEPENDDIR=depend


setup_depend: bootstrap fontawesome


# Create depend directory for dependencies
initdirs:
	[ -d $(DEPENDDIR) ] || mkdir $(DEPENDDIR)


# Download and unzip bootstrap source
bootstrap: initdirs
#	wget -O $(DEPENDDIR)/bootstrap.zip https://github.com/twbs/bootstrap/archive/v$(BSVER).zip 
	[ ! -L $(DEPENDDIR)/bootstrap ] || rm $(DEPENDDIR)/bootstrap
	cd $(DEPENDDIR) && unzip bootstrap.zip && ln -s bootstrap-$(BSVER) bootstrap 

fontawesome:
#	wget -O $(DEPENDDIR)/font-awesome.zip http://fortawesome.github.io/Font-Awesome/assets/font-awesome-$(FA_VER).zip
	[ ! -L $(DEPENDDIR)/font-awesome ] || rm $(DEPENDDIR)/font-awesome
	cd $(DEPENDDIR) && unzip font-awesome.zip && ln -s font-awesome-$(FA_VER) font-awesome

.PHONY: setup_depend initdirs bootstrap 

