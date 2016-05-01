Name:          harbour-themepack-boston
Version:       0.0.1
Release:       1
Summary:       Boston icon pack
Group:         System/Tools
Vendor:        dfstorm
Distribution:  SailfishOS
Requires:      sailfish-version >= 2.0.1, harbour-themepacksupport >= 0.0.8-1
Packager:      dfstorm <dfstorm@riseup.net>
URL:           www.genois.tk
License:       GPL

%description
Boston icon pack for Sailfish OS.

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-themepack-ivy
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
fi
fi

%changelog
* Sun Apr 30 2016 0.0.2
- First build.
