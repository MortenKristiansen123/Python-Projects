# This script checks if Hyper-V is enabled on a Windows machine and enables it if not.
# It also prompts the user to reboot the system after enabling Hyper-V.
# Remember it requires administrative privileges to run.

import subprocess
import sys


def is_hyper_v_enabled():
    check_command = (
        "Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V | Select-Object -ExpandProperty State"
    )

    try:
        result = subprocess.run(
            ["powershell.exe", "-Command", check_command],
            capture_output=True,
            text=True,
            check=True
        )
        state = result.stdout.strip()
        return state == "Enabled"
    except subprocess.CalledProcessError as e:
        print("❌ Could not check Hyper-V status:", e)
        sys.exit(1)


def enable_hyper_v():
    enable_command = (
        "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
    )

    try:
        print("🔧 Enabling Hyper-V...")
        subprocess.run(
            ["powershell.exe", "-Command", enable_command],
            check=True
        )
        print("✅ Hyper-V enabled successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Failed to enable Hyper-V:", e)
        sys.exit(1)


def ask_to_reboot():
    choice = input("🔁 Would you like to reboot now? (y/n): ").strip().lower()
    if choice == "y":
        print("🔄 Rebooting in 5 seconds...")
        subprocess.run(["shutdown", "/r", "/t", "5"])
    else:
        print(
            "ℹ️ Reboot skipped. Please restart manually later for changes to take effect.")


if __name__ == "__main__":
    print("🔍 Checking if Hyper-V is already enabled...")
    if is_hyper_v_enabled():
        print("✅ Hyper-V is already enabled. No action needed.")
    else:
        if enable_hyper_v():
            ask_to_reboot()
