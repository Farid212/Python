from PIL import Image

def B_and_W(path_to_img, output_img_path):
  color_img = Image.open(path_to_img)
  bw = color_img.convert('L')
  bw.save(output_img_path)

if __name__ == 'main':
  B_and_W('img.jpg', 'bw_img')