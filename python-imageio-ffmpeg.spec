%global pypi_name imageio-ffmpeg

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        %mkrel 1
Group:          Development/Python
Summary:        FFMPEG wrapper for Python
License:        BSD
URL:            https://github.com/imageio/imageio-ffmpeg
Source0:        http://pypi.io/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
FFMPEG wrapper for Python.

%package -n python3-%{pypi_name}
Summary:        FFMPEG wrapper for Python 3
Group:          Development/Python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FFMPEG wrapper for Python3.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf imageio_ffmpeg.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/imageio_ffmpeg/
%{python3_sitelib}/imageio_ffmpeg-%{version}-py%{python3_version}.egg-info
