''' Audio Captcha '''

# Import the necessary module
from captcha.audio import AudioCaptcha

# Define properties
captcha_audio = AudioCaptcha()

# Define data
captcha_data = captcha_audio.generate('123')

# Write to the file
captcha_audio.write('123', 'captcha_sample_audio.wav')