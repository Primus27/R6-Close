import psutil

r6_processes = ["RainbowSix_Vulkan.exe",  "RainbowSix.exe"]

# Iterate over all active processes
found = False
for process in psutil.process_iter():
    # Iterate over all potential r6 process names and kill if process active
    for r6_process in r6_processes:
        if process.name() == r6_process:
            process.kill()
            found = True
            break
    if found:
        break

