# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Patchelf(Package):
    """
    PatchELF is a small utility to modify the
    dynamic linker and RPATH of ELF executables.
    """

    homepage = "https://nixos.org/patchelf.html"
    url = "http://nixos.org/releases/patchelf/patchelf-0.8/patchelf-0.8.tar.gz"

    list_url = "http://nixos.org/releases/patchelf/"
    list_depth = 1

    version('0.10', '976539c80f28b0ac6807e93b7ec8fd6a1fb68e474f316de464b6f638095e16fd',
        url='https://github.com/gartung/patchelf/releases/download/0.10/patchelf-0.10.tar.gz')
    version('0.9', '3c265508526760f233620f35d79c79fc')
    version('0.8', '407b229e6a681ffb0e2cdd5915cb2d01')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
