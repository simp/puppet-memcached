Summary: Puppet Labs Memcached Module
Name: pupmod-saz-memcached
Version: 4.0.0
Release: 2
License: Apache License, 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppetlabs-stdlib >= 3.2.0
Requires: pupmod-iptables >= 4.1.0-4
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-puppetlabs-memcached-test

Prefix: /etc/puppet/environments/simp/modules

%description
A module to create Puppetlabs Saz Memcached as hosted at:
https://github.com/saz/puppet-memcached

%prep
%setup -q

%build

%install

[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/memcached

dirs='files lib manifests examples templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/memcached
done

cp Gemfile %{buildroot}/%{prefix}/memcached
cp LICENSE %{buildroot}/%{prefix}/memcached
cp README-DEVELOPER %{buildroot}/%{prefix}/memcached
cp README.md %{buildroot}/%{prefix}/memcached

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/memcached

%files
%defattr(0640,root,puppet,0750)
%{prefix}/memcached

%changelog
* Wed Jun 24 2015 - Trevor Vaughan <tvaughan@onyxpoint.com> - 4.0.0-2
- Removed the obsolete Modulefile

* Fri Feb 13 2015 - Trevor Vaughan <tvaughan@onyxpoint.com> - 4.0.0-1
- Migrated to the new 'simp' environment

* Wed May 21 2014 - Nick Markowski <nmarkowski@keywcorp.com> - 4.0.0-0
- Initial import
