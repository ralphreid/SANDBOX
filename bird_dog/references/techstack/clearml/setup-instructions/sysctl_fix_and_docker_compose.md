# Fixing "sysctl: unknown oid 'vm.max_map_count'" Issue on macOS

If you encounter the error message "sysctl: unknown oid 'vm.max_map_count'" while setting up ClearML on macOS, it means that the `vm.max_map_count` parameter is not recognized by the `sysctl` command on your system. You can follow the steps below to fix this issue:

1. Open a terminal window.
2. Check if the `vm.max_map_count` parameter is available on your system by running the command: `sysctl vm.max_map_count`
3. If the parameter is not found, you must manually configure it. Create a new file (e.g., `sysctl.conf`) using a text editor and add the following line to the file: `vm.max_map_count=262144`
4. Apply the changes by running the command:

```sh
  sudo mkdir  /etc/sysctl.d
  sudo cp docs/references/techstack/clearml/setup-instructions/sysctl.conf /etc/sysctl.d/99-sysctl.conf
```

6. `sudo launchctl config user path /usr/bin:/bin:/usr/sbin:/sbin` This command will reload the sysctl configuration and apply the changes.
7. After reboot, verify that the `vm.max_map_count` parameter is now recognized by running the command: `sudo sysctl -p /etc/sysctl.conf`
