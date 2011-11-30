%define module	django-evolution
%define name	python-%{module}
%define version	0.6.5
%define rel		r212

Name:           %{name}
Version:        %{version}
Release:        %mkrel 0.svn.%{rel}
Summary:        Schema evolution for Django

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-evolution/
# svn export -%{alphatag} http://django-evolution.googlecode.com/svn/trunk/ django-evolution-%{alphatag}
# tar zcf django-evolution-%{alphatag}.tar.gz django-evolution-%{alphatag}
Source0:        %{module}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README docs/*
