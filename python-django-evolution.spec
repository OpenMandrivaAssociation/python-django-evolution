%define module	django-evolution
%define name	python-%{module}
%define version	0.6.5
%define rel		r212

Name:           %{name}
Version:        %{version}
Release:        0.svn.%{rel}
Summary:        Schema evolution for Django

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-evolution/
# svn export -%{alphatag} http://django-evolution.googlecode.com/svn/trunk/ django-evolution-%{alphatag}
# tar zcf django-evolution-%{alphatag}.tar.gz django-evolution-%{alphatag}
Source0:        %{module}-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
Requires:       python-django >= 1.1.1

%description
When you run ./manage.py syncdb, Django will look for any new models that
have been defined, and add a database table to represent those new models.
However, if you make a change to an existing model, ./manage.py syncdb will
not make any changes to the database.

This is where Django Evolution fits in. Django Evolution is an extension to
Django that allows you to track changes in your models over time, and to
update the database to reflect those changes.

%prep
%setup -q -n %{module}-%{version}

%build
%__rm -rf tests
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README docs/*


%changelog
* Wed Nov 30 2011 Lev Givon <lev@mandriva.org> 0.6.5-0.svn.r212mdv2011.0
+ Revision: 735753
- Update to 0.6.5.

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.0-1.svnr164.3mdv2011.0
+ Revision: 592234
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.0-1.svnr164.2mdv2010.0
+ Revision: 442095
- rebuild

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.0-1.svnr164.1mdv2009.1
+ Revision: 349679
- import python-django-evolution

