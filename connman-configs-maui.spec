Name:       connman-configs-maui
Summary:    Connman configuration for Maui
Version:    1
Release:    1
Group:      Development/Tools
License:    GPLv2
URL:        http://www.maui-project.org
Source2:    main.conf
Requires:   connman
Provides:   connman-configs

%description
Connman configuration for Maui and Maui derived products.


%prep


%build

%install
rm -rf %{buildroot}

install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/connman/


%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/connman/main.conf
