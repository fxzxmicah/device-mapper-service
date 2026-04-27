Name:           device-mapper-service
Version:        0.1.0
Release:        1%{?dist}
Summary:        Device-mapper table service

License:        MIT
URL:            https://github.com/fxzxmicah/device-mapper-service
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

Requires:       device-mapper
Requires:       systemd
Requires:       systemd-udev
Requires:       util-linux-core

%description
%{name} installs a systemd template unit for creating device-mapper devices from
table files stored in %{_sysconfdir}/device-mapper.

%package generator
Summary:        Device-mapper table configuration generator
Requires:       %{name} = %{version}-%{release}
Requires:       coreutils
Requires:       gawk
Requires:       util-linux-core

%description generator
%{name}-generator generates device-mapper table files under %{_sysconfdir}/device-mapper
and starts the matching device-mapper@.service instance.

%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dsystemdsystemunitdir=%{_unitdir}
%meson_build

%install
%meson_install

%post
%systemd_post device-mapper@.service

%preun
%systemd_preun device-mapper@.service

%postun
%systemd_postun device-mapper@.service

%files
%license LICENSE
%doc README.md
%{_unitdir}/device-mapper@.service
%dir %{_sysconfdir}/device-mapper

%files generator
%{_sbindir}/dm-create

%changelog
* Tue Apr 28 2026 Fxzx micah <48860358+fxzxmicah@users.noreply.github.com> - 0.1.0-1
- Initial package
