## iterm2-CUDA-VERSION

A custom component to display CUDA Version information in the status bar of iTerm2

<img width="150" alt="image" src="https://github.com/uehara-mech/iterm_status_cuda/blob/assets/assets/cuda_example.jpg">

## How to use
### Install Python Runtime
You need to install Python Runtime at first.
You can install it by clicking `Scripts > Manage > Install Python Runtime`.

### Auto-run scripts
Move `get_cuda_info.py` to `$HOME/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch`

### Configure .zshrc
Next, you need to add following lines to `.zsrhc` or `.bashrc`.
```bash
function cuda_ver() {
    nvcc -V 2>/dev/null | sed -nr "s/^(.*release)(\s*)(.*)(\,)(.+)$/\3/p"
}

function iterm2_print_user_vars() {
   iterm2_set_user_var cuda_ver $(cuda_ver)
}
```

After restarting iTerm2, you can choose the battery component in preferences: `Preferences > Profiles > Session > Status bar enabled > Configure Status Bar`.