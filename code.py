''' Audio Captcha '''

# Import the necessary module
from captcha.audio import AudioCaptcha

# Define properties
captcha_audio = AudioCaptcha()

# Define data
captcha_data = captcha_audio.generate('789')