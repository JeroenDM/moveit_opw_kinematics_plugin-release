%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-moveit-opw-kinematics-plugin
Version:        0.3.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS moveit_opw_kinematics_plugin package

License:        Apache2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-moveit-core
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-moveit-core
BuildRequires:  ros-noetic-moveit-resources-fanuc-moveit-config
BuildRequires:  ros-noetic-moveit-ros-planning
BuildRequires:  ros-noetic-opw-kinematics
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MoveIt kinematics plugin for industrial robots. This plugin uses an analytical
inverse kinematic library, opw_kinematics, to calculate the inverse kinematics
for industrial robots with 6 degrees of freedom, two parallel joints, and a
spherical wrist.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Sep 22 2021 Jeroen De Maeyer <jeroen.demaeyer@kuleuven.be> - 0.3.1-1
- Autogenerated by Bloom

