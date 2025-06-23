Summary:	Dock for the Gnome Shell by micxgx@gmail.com
Name:		gnome-shell-extension-dash-to-dock
Version:	100
Release:	2
License:	GPL-2.0-or-later
Source0:	https://github.com/micheleg/dash-to-dock/archive/extensions.gnome.org-v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a41c595994d50e211d32dbf8ffcb1e6e
URL:		https://micheleg.github.io/dash-to-dock
BuildRequires:	gettext
BuildRequires:	sassc
BuildArch:	noarch

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications and
a faster switching between windows and desktops without having to
leave the desktop view.

%prep
%setup -q -n dash-to-dock-extensions.gnome.org-v%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/{COPYING*,README*}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk{_UA,}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING README.md
%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%{_datadir}/glib-2.0/schemas/*gschema.xml
