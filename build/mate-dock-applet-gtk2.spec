Name:           mate-dock-applet
Version:        0.72
Release:        1%{?dist}
Summary:        An application dock applet for the MATE panel

License:        GPLv3
URL:            https://github.com/robint99/mate-dock-applet
Source0:        %{name}-%{version}.tar.gz

BuildRequires: python3
BuildRequires: python3-scipy
BuildRequires: python3-pillow
BuildRequires: glib2-devel

%description
An application dock applet for the MATE panel

%prep
%setup -q
aclocal
automake --add-missing
autoreconf

%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc README.md
%{_libdir}/mate-applets/mate-dock-applet/*
%{_datadir}/*

%changelog

