%define alphatag r164
%define realname django-evolution

Name:           python-django-evolution
Version:        0.0
Release:        1.svn%{alphatag}.%mkrel 1
Summary:        Schema evolution for Django

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-evolution/
# svn export -%{alphatag} http://django-evolution.googlecode.com/svn/trunk/ django-evolution-%{alphatag}
# tar zcf django-evolution-%{alphatag}.tar.gz django-evolution-%{alphatag}
Source0:        %{realname}-%{alphatag}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-django

%description
When you run ./manage.py syncdb, Django will look for any new models that
have been defined, and add a database table to represent those new models.
However, if you make a change to an existing model, ./manage.py syncdb will
not make any changes to the database.

This is where Django Evolution fits in. Django Evolution is an extension to
Django that allows you to track changes in your models over time, and to
update the database to reflect those changes.

%prep
%setup -q -n %{realname}-%{alphatag}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README docs/
%{py_puresitedir}/*
