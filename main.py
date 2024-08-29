import streamlit as st
import whisper
import subprocess
from openai import OpenAI
from prompt import transcribe_prompt
import os
from whisper.utils import get_writer

st.title("Generate Subtitle App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# upload audio file with streamlit
with st.form("my_form"):
    upload_file = st.file_uploader("Upload Mp4 File", type=["mp4"]).name

    #################################################3
    submitted = st.form_submit_button("Submit")
    if submitted:


        model = whisper.load_model("base")

        def video2mp3(video_file, output_ext="mp3"):
            filename, ext = os.path.splitext(video_file)
            subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            return f"{filename}.{output_ext}"

        input_video = upload_file

        audio_file = video2mp3(input_video)

        def translate(audio):

            options = dict(beam_size=5, best_of=5)
            translate_options = dict(task="transcribe", **options)
            result = model.transcribe(audio_file,**translate_options)
            return result

        result = translate(audio_file)
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": transcribe_prompt},
            {"role": "user", "content": str(result)},
        ]
        )
        message = response.choices[0].message.content
        result = eval(message)
        output_dir = ''
        audio_path = audio_file.split(".")[0]
        srt = os.path.join(output_dir, audio_path + ".srt")
        writer = get_writer("srt", output_dir)
        writer(result, srt)

        subtitle = audio_path + ".vtt"
        output_video = audio_path + "_subtitled.mp4"

        st.video("sintel-short.mp4", subtitles=subtitle.name)

    
    




    # if st.sidebar.button("Transcribe Audio"):
    #     if audio_file is not None:
    #         st.sidebar.success("Transcribing Audio")
    #         transcription = model.transcribe(upload_file.name)
    #         st.sidebar.success("Transcription Complete")
    #         st.markdown(transcription["text"])
    #     else:
    #         st.sidebar.error("Please upload an audio file")


    # st.sidebar.header("Play Original Audio File")
    # st.sidebar.audio(upload_file)
