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

External references:
* [Official API Docs: linode.boot](https://www.linode.com/api/linode/linode.boot)

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

External references:
* [Official API Docs: linode.clone](https://www.linode.com/api/linode/linode.clone)

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

External references:
* [Official API Docs: linode.create](https://www.linode.com/api/linode/linode.create)

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

External references:
* [Official API Docs: linode.delete](https://www.linode.com/api/linode/linode.delete)

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

External references:
* [Official API Docs: linode.kvmify](https://www.linode.com/api/linode/linode.kvmify)

#### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

### linode.mutate()

```python
linode.mutate(linode_id)
```

External references:
* [Official API Docs: linode.mutate](https://www.linode.com/api/linode/linode.mutate)

#### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

### linode.reboot()

```python
linode.reboot(linode_id, config_id=None)
```

External references:
* [Official API Docs: linode.reboot](https://www.linode.com/api/linode/linode.reboot)

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

External references:
* [Official API Docs: linode.resize](https://www.linode.com/api/linode/linode.resize)

#### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| plan_id   | number |

### linode.shutdown()

```python
linode.shutdown(linode_id)
```

External references:
* [Official API Docs: linode.shutdown](https://www.linode.com/api/linode/linode.shutdown)

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

External references:
* [Official API Docs: linode.update](https://www.linode.com/api/linode/linode.update)

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

External references:
* [Official API Docs: linode.list](https://www.linode.com/api/linode/linode.list)

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

External references:
* [Official API Docs: linode.config.create](https://www.linode.com/api/linode/linode.config.create)

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

External references:
* [Official API Docs: linode.config.delete](https://www.linode.com/api/linode/linode.config.delete)

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

External references:
* [Official API Docs: linode.config.update](https://www.linode.com/api/linode/linode.config.update)

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

External references:
* [Official API Docs: linode.config.list](https://www.linode.com/api/linode/linode.config.list)

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

```python
linode.disk.create(linode_id, label, kind, size, read_only=None)
```

External references:
* [Official API Docs: linode.disk.create](https://www.linode.com/api/linode/linode.disk.create)

### linode.disk.create_from_distribution()

```python
linode.disk.create_from_distribution(linode_id, distribution_id, label, size, password, sshKey=None)
```

External references:
* [Official API Docs: linode.disk.createfromdistribution](https://www.linode.com/api/linode/linode.disk.createfromdistribution)

### linode.disk.create_from_image()

```python
linode.disk.create_from_image(linode_id, image_id, label=None, size=None, password=None, sshKey=None)
```

External references:
* [Official API Docs: linode.disk.createfromimage](https://www.linode.com/api/linode/linode.disk.createfromimage)

### linode.disk.create_from_stackscript()

```python
linode.disk.create_from_stackscript(linode_id, stackscript_id, stackscript_fields, distribution_id, label, size, password, sshKey=None)
```

External references:
* [Official API Docs: linode.disk.createfromstackscript](https://www.linode.com/api/linode/linode.disk.createfromstackscript)

### linode.disk.delete()

```python
linode.disk.delete(linode_id, disk_id)
```

External references:
* [Official API Docs: linode.disk.delete](https://www.linode.com/api/linode/linode.disk.delete)

### linode.disk.duplicate()

```python
linode.disk.duplicate(linode_id, disk_id)
```

External references:
* [Official API Docs: linode.disk.duplicate](https://www.linode.com/api/linode/linode.disk.duplicate)

### linode.disk.imagize()

```python
linode.disk.imagize(linode_id, disk_id, label=None, comments=None)
```

External references:
* [Official API Docs: linode.disk.imagize](https://www.linode.com/api/linode/linode.disk.imagize)

### linode.disk.resize()

```python
linode.disk.resize(linode_id, disk_id, size)
```

External references:
* [Official API Docs: linode.disk.resize](https://www.linode.com/api/linode/linode.disk.resize)

### linode.disk.update()

```python
linode.disk.update(linode_id, disk_id, label=None, read_only=None)
```

External references:
* [Official API Docs: linode.disk.update](https://www.linode.com/api/linode/linode.disk.update)

### linode.disk.view()

```python
linode.disk.view(linode_id, disk_id=None)
```

External references:
* [Official API Docs: linode.disk.list](https://www.linode.com/api/linode/linode.disk.list)

## linode.ip

### linode.ip.addprivate()

```python
linode.ip.addprivate(linode_id)
```

External references:
* [Official API Docs: linode.ip.addprivate](https://www.linode.com/api/linode/linode.ip.addprivate)

### linode.ip.addpublic()

```python
linode.ip.addpublic(linode_id)
```

External references:
* [Official API Docs: linode.ip.addpublic](https://www.linode.com/api/linode/linode.ip.addpublic)

### linode.ip.setrdns()

```python
linode.ip.setrdns(ip_id, hostname)
```

External references:
* [Official API Docs: linode.ip.setrdns](https://www.linode.com/api/linode/linode.ip.setrdns)

### linode.ip.swap()

```python
linode.ip.swap(ip_id, ip_id_b=None, linode_id_b=None)
```

External references:
* [Official API Docs: linode.ip.swap](https://www.linode.com/api/linode/linode.ip.swap)

### linode.ip.view()

```python
linode.ip.view(linode_id, ip_id=None)
```

External references:
* [Official API Docs: linode.ip.list](https://www.linode.com/api/linode/linode.ip.list)

## linode.job

### linode.job.view()

```python
linode.job.view(linode_id, job_id=None, pending=None)
```

External references:
* [Official API Docs: linode.job.list](https://www.linode.com/api/linode/linode.job.list)

## avail

### avail.datacenters()

```python
linode.avail.datacenters()
```

External references:
* [Official API Docs: linode.avail.datacenters](https://www.linode.com/api/linode/linode.avail.datacenters)

### avail.distributions()

```python
linode.avail.distributions()
```

External references:
* [Official API Docs: linode.avail.distributions](https://www.linode.com/api/linode/linode.avail.distributions)

### avail.kernels()

```python
linode.avail.kernels()
```

External references:
* [Official API Docs: linode.avail.kernels](https://www.linode.com/api/linode/linode.avail.kernels)

### avail.linodeplans()

```python
linode.avail.linodeplans()
```

External references:
* [Official API Docs: linode.avail.linodeplans](https://www.linode.com/api/linode/linode.avail.linodeplans)

### avail.nodebalancers()

```python
linode.avail.nodebalancers()
```

External references:
* [Official API Docs: linode.avail.nodebalancers](https://www.linode.com/api/linode/linode.avail.nodebalancers)

### avail.stackscripts()

```python
linode.avail.stackscripts()
```

External references:
* [Official API Docs: linode.avail.stackscripts](https://www.linode.com/api/linode/linode.avail.stackscripts)
