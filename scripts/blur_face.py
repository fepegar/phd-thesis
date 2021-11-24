from pathlib import Path

from PIL import Image, ImageFilter, ImageDraw



def blur_face(image, x, y, radius_blur_image, radius_face, radius_blur_image_mask):
    image2 = image.filter(ImageFilter.GaussianBlur(radius=radius_blur_image))
    image2.save('/tmp/blurry.jpg')
    mask = Image.new('L', image.size)
    draw = ImageDraw.Draw(mask)
    x0 = x - radius_face
    x1 = x + radius_face
    y0 = y - radius_face
    y1 = y + radius_face
    xy = x0, y0, x1, y1
    draw.ellipse(xy, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=radius_blur_image_mask))
    mask.save('/tmp/mask.png')
    return Image.composite(image2, image, mask)


figures_dir = Path().parent.parent / 'figures'

ssid = '030_01'
points = [
    (1600, 170),
    (435, 75),
]

radii = (
    100,
    60,
)

input_path = figures_dir / f'{ssid}.jpg'
output_path = figures_dir / f'{ssid}_blurred.jpg'
image = Image.open(input_path)
for (x, y), radius in zip(points, radii):
    radius_face = radius
    radius_blur_image = 20
    radius_blur_image_mask = 10
    image = blur_face(image, x, y, radius_blur_image, radius_face, radius_blur_image_mask)
image.save(output_path)
