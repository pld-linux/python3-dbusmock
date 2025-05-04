#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Mock D-Bus objects
Summary(pl.UTF-8):	Atrapa obiektów D-Bus
Name:		python3-dbusmock
Version:	0.34.3
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-dbusmock/
Source0:	https://files.pythonhosted.org/packages/source/p/python-dbusmock/python_dbusmock-%{version}.tar.gz
# Source0-md5:	a2de46b58aa39d8337d4104493404249
URL:		https://pypi.org/project/python-dbusmock/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:45
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-dbus
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, logind, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

%description -l pl.UTF-8
Przy użyciu tej biblioteki Pythona można łatwo tworzyć obiekty atrap
na szynie D-Bus. Jest to przydatne do pisania testów oprogramowania
komunikującego się z usługami D-Bus, takimi jak upower, systemd,
logind, gnome-session itp., kiedy trudne jest (lub niemożliwe bez
uprawnień administratora) ustawienie stanu rzeczywistych usług na
oczekiwany w testach.

%prep
%setup -q -n python_dbusmock-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m unittest discover -s tests
# discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%{py3_sitescriptdir}/dbusmock
%{py3_sitescriptdir}/python_dbusmock-%{version}-py*.egg-info
