<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [python-linode-apiv3](#python-linode-apiv3)
  - [Example](#example)
  - [API](#api)
    - [linode](#linode)
      - [linode.boot()](#linodeboot)
        - [Input](#input)
        - [Output](#output)
      - [linode.clone()](#linodeclone)
        - [Input](#input-1)
        - [Output](#output-1)
      - [linode.create()](#linodecreate)
        - [Input](#input-2)
        - [Output](#output-2)
      - [linode.delete()](#linodedelete)
        - [Input](#input-3)
        - [Output](#output-3)
      - [linode.kvmify()](#linodekvmify)
        - [Input](#input-4)
      - [linode.mutate()](#linodemutate)
        - [Input](#input-5)
      - [linode.reboot()](#linodereboot)
        - [Input](#input-6)
        - [Output](#output-4)
      - [linode.resize()](#linoderesize)
        - [Input](#input-7)
      - [linode.shutdown()](#linodeshutdown)
        - [Input](#input-8)
        - [Output](#output-5)
      - [linode.update()](#linodeupdate)
        - [Input](#input-9)
          - [Alert](#alert)
          - [AlertOptions](#alertoptions)
          - [Backup](#backup)
          - [Ssh](#ssh)
        - [Output](#output-6)
      - [linode.view()](#linodeview)
        - [Input](#input-10)
        - [Output (list)](#output-list)
    - [linode.config](#linodeconfig)
      - [linode.config.create()](#linodeconfigcreate)
      - [linode.config.delete()](#linodeconfigdelete)
      - [linode.config.update()](#linodeconfigupdate)
      - [linode.config.view()](#linodeconfigview)
    - [linode.disk](#linodedisk)
      - [linode.disk.create()](#linodediskcreate)
      - [linode.disk.createfromdistribution()](#linodediskcreatefromdistribution)
      - [linode.disk.createfromimage()](#linodediskcreatefromimage)
      - [linode.disk.createfromstackscript()](#linodediskcreatefromstackscript)
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

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# python-linode-apiv3

This is a Linode APIv3 client for Python 3.

## Example

```python
from api import linode

for l in linode.view():
    print(l.label)
    for d in linode.disk.view(l.linodeid):
        print('\t', d.disk)
```

## API

### linode

#### linode.boot()

```python
linode.boot(linode_id, config_id=None)
```

##### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

##### Output

| Key       | Type   |
| --------- | ------ |
| jobid     | number |

#### linode.clone()

```python
linode.clone(linode_id, datacenter_id, plan_id, payment_term=None)
```

##### Input

| Key           | Type   |
| ------------- | ------ |
| linode_id     | number |
| datacenter_id | number |
| plan_id       | number |
| payment_term  | number |

##### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

#### linode.create()

```python
linode.create(datacenter_id, plan_id, payment_term=None)
```

##### Input

| Key           | Type   |
| ------------- | ------ |
| datacenter_id | number |
| plan_id       | number |
| payment_term  | number |

##### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

#### linode.delete()

```python
linode.delete(linode_id, skip_checks=None)
```

##### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |
| skip_checks   | boolean |

##### Output

| Key       | Type   |
| --------- | ------ |
| linodeid  | number |

#### linode.kvmify()

```python
linode.kvmify(linode_id)
```

##### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

#### linode.mutate()

```python
linode.mutate(linode_id)
```

##### Input

| Key           | Type    |
| ------------- | ------- |
| linode_id     | number  |

#### linode.reboot()

```python
linode.reboot(linode_id, config_id=None)
```

##### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| config_id | number |

##### Output

| Key   | Type   |
| ----- | ------ |
| jobid | number |

#### linode.resize()

```python
linode.resize(linode_id, plan_id)
```

##### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |
| plan_id   | number |

#### linode.shutdown()

```python
linode.shutdown(linode_id)
```

##### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |

##### Output

| Key   | Type   |
| ----- | ------ |
| jobid | number |

#### linode.update()

```python
linode.update(linode_id, label=None, group=None, alerts=None, backups=None, watchdog=None, ssh=None)
```

##### Input

| Key       | Type    |
| --------- | ------- |
| linode_id | number  |
| label     | string  |
| group     | string  |
| alerts    | Alert   |
| backups   | Backup  |
| watchdog  | boolean |
| ssh       | Ssh     |

###### Alert

| Key             | Type         |
| --------------- | ------------ |
| cpu             | AlertOptions |
| diskio          | AlertOptions |
| bandwidth_in    | AlertOptions |
| bandwidth_out   | AlertOptions |
| bandwidth_quota | AlertOptions |

###### AlertOptions

| Key       | Type    |
| --------- | ------- |
| enabled   | boolean |
| threshold | number  |

###### Backup

| Key     | Type   |
| ------- | ------ |
| window  | number |
| weekday | number |

###### Ssh

| Key      | Type    |
| -------- | ------- |
| disabled | boolean |
| user     | string  |
| ip       | string  |
| port     | number  |

##### Output

| Key      | Type   |
| -------- | ------ |
| linodeid | number |


#### linode.view()

```python
linode.view(linode_id=None)
```

##### Input

| Key       | Type   |
| --------- | ------ |
| linode_id | number |

##### Output (list)

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

### linode.config

#### linode.config.create()

#### linode.config.delete()

#### linode.config.update()

#### linode.config.view()

### linode.disk

#### linode.disk.create()

#### linode.disk.createfromdistribution()

#### linode.disk.createfromimage()

#### linode.disk.createfromstackscript()

#### linode.disk.delete()

#### linode.disk.duplicate()

#### linode.disk.imagize()

#### linode.disk.resize()

#### linode.disk.update()

#### linode.disk.view()

### linode.ip

#### linode.ip.addprivate()

#### linode.ip.addpublic()

#### linode.ip.setrdns()

#### linode.ip.swap()

#### linode.ip.view()

### linode.job

#### linode.job.view()