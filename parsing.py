import os
from openai import OpenAI
import base64
import streamlit as st



client = OpenAI(
    api_key=st.secrets["openai_api_key"]
)


class elec_meter_parsing :
  

    def __init__(self) -> None:
        pass
  
    def encode_image(self,image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def parse_data_from_image(self, img_path):
    

        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": """
                            #### INSTRUCTION ####
                            You are a ocr parser for getting the electricity reading and the unit from the image.
                            you will provide an image. you have to parse the meter reading and the unit of that reading from the image.
                            meter reading unit can be kwh or kvah. you have to choose from the electric meter image.
                            Output json format :- {
                            "Electricity Reading" : float,
                            "Electricity Unit" : str}"""
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img_path}"
                }
                }
            ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "json_object"
        }
        )
        print(response.choices[0].message.content)

        return eval(response.choices[0].message.content)
    

    def main(self, image_paths):
        
        response_list =[]
        for image_path in image_paths:
            base64_path = self.encode_image(image_path)

            response = self.parse_data_from_image(base64_path)

            response["Image Name"]  = image_path[13:]
            response_list.append(response)
            os.remove(image_path)
        
        return response_list
    

obj_elec_meter_parsing = elec_meter_parsing()