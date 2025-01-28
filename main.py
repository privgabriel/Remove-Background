from rembg import remove
from PIL import Image

def remove_background(input_path: str, output_path: str) -> None:
    try:
        with Image.open(input_path) as img:
            img_no_bg = remove(img)
            
            img_no_bg.save(output_path)
            print(f"Imagem salva com sucesso em: {output_path}")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    input_path = ""
    output_path = ""
    
    remove_background(input_path, output_path)
