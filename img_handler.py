import os
from PIL import Image
import requests

imgs = {
    "vs":"./img/vs.png"
}

async def vs_create(url1:str, url2:str):
    vs = Image.open(os.path.join(imgs["vs"]))

    size = (150,150)

    f1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    f2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

    pos1 = (vs.width//2 - f1.width*2, vs.height//2 - f1.height//2)
    pos2 = (vs.width//2 + f2.width, vs.height//2 - f2.height//2)

    vs.paste(f1, pos1)
    vs.paste(f2, pos2)


    vs.save(os.path.join("./img", "result.png"))

