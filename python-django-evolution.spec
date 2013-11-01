%define module	django-evolution

Name:           python-%{module}
Version:        0.6.9
Release:        1
Summary:        Schema evolution for Django

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-evolution/
# svn export -%{alphatag} http://django-evolution.googlecode.com/svn/trunk/ django-evolution-%{alphatag}
# tar zcf django-evolution-%{alphatag}.tar.gz django-evolution-%{alphatag}
Source0:        http://pypi.python.org/packages/source/d/django_evolution/django_evolution-%{version}.tar.gz

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
%setup -q -n django_evolution-%{version}

%build
%__rm -rf tests
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc AUTHORS LICENSE README docs/*

