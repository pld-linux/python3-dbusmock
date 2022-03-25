#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Mock D-Bus objects
Summary(pl.UTF-8):	Atrapa obiektów D-Bus
Name:		python-dbusmock
Version:	0.19
Release:	4
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-dbusmock/
Source0:	https://files.pythonhosted.org/packages/source/p/python-dbusmock/python-dbusmock-%{version}.tar.gz
# Source0-md5:	565aaae672e065c9c17e7fafd1843701
URL:		https://pypi.org/project/python-dbusmock/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-dbus
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
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

%package -n python3-dbusmock
Summary:	Mock D-Bus objects
Summary(pl.UTF-8):	Atrapa obiektów D-Bus
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-dbusmock
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, logind, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

%description -n python3-dbusmock -l pl.UTF-8
Przy użyciu tej biblioteki Pythona można łatwo tworzyć obiekty atrap
na szynie D-Bus. Jest to przydatne do pisania testów oprogramowania
komunikującego się z usługami D-Bus, takimi jak upower, systemd,
logind, gnome-session itp., kiedy trudne jest (lub niemożliwe bez
uprawnień administratora) ustawienie stanu rzeczywistych usług na
oczekiwany w testach.

%prep
%setup -q

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m nose tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m nose tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py_sitescriptdir}/dbusmock
%{py_sitescriptdir}/python_dbusmock-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dbusmock
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py3_sitescriptdir}/dbusmock
%{py3_sitescriptdir}/python_dbusmock-%{version}-py*.egg-info
%endif
