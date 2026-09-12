import os
import subprocess
import threading
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class TikTokApp(MDApp):

  def build(self):
    self.theme_cls.primary_palette = "Red"
    self.theme_cls.theme_style = "Dark"
    screen = MDScreen()

    screen.add_widget(
        MDLabel(
            text="TikTok Downloader",
            halign="center",
            font_style="H4",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
        )
    )

    self.url_input = MDTextField(
        hint_text="Вставьте ссылку на TikTok",
        pos_hint={"center_x": 0.5, "center_y": 0.6},
        size_hint_x=0.85,
    )
    screen.add_widget(self.url_input)

    self.btn = MDRaisedButton(
        text="СКАЧАТЬ В ГАЛЕРЕЮ",
        pos_hint={"center_x": 0.5, "center_y": 0.45},
        on_release=self.start_download,
    )
    screen.add_widget(self.btn)

    self.status = MDLabel(
        text="",
        halign="center",
        pos_hint={"center_x": 0.5, "center_y": 0.3},
        theme_text_color="Hint",
    )
    screen.add_widget(self.status)

    return screen

  def start_download(self, instance):
    url = self.url_input.text.strip()
    if not url:
      self.status.text = "Введите ссылку!"
      return

    self.status.text = "Скачивание..."
    self.btn.disabled = True
    threading.Thread(target=self.download, args=(url,)).start()

  def download(self, url):
    try:
      download_path = "/sdcard/Download"
      cmd = ["yt-dlp", "-P", download_path, url]
      res = subprocess.run(cmd, capture_output=True, text=True)

      if res.returncode == 0:
        self.update_status("Готово! Видео в Загрузках.")
      else:
        self.update_status("Ошибка скачивания.")
    except Exception as e:
      self.update_status(f"Ошибка: {e}")

  def update_status(self, msg):
    Clock.schedule_once(lambda dt: self._set_status(msg))

  def _set_status(self, msg):
    self.status.text = msg
    self.btn.disabled = False
    self.url_input.text = ""


if __name__ == "__main__":
  TikTokApp().run()
  
