import subprocess


def create_vm(vm_name, memory_mb, vhd_path, switch_name):
    powershell_script = f"""
    New-VM -Name "{vm_name}" -MemoryStartupBytes {memory_mb}MB -VHDPath "{vhd_path}" -SwitchName "{switch_name}"
    """
    completed = subprocess.run(
        ["powershell", "-Command", powershell_script], capture_output=True, text=True)

    if completed.returncode == 0:
        print("VM created successfully!")
    else:
        print("Error creating VM:")
        print(completed.stderr)


# Example usage
create_vm("TestVM", 2048,
          "C:\\HyperV\\Virtual Hard Disks\\testvm.vhdx", "Default Switch")
