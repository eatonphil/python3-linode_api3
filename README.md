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

#### linode.view()

```python
linode.view(linode_id=None)
```

##### Input

| Key   | Type   |
| ----- | ------ |
| jobid | number |

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