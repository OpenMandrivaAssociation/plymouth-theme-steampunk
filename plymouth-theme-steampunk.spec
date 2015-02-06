# noarch package but uses _lib macro in post scripts
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	"SteampunK Powered Linux" Plymouth theme
Name:		plymouth-theme-steampunk
Version:	3.0
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		System/Kernel and hardware
Url:		http://kde-look.org/content/show.php?content=146030
Source0:	http://sites.google.com/site/binaryinspiration/download/SPL_Plymouth.tar.gz
Requires:	plymouth
Requires(post,postun):	plymouth-scripts

%description
This package contains the "SteampunK Powered Linux" Plymouth theme.

%files
%{_datadir}/plymouth/themes/SteampunK

%post
if [ -x %{_sbindir}/plymouth-set-default-theme ]; then
    export LIB=%{_lib}
    if [ $1 -eq 1 ]; then
        %{_sbindir}/plymouth-set-default-theme --rebuild-initrd SteampunK
    else
        THEME=$(%{_sbindir}/plymouth-set-default-theme)
        if [ "$THEME" == "text" -o "$THEME" == "SteampunK" ]; then
            %{_sbindir}/plymouth-set-default-theme --rebuild-initrd SteampunK
        fi
    fi
fi

%postun
export LIB=%{_lib}
if [ $1 -eq 0 -a -x %{_sbindir}/plymouth-set-default-theme ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "SteampunK" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset --rebuild-initrd
    fi
fi

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/

cp -r SteampunK %{buildroot}%{_datadir}/plymouth/themes/
