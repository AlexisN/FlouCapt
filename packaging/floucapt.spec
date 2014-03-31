#
# spec file for package Floucapt
#

#

%define source_name floucapt
%define pkg_version 1.0

Name:       floucapt
Version:    %pkg_version
Release:    1
Summary:    Floucapt project
Source0:    %{source_name}-%{pkg_version}.tar.gz
Source1:    floucapt.service
URL:        https://github.com/AlexisN/FlouCapt/
Group:      Productivity/Networking/Web/Utilities
License:    License
BuildRoot:  %{_tmppath}/build-%{name}-%{version}
BuildArch:  noarch
BuildRequires:  python-distribute
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libsystemd-daemon)
%endif

Requires:   python-opencv
Requires:   apache2
Requires:   php5
Requires:   apache2-mod_php5
%py_requires

#For systemd
%if %suse_version > 1220
%define _unitdir /usr/lib/systemd
%else
%define _unitdir /lib/systemd
%endif

%description


%prep
%setup -q -n %{source_name}
%__sed -i 's|haarcascades/|/usr/share/OpenCV/haarcascades/|g' PictProcess/floucapt/PictureProcessing.py
%__sed -i 's|out|/srv/www/htdocs/flouCapt|g' PictProcess/floucapt/config.ini
%__sed -i 's|config.ini|/etc/floucapt/config.ini|g' PictProcess/floucapt/floucapt.py


%build
export CFLAGS="$RPM_OPT_FLAGS"
cd PictProcess
python setup.py build
cd ..

%install
cd PictProcess
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record-rpm=INSTALLED_FILES
cd ..
%if 0%{?suse_version} >= 1210
mkdir -p $RPM_BUILD_ROOT%{_unitdir}/system/
install -m 644 $RPM_SOURCE_DIR/floucapt.service $RPM_BUILD_ROOT%{_unitdir}/system/floucapt.service
%endif

install webPanel/conf/webConf.ini $RPM_BUILD_ROOT/etc/floucapt/

#mkdir -p $RPM_BUILD_ROOT/etc/apache2/conf.d/
#install -m 644 $RPM_SOURCE_DIR/floucapt.conf $RPM_BUILD_ROOT/etc/apache2/conf.d/floucapt.conf
# apache configuration
#%{__mkdir_p} $RPM_BUILD_ROOT/etc/apache2/conf.d/
#%{__install} -m 644 $RPM_SOURCE_DIR/floucapt.conf $RPM_BUILD_ROOT/etc/apache2/conf.d/floucapt.conf

#--------------webPanel----------------------------------------------------------------------------
mkdir -p -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/js/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/images/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/css/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/conf/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/css/
mkdir -p -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
mkdir -m 775 $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/pictures

install -m 644 webPanel/.htaccess $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/
install -m 644 webPanel/index.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/
install -m 644 webPanel/transition.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/
install -m 644 webPanel/data.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/
install -m 644 webPanel/js/ejs_slidein.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
install -m 644 webPanel/js/init.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
install -m 644 webPanel/js/jquery.fullPage.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
install -m 644 webPanel/js/main.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
install -m 644 webPanel/js/skel.min.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/js/
install -m 644 webPanel/css/style.css $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/css/
install -m 644 webPanel/images/error/400.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/401.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/402.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/403.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/404.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/408.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/500.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/502.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/503.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/error/504.png $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/error/
install -m 644 webPanel/images/def.jpg $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/images/
install -m 644 webPanel/admin/admin.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/config.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/data.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/identification.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/index.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/process_form.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/verif.php $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/
install -m 644 webPanel/admin/js/jquery.tools.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/js/
install -m 644 webPanel/admin/js/jquery.uniform.min.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/js/
install -m 644 webPanel/admin/js/main.js $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/js/
install -m 644 webPanel/admin/images/bg-admin.jpg $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/images/
install -m 644 webPanel/admin/images/help.gif $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/images/
install -m 644 webPanel/admin/css/index.css $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/css/
install -m 644 webPanel/admin/css/admin.css $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/css/
install -m 644 webPanel/admin/css/style.css $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/css/
install -m 644 webPanel/admin/css/uniform.css $RPM_BUILD_ROOT/srv/www/htdocs/flouCapt/admin/css/
#--------------------------------------------------------------------------------------------------


%clean
rm -rf %{buildroot}

%files -f PictProcess/INSTALLED_FILES
%defattr(-,root,root)
%doc README.md 

%attr(775, floucapt, floucapt) /etc/floucapt
%attr(664, floucapt, floucapt) %config %{_sysconfdir}/floucapt/config.ini
%attr(664, floucapt, floucapt) %config %{_sysconfdir}/floucapt/webConf.ini

%attr(-, floucapt, floucapt) /srv/www/htdocs/flouCapt

%if 0%{?suse_version} >= 1210
%{_unitdir}/system/floucapt.service
%endif


#%defattr(644,root,root,755)
#%dir /etc/apache2/conf.d
#%config(noreplace) /etc/apache2/conf.d/floucapt.conf
#%defattr(-,root,root)

#-------------------------------------webPanel-----------------------------------------------------
%dir /srv/www/htdocs/flouCapt
%dir /srv/www/htdocs/flouCapt/js
%dir /srv/www/htdocs/flouCapt/conf
%dir /srv/www/htdocs/flouCapt/css
%dir /srv/www/htdocs/flouCapt/images/error

%dir /srv/www/htdocs/flouCapt/admin
%dir /srv/www/htdocs/flouCapt/admin/js
%dir /srv/www/htdocs/flouCapt/admin/images
%dir /srv/www/htdocs/flouCapt/admin/css

%dir /srv/www/htdocs/flouCapt/pictures
/srv/www/htdocs/flouCapt/.htaccess
/srv/www/htdocs/flouCapt/index.php
/srv/www/htdocs/flouCapt/transition.php
/srv/www/htdocs/flouCapt/data.php
/srv/www/htdocs/flouCapt/js/ejs_slidein.js
/srv/www/htdocs/flouCapt/js/init.js
/srv/www/htdocs/flouCapt/js/jquery.fullPage.js
/srv/www/htdocs/flouCapt/js/main.js
/srv/www/htdocs/flouCapt/js/skel.min.js
/srv/www/htdocs/flouCapt/css/style.css
/srv/www/htdocs/flouCapt/images/error/400.png
/srv/www/htdocs/flouCapt/images/error/401.png
/srv/www/htdocs/flouCapt/images/error/402.png
/srv/www/htdocs/flouCapt/images/error/403.png
/srv/www/htdocs/flouCapt/images/error/404.png
/srv/www/htdocs/flouCapt/images/error/408.png
/srv/www/htdocs/flouCapt/images/error/500.png
/srv/www/htdocs/flouCapt/images/error/502.png
/srv/www/htdocs/flouCapt/images/error/503.png
/srv/www/htdocs/flouCapt/images/error/504.png
/srv/www/htdocs/flouCapt/images/def.jpg
/srv/www/htdocs/flouCapt/admin/admin.php
/srv/www/htdocs/flouCapt/admin/config.php
/srv/www/htdocs/flouCapt/admin/data.php
/srv/www/htdocs/flouCapt/admin/identification.php
/srv/www/htdocs/flouCapt/admin/index.php
/srv/www/htdocs/flouCapt/admin/process_form.php
/srv/www/htdocs/flouCapt/admin/verif.php
/srv/www/htdocs/flouCapt/admin/js/jquery.tools.js
/srv/www/htdocs/flouCapt/admin/js/jquery.uniform.min.js
/srv/www/htdocs/flouCapt/admin/js/main.js
/srv/www/htdocs/flouCapt/admin/images/bg-admin.jpg
/srv/www/htdocs/flouCapt/admin/css/index.css
/srv/www/htdocs/flouCapt/admin/css/admin.css
/srv/www/htdocs/flouCapt/admin/css/style.css
/srv/www/htdocs/flouCapt/admin/css/uniform.css
#--------------------------------------------------------------------------------------------------


%pre
/usr/sbin/groupadd -r floucapt >/dev/null 2>/dev/null || :
/usr/sbin/useradd -r -g floucapt -c "Floucapt owner" \
                  -s /bin/false floucapt 2> /dev/null || :
/usr/sbin/usermod -g floucapt -s /bin/false floucapt 2> /dev/null || :
/usr/bin/gpasswd -a wwwrun floucapt >/dev/null 2>/dev/null || :


%post

mkdir -p /etc/apache2/conf.d/
echo -e "<Directory /srv/www/htdocs/flouCapt>\n\
    AllowOverride all\n\
</Directory>\n" > /etc/apache2/conf.d/floucapt.conf

#systemctl restart floucapt.service
#systemctl restart apache2.service


%changelog