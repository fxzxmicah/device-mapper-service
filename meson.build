project(
  'device-mapper-service',
  version: '0.1.1',
  license: 'MIT',
  meson_version: '>= 0.60.0',
)

prefix = get_option('prefix')
bindir = join_paths(prefix, get_option('bindir'))
sbindir = join_paths(prefix, get_option('sbindir'))
sysconfdir = get_option('sysconfdir')
systemdsystemunitdir = get_option('systemdsystemunitdir')

if systemdsystemunitdir == ''
  systemdsystemunitdir = join_paths(prefix, 'lib/systemd/system')
endif

conf = configuration_data()
conf.set('bindir', bindir)
conf.set('sbindir', sbindir)
conf.set('sysconfdir', sysconfdir)

configure_file(
  input: 'data/device-mapper@.service.in',
  output: 'device-mapper@.service',
  configuration: conf,
  install: true,
  install_dir: systemdsystemunitdir,
)

configure_file(
  input: 'data/dm-create.sh.in',
  output: 'dm-create',
  configuration: conf,
  install: true,
  install_dir: get_option('sbindir'),
  install_mode: 'rwxr-xr-x',
)

install_emptydir(join_paths(sysconfdir, 'device-mapper'))
