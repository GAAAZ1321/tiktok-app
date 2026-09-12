import subprocess
import threading
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class TikTokApp(App):

  def build(self):
    layout = BoxLayout(
        orientation='vertical', padding=20, spacing=15
    )

    layout.add_widget(
        Label(
            text='TikTok Downloader', font_size='24sp', size_hint_y=0.2
        )
    )

    self.url_input = TextInput(
        hint_text='Вставьте ссылку на TikTok...',
        multiline=False,
        size_hint_y=0.15,
        font_size='16sp',
    )
    layout.add_widget(self.url_input)

    self.btn = Button(
        text='СКАЧАТЬ В ГАЛЕРЕЮ',
        size_hint_y=0.15,
        background_color=(0.9, 0.2, 0.2, 1),
        font_size='18sp',
    )
    self.btn.bind(on_press=self.start_download)
    layout.add_widget(self.btn)

    self.status = Label(
        text='',
        font_size='14sp',
        color=(0.7, 0.7, 0.7, 1),
        size_hint_y=0.5,
    )
    layout.add_widget(self.status)

    return layout

  def start_download(self, instance):
    url = self.url_input.text.strip()
    if not url:
      self.status.text = 'Введите ссылку!'
      return

    self.status.text = 'Скачивание...'
    self.btn.disabled = True
    threading.Thread(target=self.download, args=(url,)).start()

  def download(self, url):
    try:
      download_path = '/sdcard/Download'
      cmd = ['yt-dlp', '-P', download_path, url]
      res = subprocess.run(cmd, capture_output=True, text=True)

      if res.returncode == 0:
        self.update_status('Готово! Видео в Загрузках.')
      else:
        self.update_status('Ошибка скачивания.')
    except Exception as e:
      self.update_status(f'Ошибка: {e}')

  def update_status(self, msg):
    Clock.schedule_once(lambda dt: self._set_status(msg))

  def _set_status(self, msg):
    self.status.text = msg
    self.btn.disabled = False
    self.url_input.text = ''


if __name__ == '__main__':
  TikTokApp().run()
  
