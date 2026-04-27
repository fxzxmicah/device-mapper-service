# device-mapper-service

device-mapper-service provides a systemd template unit for creating
device-mapper devices from table files stored in `/etc/device-mapper`.

The package is split into two RPMs:

- `device-mapper-service` installs `device-mapper@.service` and owns
  `/etc/device-mapper`.
- `device-mapper-service-generator` installs `dm-create`, a helper that writes
  table files and starts the matching service instance.

## Table Files

Each device is described by a table file named:

```text
/etc/device-mapper/NAME.table
```

Start a configured device with:

```sh
systemctl enable --now device-mapper@NAME.service
```

Stop it with:

```sh
systemctl disable --now device-mapper@NAME.service
```

## Generating a Table

Install the generator subpackage, then run:

```sh
dm-create NAME DEV1 DEV2...
```

For example:

```sh
dm-create faststripe /dev/sdb /dev/sdc
```

`dm-create` creates `/etc/device-mapper/faststripe.table`, reloads systemd, and
starts `device-mapper@faststripe.service`.

The stripe chunk size is controlled by `CHUNK_SECTORS` and defaults to `256`
sectors:

```sh
CHUNK_SECTORS=512 dm-create faststripe /dev/sdb /dev/sdc
```

## Building

The project uses Meson only to configure and install template files:

```sh
meson setup build
meson compile -C build
meson install -C build
```
