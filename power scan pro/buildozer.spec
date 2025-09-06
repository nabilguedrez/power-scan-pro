[app]
title = PowerScan Pro
source.main = main.py
package.name = powerscanpro
package.domain = com.powerscan.app
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
output.dir = bin
