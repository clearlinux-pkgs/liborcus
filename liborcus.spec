#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liborcus
Version  : 0.17.2
Release  : 33
URL      : https://dev-www.libreoffice.org/src/liborcus-0.17.2.tar.bz2
Source0  : https://dev-www.libreoffice.org/src/liborcus-0.17.2.tar.bz2
Summary  : Standalone file import filter library for spreadsheet documents.
Group    : Development/Tools
License  : MIT MPL-2.0-no-copyleft-exception
Requires: liborcus-bin = %{version}-%{release}
Requires: liborcus-lib = %{version}-%{release}
Requires: liborcus-license = %{version}-%{release}
Requires: liborcus-python = %{version}-%{release}
Requires: liborcus-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : ixion-dev
BuildRequires : pkgconfig(mdds-2.0)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(zlib)

%description
Orcus - library for processing spreadsheet documents.
=====================================================

%package bin
Summary: bin components for the liborcus package.
Group: Binaries
Requires: liborcus-license = %{version}-%{release}

%description bin
bin components for the liborcus package.


%package dev
Summary: dev components for the liborcus package.
Group: Development
Requires: liborcus-lib = %{version}-%{release}
Requires: liborcus-bin = %{version}-%{release}
Provides: liborcus-devel = %{version}-%{release}
Requires: liborcus = %{version}-%{release}

%description dev
dev components for the liborcus package.


%package lib
Summary: lib components for the liborcus package.
Group: Libraries
Requires: liborcus-license = %{version}-%{release}

%description lib
lib components for the liborcus package.


%package license
Summary: license components for the liborcus package.
Group: Default

%description license
license components for the liborcus package.


%package python
Summary: python components for the liborcus package.
Group: Default
Requires: liborcus-python3 = %{version}-%{release}

%description python
python components for the liborcus package.


%package python3
Summary: python3 components for the liborcus package.
Group: Default
Requires: python3-core

%description python3
python3 components for the liborcus package.


%prep
%setup -q -n liborcus-0.17.2
cd %{_builddir}/liborcus-0.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649830165
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-gnumeric-filter \
--disable-spreadsheet-model
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1649830165
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liborcus
cp %{_builddir}/liborcus-0.17.2/LICENSE %{buildroot}/usr/share/package-licenses/liborcus/d22157abc0fc0b4ae96380c09528e23cf77290a9
cp %{_builddir}/liborcus-0.17.2/test/json/validation/LICENSE %{buildroot}/usr/share/package-licenses/liborcus/8cdf65935c756d59ad0912cf700d908b37f739d9
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/orcus-css-dump
/usr/bin/orcus-detect
/usr/bin/orcus-json
/usr/bin/orcus-mso-encryption
/usr/bin/orcus-yaml
/usr/bin/orcus-zip-dump

%files dev
%defattr(-,root,root,-)
/usr/include/liborcus-0.17/orcus/base64.hpp
/usr/include/liborcus-0.17/orcus/cell_buffer.hpp
/usr/include/liborcus-0.17/orcus/config.hpp
/usr/include/liborcus-0.17/orcus/css_document_tree.hpp
/usr/include/liborcus-0.17/orcus/css_parser.hpp
/usr/include/liborcus-0.17/orcus/css_parser_base.hpp
/usr/include/liborcus-0.17/orcus/css_selector.hpp
/usr/include/liborcus-0.17/orcus/css_types.hpp
/usr/include/liborcus-0.17/orcus/csv_parser.hpp
/usr/include/liborcus-0.17/orcus/csv_parser_base.hpp
/usr/include/liborcus-0.17/orcus/detail/parser_token_buffer.hpp
/usr/include/liborcus-0.17/orcus/detail/thread.hpp
/usr/include/liborcus-0.17/orcus/dom_tree.hpp
/usr/include/liborcus-0.17/orcus/env.hpp
/usr/include/liborcus-0.17/orcus/exception.hpp
/usr/include/liborcus-0.17/orcus/format_detection.hpp
/usr/include/liborcus-0.17/orcus/global.hpp
/usr/include/liborcus-0.17/orcus/info.hpp
/usr/include/liborcus-0.17/orcus/interface.hpp
/usr/include/liborcus-0.17/orcus/json_document_tree.hpp
/usr/include/liborcus-0.17/orcus/json_global.hpp
/usr/include/liborcus-0.17/orcus/json_parser.hpp
/usr/include/liborcus-0.17/orcus/json_parser_base.hpp
/usr/include/liborcus-0.17/orcus/json_parser_thread.hpp
/usr/include/liborcus-0.17/orcus/json_structure_tree.hpp
/usr/include/liborcus-0.17/orcus/measurement.hpp
/usr/include/liborcus-0.17/orcus/orcus_csv.hpp
/usr/include/liborcus-0.17/orcus/orcus_gnumeric.hpp
/usr/include/liborcus-0.17/orcus/orcus_import_ods.hpp
/usr/include/liborcus-0.17/orcus/orcus_import_xlsx.hpp
/usr/include/liborcus-0.17/orcus/orcus_json.hpp
/usr/include/liborcus-0.17/orcus/orcus_ods.hpp
/usr/include/liborcus-0.17/orcus/orcus_xls_xml.hpp
/usr/include/liborcus-0.17/orcus/orcus_xlsx.hpp
/usr/include/liborcus-0.17/orcus/orcus_xml.hpp
/usr/include/liborcus-0.17/orcus/parser_base.hpp
/usr/include/liborcus-0.17/orcus/parser_global.hpp
/usr/include/liborcus-0.17/orcus/sax_ns_parser.hpp
/usr/include/liborcus-0.17/orcus/sax_parser.hpp
/usr/include/liborcus-0.17/orcus/sax_parser_base.hpp
/usr/include/liborcus-0.17/orcus/sax_token_parser.hpp
/usr/include/liborcus-0.17/orcus/sax_token_parser_thread.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/export_interface.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/import_interface.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/import_interface_pivot.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/import_interface_view.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/types.hpp
/usr/include/liborcus-0.17/orcus/spreadsheet/view_types.hpp
/usr/include/liborcus-0.17/orcus/stream.hpp
/usr/include/liborcus-0.17/orcus/string_pool.hpp
/usr/include/liborcus-0.17/orcus/threaded_json_parser.hpp
/usr/include/liborcus-0.17/orcus/threaded_sax_token_parser.hpp
/usr/include/liborcus-0.17/orcus/tokens.hpp
/usr/include/liborcus-0.17/orcus/types.hpp
/usr/include/liborcus-0.17/orcus/xml_namespace.hpp
/usr/include/liborcus-0.17/orcus/xml_structure_tree.hpp
/usr/include/liborcus-0.17/orcus/xml_writer.hpp
/usr/include/liborcus-0.17/orcus/yaml_document_tree.hpp
/usr/include/liborcus-0.17/orcus/yaml_parser.hpp
/usr/include/liborcus-0.17/orcus/yaml_parser_base.hpp
/usr/include/liborcus-0.17/orcus/zip_archive.hpp
/usr/include/liborcus-0.17/orcus/zip_archive_stream.hpp
/usr/lib64/liborcus-0.17.so
/usr/lib64/liborcus-mso-0.17.so
/usr/lib64/liborcus-parser-0.17.so
/usr/lib64/pkgconfig/liborcus-0.17.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liborcus-0.17.so.0
/usr/lib64/liborcus-0.17.so.0.0.0
/usr/lib64/liborcus-mso-0.17.so.0
/usr/lib64/liborcus-mso-0.17.so.0.0.0
/usr/lib64/liborcus-parser-0.17.so.0
/usr/lib64/liborcus-parser-0.17.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liborcus/8cdf65935c756d59ad0912cf700d908b37f739d9
/usr/share/package-licenses/liborcus/d22157abc0fc0b4ae96380c09528e23cf77290a9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
