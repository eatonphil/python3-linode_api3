import json
import os
import types

import requests

API_KEY = os.environ.get("LINODE_APIV3_KEY")

def module(name): return types.ModuleType(name)

def init(api_key):
    global API_KEY
    API_KEY = api_key

def format_response(d):
    formatted_response = type("", (object,), {})()
    for key, value in d.items():
        if isinstance(value, list):
            setattr(formatted_response, key.lower(), [format_response(v) for v in value])
        elif isinstance(value, dict):
            setattr(formatted_response, key.lower(), format_response(value))
        else:
            setattr(formatted_response, key.lower(), value)

    return formatted_response

def request(action, data=None):
    if not data:
        data = {}

    data.update({
        "api_key": API_KEY,
        "api_action": action,
    })

    response = requests.get("https://api.linode.com/", params=data)

    formatted_response = format_response(response.json())

    if not formatted_response.errorarray:
        return formatted_response.data

    raise Exception([vars(e) for e in formatted_response.errorarray])

linode = module("linode")

def linode_create(datacenter_id, plan_id, payment_term=None):
    data = {
        "DatacenterID": datacenter_id,
        "PlanID": plan_id
    }
    if payment_term:
        data["PaymentTerm"] = payment_term
    return request("linode.create", data)

def linode_update(linode_id, label=None, group=None, alerts=None, backups=None, watchdog=None, ssh=None):
    data = {"LinodeID": linode_id}
    if label:
        data["Label"] = label

    if group:
        data["Group"] = group

    if alerts:
        cpu = alerts.get("cpu", {})
        if cpu.get("enabled"):
            data["Alert_cpu_enabled"] = cpu.get("enabled")
        if cpu.get("threshold"):
            data["Alert_cpu_threshold"] = cpu.get("threshold")

        diskio = alerts.get("diskio", {})
        if diskio.get("enabled"):
            data["Alert_diskio_enabled"] = diskio.get("enabled")
        if diskio.get("threshold"):
            data["Alert_diskio_threshold"] = diskio.get("threshold")

        bandwidth_in = alerts.get("bandwidth_in", {})
        if bandwidth_in.get("enabled"):
            data["Alert_bwin_enabled"] = bandwidth_in.get("enabled")
        if bandwidth_in.get("threshold"):
            data["Alert_bwin_threshold"] = bandwidth_in.get("threshold")

        bandwidth_out = alerts.get("bandwidth_out", {})
        if bandwidth_out.get("enabled"):
            data["Alert_bwout_enabled"] = bandwidth_out.get("enabled")
        if bandwidth_out.get("threshold"):
            data["Alert_bwout_threshold"] = bandwidth_out.get("threshold")

        bandwidth_quota = alerts.get("bandwidth_quote", {})
        if bandwidth_quota.get("enabled"):
            data["Alert_bwquota_enabled"] = bandwidth_quota.get("enabled")
        if bandwidth_quota.get("threshold"):
            data["Alert_bwquota_threshold"] = bandwidth_quota.get("threshold")

    if backups:
        if backups.get("window"):
            data["backupWindow"] = backups.get("window")
        if backups.get("weekday"):
            data["backupWeeklyDay"] = backups.get("weekday")

    if watchdog:
        data["watchdog"] = watchdog

    if ssh:
        if ssh.get("disabled"):
            data["ms_ssh_disabled"] = ssh["disabled"]
        if ssh.get("user"):
            data["ms_ssh_user"] = ssh["user"]
        if ssh.get("ip"):
            data["ms_ssh_ip"] = ssh["ip"]
        if ssh.get("port"):
            data["ms_ssh_port"] = ssh["port"]

    return requests("linode.update", data)

def linode_clone(linode_id, datacenter_id, plan_id, payment_term=None):
    data = {
        "LinodeID": linode_id,
        "DatacenterID": datacenter_id,
        "PlanID": plan_id,
    }
    if payment_term:
        data["PaymentTerm"] = payment_term
    return request("linode.clone", data)

def linode_boot(linode_id, config_id=None):
    data = {"LinodeID": linode_id}
    if config_id:
        data["ConfigID"] = config_id
    return request("linode.boot", data)

def linode_reboot(linode_id, config_id=None):
    data = {"LinodeID": linode_id}
    if config_id:
        data["ConfigID"] = config_id
    return request("linode.reboot", data)

def linode_shutdown(linode_id):
    return request("linode.shutdown", {"LinodeID": linode_id})

def linode_view(linode_id=None):
    data = { "LinodeID": linode_id } if linode_id else None
    return request("linode.list", data)

def linode_delete(linode_id, skip_checks=False):
    return request("linode.delete", {
        "LinodeID": linode_id,
        "skipChecks": skip_checks,
    })

def linode_kvmify(linode_id):
    return request("linode.kvmify", {"LinodeID": linode_id})

def linode_mutate(linode_id):
    return request("linode.mutate", {"LinodeID": linode_id})

def linode_resize(linode_id, plan_id):
    return request("linode.resize", {
        "LinodeID": linode_id,
        "PlanID": plan_id
    })

linode.create = linode_create
linode.update = linode_update
linode.clone = linode_clone
linode.boot = linode_boot
linode.reboot = linode_reboot
linode.shutdown = linode_shutdown
linode.view = linode_view
linode.delete = linode_delete
linode.kvmify = linode_kvmify
linode.mutate = linode_mutate
linode.resize = linode_resize

linode.config = module("linode.config")

def linode_config_create(linode_id, kernel_id, label, disks, comments=None,
                         ram_limit=None, virt_mode=None, run_level=None,
                         root_device=None, helpers=None,
                         automount_devtmpfs=None, config_id=None):
    data = {
        "LinodeID": linode_id,
        "KernelID": kernel_id,
        "Label": label,
        "DiskList": ",".join([str(d) for d in disks]),
    }

    if config_id:
        data["ConfigID"] = config_id

    if comments:
        data["Comments"] = comments

    if ram_limit:
        data["RAMLimit"] = ram_limit

    if virt_mode:
        data["virt_mode"] = virt_mode

    if run_level:
        data["RunLevel"] = run_level

    if root_device:
        if root_device.get("number"):
            data["RootDeviceNum"] = root_device["number"]
        if root_device.get("custom"):
            data["RootDeviceCustom"] = root_device["custom"]
        if root_device.get("read_only") is not None:
            data["RootDeviceRO"] = root_device["read_only"]

    if helpers:
        if helpers.get("disable_update_db") is not None:
            data["helper_disableUpdateDB"] = helpers["disable_update_db"]
        if helpers.get("distro") is not None:
            data["helper_distro"] = helpers["distro"]
        if helpers.get("xen") is not None:
            data["helper_xen"] = helpers["xen"]
        if helpers.get("depmod") is not None:
            data["helper_depmod"] = helpers["depmod"]
        if helpers.get("network") is not None:
            data["helper_network"] = helpers["network"]

    if automount_devtmpfs is not None:
        data["devtmpfs_automount"] = automount_devtmpfs

    action = "linode.config.create" if not config_id else "linode.config.update"
    return request(action, data)

def linode_config_delete(linode_id, config_id):
    return request("linode.config.delete", {
        "LinodeID": linode_id,
        "ConfigID": config_id,
    })

def linode_config_update(linode_id, config_id, *args, **kwargs):
    return linode_config_create(linode_id, *args, config_id=config_id, **kwargs)

def linode_config_view(linode_id, config_id=None):
    data = {"LinodeID": linode_id}
    if config_id:
        data["ConfigID"] = config_id
    return request("linode.config.list", data)

linode.config.create = linode_config_create
linode.config.delete = linode_config_delete
linode.config.update = linode_config_update
linode.config.view = linode_config_view

linode.disk = module("linode.disk")

def linode_disk_create(linode_id, label, kind, size, read_only=None):
    data = {
        "LinodeID": linode_id,
        "Label": label,
        "Type": kind,
        "Size": size,
    }

    if read_only is not None:
        data["isReadOnly"] = read_only

    return request("linode.disk.create", data)

def linode_disk_create_from_distribution(linode_id, distribution_id, label,
                                         size, password, sshKey=None):
    data = {
        "LinodeID": linode_id,
        "DistributionId": distribution_id,
        "Label": label,
        "Size": size,
        "rootPass": password,
    }

    if sshKey:
        data["rootSSHKey"] = sshKey

    return request("linode.disk.createFromDistribution", data)

def linode_disk_create_from_image(linode_id, image_id, label=None, size=None,
                                  password=None, sshKey=None):
    data = {
        "LinodeID": linode_id,
        "ImageId": image_id,
    }

    if label:
        data["Label"] = label

    if size:
        data["Size"] = size

    if password:
        data["rootPass"] = password

    if sshKey:
        data["rootSSHKey"] = sshKey

    return request("linode.disk.createfromimage", data)

def linode_disk_create_from_stackscript(linode_id, stackscript_id,
                                        stackscript_fields, distribution_id,
                                        label, size, password, sshKey=None):
    data = {
        "LinodeID": linode_id,
        "StackscriptID": stackscript_id,
        "StackscriptUDFResponses": json.dumps(stackscript_fields),
        "DistributionId": distribution_id,
        "Label": label,
        "Size": size,
        "rootPass": password,
    }

    if sshKey:
        data["rootSSHKey"] = sshKey

    return request("linode.disk.createfromstackscript", data)

def linode_disk_delete(linode_id, disk_id):
    return request("linode.disk.delete", {
        "LinodeID": linode_id,
        "DiskID": disk_id,
    })

def linode_disk_duplicate(linode_id, disk_id):
    return request("linode.disk.duplicate", {
        "LinodeID": linode_id,
        "DiskID": disk_id,
    })

def linode_disk_imagize(linode_id, disk_id, label=None, comments=None):
    data = {
        "LinodeID": linode_id,
        "DiskID": disk_id,
    }

    if label:
        data["Label"] = label

    if comments:
        data["Description"] = comments

    return request("linode.disk.imagize", data)

def linode_disk_resize(linode_id, disk_id, size):
    return request("linode.disk.resize", {
        "LinodeID": linode_id,
        "DiskID": disk_id,
        "Size": size,
    })

def linode_disk_update(linode_id, disk_id, label=None, read_only=None):
    data ={
        "LinodeID": linode_id,
        "DiskID": disk_id,
    }

    if label:
        data["Label"] = label

    if read_only is not None:
        data["isReadOnly"] = read_only

    return request("linode.disk.resize", data)

def linode_disk_view(linode_id, disk_id=None):
    data = {"LinodeID": linode_id}
    if disk_id:
        data["DiskID"] = disk_id

    return request("linode.disk.list", data)

linode.disk.create = linode_disk_create
linode.disk.create_from_distribution = linode_disk_create_from_distribution
linode.disk.create_from_image = linode_disk_create_from_image
linode.disk.create_from_stackscript = linode_disk_create_from_stackscript
linode.disk.delete = linode_disk_delete
linode.disk.duplicate = linode_disk_duplicate
linode.disk.imagize = linode_disk_imagize
linode.disk.resize = linode_disk_resize
linode.disk.update = linode_disk_update
linode.disk.view = linode_disk_view

linode.ip = module("linode.ip")

def linode_ip_addprivate(linode_id):
    return request("linode.ip.addprivate", {
        "LinodeID": linode_id
    })

def linode_ip_addpublic(linode_id):
    return request("linode.ip.addpublic", {
        "LinodeID": linode_id
    })

def linode_ip_view(linode_id, ip_id=None):
    data = {"LinodeID": linode_id}
    if ip_id:
        data["IPAddressID"] = ip_id
    return request("linode.ip.list", data)

def linode_ip_setrdns(ip_id, hostname):
    return request("linode.ip.setrdns", {
        "IPAddressID": ip_id,
        "Hostname": hostname
    })

def linode_ip_swap(ip_id, ip_id_b=None, linode_id_b=None):
    data = {"IPAddressId": ip_id_a}
    if ip_id_b:
        data["withIPAddressID"] = ip_id_b
    elif linode_id_b:
        data["toLinodeID"] = linode_id_b
    return request("linode.ip.swap", data)

linode.ip.addprivate = linode_ip_addprivate
linode.ip.addpublic = linode_ip_addpublic
linode.ip.view = linode_ip_view
linode.ip.setrdns = linode_ip_setrdns
linode.ip.swap = linode_ip_swap

linode.job = module("linode.job")

def linode_job_view(linode_id, job_id=None, pending=None):
    data = {"LinodeID": linode_id}
    if job_id:
        data["JobID"] = job_id
    if pending is not None:
        data["pendingOnly"] = pending
    return request("linode.job.list", data)

linode.job.view = linode_job_view

avail = module('avail')

def avail_datacenters():
    return request("avail.datacenters")

def avail_distributions(distribution_id=None):
    data = {"DistributionID": distribution_id} if distribution_id else {}
    return request("avail.distributions", data)

def avail_kernels(xen=None, kvm=None):
    data = {}
    if xen is not None:
        data["isXen"] = xen

    if kvm is not None:
        data["isKVM"] = kvm

    return request("avail.kernels", data)

def avail_linodeplans(plan_id=None):
    data = {"PlanID": plan_id} if plan_id else None
    return request("avail.linodeplans", data)

def avail_nodebalancers():
    return request("avail.nodebalancers")

def avail_stackscripts(distribution_id=None, vendor=None, keywords=None):
    data = {}
    if distribution_id:
        data["DistributionID"] = distribution_id

    if vendor:
        data["DistributionVendor"] = vendor

    if keywords:
        data["keywords"] = keywords

    return request("avail.stackscripts", data)

avail.datacenters = avail_datacenters
avail.distributions = avail_distributions
avail.kernels = avail_kernels
avail.linodeplans = avail_linodeplans
avail.nodebalancers = avail_nodebalancers
avail.stackscripts = avail_stackscripts
