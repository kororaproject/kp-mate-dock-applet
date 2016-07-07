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
BuildRequires: automake

%global debug_package %{nil} 

%description
An application dock applet for the MATE panel

%prep
%setup -q
aclocal
automake --add-missing
autoreconf

%build
%configure --with-gtk3
make %{?_smp_mflags}


%install
%make_install


%files
%doc README.md
%{_libdir}/mate-applets/mate-dock-applet/*
%{_datadir}/dbus-1/services/org.mate.panel.applet.DockAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.dock.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.DockApplet.mate-panel-applet


%changelog
* Mon Jul  7 2016 Matthew Oliver <matt@oliver.net.au> 
- Created initial spec

