[app]
title = TikTok Downloader
package.name = tiktokdownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,kivy,kivymd,yt-dlp,openssl,urllib3,certifi,ffmpeg
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

