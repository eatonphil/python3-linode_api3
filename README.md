This is a Linode APIv3 client for Python 3.

```python
from api import linode

for l in linode.view():
    print(l.label)
    for d in linode.disk.view(l.linodeid):
        print('\t', d.disk)
```

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Modules and Functions**

- [linode](#linode)
  - [linode.boot()](#linodeboot)
  - [linode.clone()](#linodeclone)
  - [linode.create()](#linodecreate)
  - [linode.delete()](#linodedelete)
  - [linode.kvmify()](#linodekvmify)
  - [linode.mutate()](#linodemutate)
  - [linode.reboot()](#linodereboot)
  - [linode.resize()](#linoderesize)
  - [linode.shutdown()](#linodeshutdown)
  - [linode.update()](#linodeupdate)
  - [linode.view()](#linodeview)
- [linode.config](#linodeconfig)
  - [linode.config.create()](#linodeconfigcreate)
  - [linode.config.delete()](#linodeconfigdelete)
  - [linode.config.update()](#linodeconfigupdate)
  - [linode.config.view()](#linodeconfigview)
- [linode.disk](#linodedisk)
  - [linode.disk.create()](#linodediskcreate)
  - [linode.disk.create_from_distribution()](#linodediskcreate_from_distribution)
  - [linode.disk.create_from_image()](#linodediskcreate_from_image)
  - [linode.disk.create_from_stackscript()](#linodediskcreate_from_stackscript)
  - [linode.disk.delete()](#linodediskdelete)
  - [linode.disk.duplicate()](#linodediskduplicate)
  - [linode.disk.imagize()](#linodediskimagize)
  - [linode.disk.resize()](#linodediskresize)
  - [linode.disk.update()](#linodediskupdate)
  - [linode.disk.view()](#linodediskview)
- [linode.ip](#linodeip)
  - [linode.ip.addprivate()](#linodeipaddprivate)
  - [linode.ip.addpublic()](#linodeipaddpublic)
  - [linode.ip.setrdns()](#linodeipsetrdns)
  - [linode.ip.swap()](#linodeipswap)
  - [linode.ip.view()](#linodeipview)
- [linode.job](#linodejob)
  - [linode.job.view()](#linodejobview)
- [avail](#avail)
  - [avail.datacenters()](#availdatacenters)
  - [avail.distributions()](#availdistributions)
  - [avail.kernels()](#availkernels)
  - [avail.linodeplans()](#availlinodeplans)
  - [avail.nodebalancers()](#availnodebalancers)
  - [avail.stackscripts()](#availstackscripts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## linode

### linode.boot()

```python
linode.boot(linode_id, config_id=None)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

#### Output

| Key       | Type   |
| --------- | ------ |
| jobid     | number |

### linode.clone()

```python
linode.clone(linode_id, datacenter_id, plan_id, payment_term=None)
```

#### Input

| Key           | Type   |
| ------------- | ------ |
| linode_id     | number |
| datacenter_id | number |
| plan_id       | number |
| payment_term  | number |

#### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

### linode.create()

```python
linode.create(datacenter_id, plan_id, payment_term=None)
```

#### Input

| Key           | Type   |
| ------------- | ------ |
| datacenter_id | number |
| plan_id       | number |
| payment_term  | number |

#### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

### linode.delete()

```python
linode.delete(linode_id, skip_checks=None)
```

#### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |
| skip_checks   | boolean |

#### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

### linode.kvmify()

```python
linode.kvmify(linode_id)
```

#### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

### linode.mutate()

```python
linode.mutate(linode_id)
```

#### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

### linode.reboot()

```python
linode.reboot(linode_id, config_id=None)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

#### Output

| Key   | Type   |
| ----- | ------ |
| jobid | number |

### linode.resize()

```python
linode.resize(linode_id, plan_id)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| plan_id   | number |

### linode.shutdown()

```python
linode.shutdown(linode_id)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |

#### Output

| Key   | Type   |
| ----- | ------ |
| jobid | number |

### linode.update()

```python
linode.update(linode_id, label=None, group=None, alerts=None, backups=None, watchdog=None, ssh=None)
```

#### Input

| Key       | Type    |
| --------- | ------- |
| linode_id | number  |
| label     | string  |
| group     | string  |
| alerts    | Alert   |
| backups   | Backup  |
| watchdog  | boolean |
| ssh       | Ssh     |

##### Alert

| Key             | Type         |
| --------------- | ------------ |
| cpu             | AlertOptions |
| diskio          | AlertOptions |
| bandwidth_in    | AlertOptions |
| bandwidth_out   | AlertOptions |
| bandwidth_quota | AlertOptions |

##### AlertOptions

| Key       | Type    |
| --------- | ------- |
| enabled   | boolean |
| threshold | number  |

##### Backup

| Key     | Type   |
| ------- | ------ |
| window  | number |
| weekday | number |

##### Ssh

| Key      | Type    |
| -------- | ------- |
| disabled | boolean |
| user     | string  |
| ip       | string  |
| port     | number  |

#### Output

| Key      | Type   |
| -------- | ------ |
| linodeid | number |


### linode.view()

```python
linode.view(linode_id=None)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |

#### Output (list)

| Key                     | Type    |
| ----------------------- | ------  |
| alert_bwin_enabled      | boolean |
| alert_bwin_threshold    | number  |
| alert_bwout_enabled     | boolean |
| alert_bwout_threshold   | number  |
| alert_bwquota_enabled   | boolean |
| alert_bwquota_threshold | number  |
| alert_cpu_enabled       | boolean |
| alert_cpu_threshold     | number  |
| alert_diskio_enabled    | number  |
| alert_diskio_threshold  | boolean |
| backupsenabled          | boolean |
| backupweeklyday         | number  |
| backupwindow            | number  |
| create_dt               | date    |
| datacenterid            | number  |
| distributionvendor      | string  |
| iskvm                   | boolean |
| isxen                   | boolean |
| label                   | string  |
| linodeid                | number  |
| lpm_displaygroup        | string  |
| planid                  | number  |
| status                  | string  |
| totalhd                 | number  |
| totalram                | number  |
| totalxfer               | number  |
| watchdog                | boolean |

## linode.config

### linode.config.create()

```python
linode.config.create(linode_id, kernel_id, label, disks, comments=None,
                     ram_limit=None, virt_mode=None, run_level=None,
                     root_device=None, helpers=None, automount_devtmpfs=None)
```

#### Input

| Key                | Type       |
| -------------------| ---------- |
| linode_id          | number     |
| kernel_id          | number     |
| label              | string     |
| comments           | string     |
| ram_limit          | number     |
| virt_mode          | string     |
| run_level          | string     |
| root_device        | RootDevice |
| helpers            | Helpers    |
| automount_devtmpfs | boolean    |

##### RootDevice

| Key       | Type    |
| --------- | ------- |
| number    | number  |
| custom    | string  |
| read_only | boolean |

##### Helpers

| Key               | Type    |
| ----------------- | ------- |
| disable_update_db | boolean |
| distro            | boolean |
| xen               | boolean |
| depmod            | boolean |
| network           | boolean |

#### Output

| Key       | Type   |
| --------- | ------ |
| configid  | number |

### linode.config.delete()

```python
linode.delete(linode_id, config_id)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

#### Output

| Key       | Type   |
| --------- | ------ |
| configid  | number |

### linode.config.update()

```python
linode.config.update(linode_id, config_id, kernel_id, label, disks,
                     comments=None, ram_limit=None, virt_mode=None,
                     run_level=None, root_device=None, helpers=None,
                     automount_devtmpfs=None)
```

#### Input

| Key                | Type       |
| -------------------| ---------- |
| linode_id          | number     |
| config_id          | number     |
| kernel_id          | number     |
| label              | string     |
| comments           | string     |
| ram_limit          | number     |
| virt_mode          | string     |
| run_level          | string     |
| root_device        | RootDevice |
| helpers            | Helpers    |
| automount_devtmpfs | boolean    |

##### RootDevice

| Key       | Type    |
| --------- | ------- |
| number    | number  |
| custom    | string  |
| read_only | boolean |

##### Helpers

| Key               | Type    |
| ----------------- | ------- |
| disable_update_db | boolean |
| distro            | boolean |
| xen               | boolean |
| depmod            | boolean |
| network           | boolean |

#### Output

| Key       | Type   |
| --------- | ------ |
| configid  | number |

### linode.config.view()

```python
linode.config.view(linode_id, config_id=None)
```

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

#### Output (list)

| Key                    | Type          |
| ---------------------- | ------------- |
| rootdevicenum          | number        |
| rootdevicecustom       | string        |
| runlevel               | string        |
| helper_xen             | number        |
| virt_mode              | number        |
| disklist               | number (list) |
| isrescue               | boolean       |
| kernelid               | number        |
| helper_network         | number        |
| linodeid               | number        |
| comments               | string        |
| configid               | number        |
| helper_libtls          | number        |
| rootdevicero           | boolean       |
| devtmpfs_automount     | boolean       | 
| helper_disableupdatedb | number        |
| helper_depmod          | number        |
| ramlimit               | number        |
| label                  | string        |
| helper_distro          | number        |

## linode.disk

### linode.disk.create()

### linode.disk.create_from_distribution()

### linode.disk.create_from_image()

### linode.disk.create_from_stackscript()

### linode.disk.delete()

### linode.disk.duplicate()

### linode.disk.imagize()

### linode.disk.resize()

### linode.disk.update()

### linode.disk.view()

## linode.ip

### linode.ip.addprivate()

### linode.ip.addpublic()

### linode.ip.setrdns()

### linode.ip.swap()

### linode.ip.view()

## linode.job

### linode.job.view()

## avail

### avail.datacenters()

### avail.distributions()

### avail.kernels()

### avail.linodeplans()

### avail.nodebalancers()

### avail.stackscripts()