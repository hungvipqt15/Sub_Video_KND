import streamlit as st
# from openai import OpenAI
# from prompt import translate_prompt, transcribe_prompt
import gradio as gr
import os
import sys
import subprocess
import whisper
model = whisper.load_model("medium")

def video2mp3(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    return f"{filename}.{output_ext}"



st.title("🦜🔗 Generate subtitle for video")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


with st.form("my_form"):
    # input_video = '/content/videoplayback2.mp4' ################ chỗ này cần input
    input_video = st.file_uploader("Choose a video...", type=["mp4"])
    option_font = st.selectbox(
        "which word font you want to use?",
        ("Arial", "Elephant", "Ravie","Times New Roman"),
    )

    option_size = st.selectbox(
        "which size you want to use?",
        ("15", "16", "17","18","19",20),
    )






    # temperature = st.text_input("",
    # placeholder="Temperature"
    # )
    # print(type(temperature))
    # media_type = st.text_input("",
    #     placeholder="Enter a social media type",
    # )
    # number_words = st.text_input("",
    #     placeholder="Enter number of words you want to generate",
    # )
    # input_content = st.text_input("",
    #     placeholder="Enter your input content",
    # )
    # style_content = st.text_input("",
    #     placeholder="Enter your style content",
    # )

    # prompt = template.format(input_content=input_content,style_content=style_content,number_words=number_words,social_media_type=media_type)

    # client = OpenAI(
    #     # This is the default and can be omitted
    #     api_key=openai_api_key,
    # )

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": prompt,
    #         }
    #     ],
    #     model="gpt-4o",
    #     temperature=0.5
    # )
    



    # submitted = st.form_submit_button("Submit")
    # st.write("### Answer")
    # output = chat_completion.choices[0].message.content
    # st.info(output)

    # st.write("### Number words")
    # num_words_output = len(output.split())
    # st.info(num_words_output)