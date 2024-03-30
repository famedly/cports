pkgname = "famedly-openpgp-scripts"
pkgver = "20240330"
pkgrel = 0
_commit = "9aebfebda82fe5af347ff169dcebc495c3ed770d"
depends = [
    "bash",
    "chimerautils",
    "jq",
    "openpgp-ca",
    "openpgp-card-tools",
    "rusty-diceware",
    "sequoia-sq",
]
pkgdesc = "Famedly OpenPGP scripts"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "AGPL-3.0-or-later"
url = "https://github.com/famedly/openpgp-scripts"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "013fb5962a6b8c01f8f1a4bf1def942f0f68dfb4bf670f2016a187fef7588eba"


def do_install(self):
    for bin in [
        "fos-export",
        "fos-mount",
        "fos-new",
        "fos-part-id",
        "fos-partitions",
    ]:
        self.install_bin(bin)

    self.install_license("LICENSE")
