"""Validate public EZPin release files before publication."""
import hashlib
import json
import os
import re
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
package = root / "package"
tag = os.environ.get("RELEASE_TAG", "")
if not package.exists() and not tag:
    print("Distribution repository initialized; no release package staged yet.")
    raise SystemExit(0)

manifest = json.loads((package / "ezpin-update.json").read_text())
version = manifest["version"]
assert re.fullmatch(r"\d+\.\d+\.\d+", version), "Stable release required"
assert not tag or tag == "v" + version, "Tag/version mismatch"
expected_url = f"https://github.com/iamrook/ezpin-releases/releases/download/v{version}/ezpin-{version}.zip"
assert manifest["download_url"] == expected_url, "Unexpected download destination"
archive = package / "ezpin.zip"
assert hashlib.sha256(archive.read_bytes()).hexdigest() == manifest["sha256"], "Checksum mismatch"
allowed = {"ezpin/ezpin.php", "ezpin/readme.txt", "ezpin/LICENSE", "ezpin/includes/class-admin.php", "ezpin/includes/class-plugin.php", "ezpin/includes/class-updater.php", "ezpin/assets/admin.js", "ezpin/assets/ezpin.js", "ezpin/assets/ezpin.css"}
with zipfile.ZipFile(archive) as z:
    assert set(z.namelist()) == allowed and len(z.namelist()) == len(allowed), "Unexpected archive contents"
    header = z.read("ezpin/ezpin.php").decode()
    readme = z.read("ezpin/readme.txt").decode()
    assert f"Version: {version}\n" in header and f"const VERSION = '{version}';" in header
    assert f"Stable tag: {version}\n" in readme
    assert "Update URI: https://github.com/iamrook/ezpin-releases\n" in header
assert (package / "release-notes.md").read_text().strip(), "Release notes required"
print(f"PASS: EZPin {version}: exact runtime file list, versions, public URL, and SHA-256 verified")
