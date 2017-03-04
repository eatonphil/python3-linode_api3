import os
import types

from unrequests import requests

api_key = os.environ["LINODE_APIV3_KEY"]

def module(name): return types.ModuleType(name)

def format_response(d):
    formatted_response = type("", (object,), {})()
    for key, value in d.items():
        if isinstance(value, list):
            setattr(formatted_response, key.lower(), list(map(format_response, value)))
        elif isinstance(value, dict):
            setattr(formatted_response, key.lower(), format_response(value))
        else:
            setattr(formatted_response, key.lower(), value)

    return formatted_response

def request(action, data=None):
    if not data:
        data = {}

    data.update({
        "api_key": api_key,
        "api_action": action,
    })

    response = requests.get("https://api.linode.com/", data)

    formatted_response = format_response(response.json())

    if not formatted_response.errorarray:
        return formatted_response.data

    raise formatted_response.errorarray

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

def linode_delete(linode_id):
    return request("linode.delete", {
        "LinodeID": linode_id
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

def linode_config_create(linode_id, kernel_id, label, disks):
    return request("linode.config.create", {
        "LinodeID": linode_id,
        "KernelID": kernel_id,
        "Label": label,
        "DiskList": disks.join(",")
    })

def linode_config_delete(linode_id, config_id):
    return request("linode.config.delete", {
        "LinodeID": linode_id,
        "ConfigID": config_id,
    })

linode.config.create = linode_config_create
linode.config.delete = linode_config_delete

linode.disk = module("linode.disk")

def linode_disk_create(linode_id, label, type, size):
    return request("linode.disk.create", {
        "LinodeID": linode_id,
        "Label": label,
        "Type": type,
        "Size": size,
    })

def linode_disk_view(linode_id, disk_id=None):
    data = {"LinodeID": linode_id}
    if disk_id:
        data["DiskID"] = disk_id

    return request("linode.disk.list", data)

def linode_disk_delete(linode_id, disk_id):
    return request("linode.disk.delete", {
        "LinodeID": linode_id,
        "DiskID": disk_id,
    })

linode.disk.create = linode_disk_create
linode.disk.view = linode_disk_view
linode.disk.delete = linode_disk_delete

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
