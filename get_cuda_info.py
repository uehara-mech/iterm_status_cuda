#!/usr/bin/env python3.7

import iterm2
from iterm2 import StatusBarComponent, StatusBarRPC, run_forever


async def main(connection):
    # This is an example of using an asyncio context manager to register a custom control
    # sequence. You can send a custom control sequence by issuing this command in a
    # terminal session in iTerm2 while this script is running:
    #
    # printf "\033]1337;Custom=id=%s:%s\a" "shared-secret" "create-window"

    component = StatusBarComponent(
        short_description="cuda",
        detailed_description="Show default cuda version",
        knobs=[],
        exemplar="CUDA Ver. 9.0",
        update_cadence=1.0,
        identifier="cx.oldsea.cuda",
    )

    @StatusBarRPC
    async def cuda_version(knobs, nvcc=iterm2.Reference('user.cuda_ver?')):
        if not nvcc:
            return "CUDA UNAVAILABLE"
        else:
            try:
                ver_str = nvcc.split('release')[-1]
                ver_str = ver_str.split(',')[0].split()[0]
            except:
                return "CUDA ERROR"

            show_cuda_version = "CUDA Ver. {}".format(ver_str)
            return show_cuda_version

    await component.async_register(connection, cuda_version, timeout=None)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
run_forever(main)
