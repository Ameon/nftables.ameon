# /proj/vscode/nftables.ameon/build.py

import json
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

project_dir = Path(__file__).resolve().parent
package = json.loads((project_dir / "package.json").read_text())

name = package["name"]
publisher = package["publisher"]
version = package["version"]
extension_id = f"{publisher}.{name}"
output = project_dir / f"{extension_id}-{version}.vsix"

manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">
  <Metadata>
    <Identity Id="{escape(name)}" Version="{escape(version)}" Publisher="{escape(publisher)}" />
    <DisplayName>{escape(package["displayName"])}</DisplayName>
    <Description xml:space="preserve">{escape(package["description"])}</Description>
    <Categories>Programming Languages</Categories>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code" Version="[1.90.0,)" />
  </Installation>
  <Dependencies />
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
  </Assets>
</PackageManifest>
"""

content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json" />
  <Default Extension="xml" ContentType="application/xml" />
  <Default Extension="md" ContentType="text/markdown" />
  <Default Extension="py" ContentType="text/plain" />
  <Default Extension="txt" ContentType="text/plain" />
  <Default Extension="vsixmanifest" ContentType="text/xml" />
</Types>
"""

with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    archive.writestr("[Content_Types].xml", content_types)
    archive.writestr("extension.vsixmanifest", manifest)

    for filename in (
        "package.json",
        "language-configuration.json",
        "syntaxes/nftables.tmLanguage.json",
    ):
        archive.write(project_dir / filename, f"extension/{filename}")

print(f"Created: {output}")
