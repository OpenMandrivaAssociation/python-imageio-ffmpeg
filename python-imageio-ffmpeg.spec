%global pypi_name imageio-ffmpeg

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        1
Group:          Development/Python
Summary:        FFMPEG wrapper for Python
License:        BSD
URL:            https://github.com/imageio/imageio-ffmpeg
Source0:        http://pypi.io/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildArch:      noarch

%description
FFMPEG wrapper for Python.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf imageio_ffmpeg.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
%{python_sitelib}/imageio_ffmpeg/
%{python_sitelib}/imageio_ffmpeg-%{version}-py%{python_version}.egg-info
