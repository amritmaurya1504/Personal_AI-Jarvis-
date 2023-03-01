from Body.Speak import Speak
import speedtest

def Internet():
    Speak("wait sir, i am calculating the speed.")
    st = speedtest.Speedtest()
    dl = st.download() * 0.000000125
    downloadSpeed = "{:.2f}".format(dl)
    up = st.upload() * 0.000000125
    uploadSpeed = "{:.2f}".format(up)
    Speak(
        f"sir we have {downloadSpeed} mb per second downloading speed and {uploadSpeed} mb per second uploading speed!")

