Name:		francis
Version:	25.08.1
Release:	1
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Time tracking application
URL:		https://invent.kde.org/utilities/francis
License:	GPL
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickTools)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KirigamiAddons)

%description
Time tracking application making use of the pomodoro technique

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.francis.desktop
%{_datadir}/icons/hicolor/*/apps/org.kde.francis.svg
%{_datadir}/metainfo/org.kde.francis.metainfo.xml
