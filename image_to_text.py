# This file contains the core functions.

# Calculate the average of the items in iterable object
def avg(iterable):
    _sum = 0
    for i in iterable:
        _sum += i
    return _sum / len(iterable)

# Turn an image into text
# Example:
# img = cv2.imread("sample.jpeg").tolist()
# text_image = image_to_text(img)
def image_to_text(img, reverse=False):
    PATERN = "                            _.,-=+:;cba!?0123456789$W#@Ñ"
    if reverse:
        PATERN = "Ñ@#W$9876543210?!abc;:+=-,._                            "
    output = [['' for i in range(len(img[0]))] for j in range(len(img))]
    for i in range(len(output)):
        for j in range(len(output[i])):
            output[i][j] = PATERN[round(avg(img[i][j]) * (len(PATERN)-1) / 255)]
    return output

# Prints the output of image_to_text function
# Example:
# print_text_img(text_image)
def print_text_img(text):
    print('\n'.join([''.join(i) for i in text]) + '\n'*2)

# Creates output.txt and writes the output of image_to_text function in it.
# Example:
# save_to_file(text_image)
def save_to_file(text, file_path='output.txt'):
    try:
        open(file_path, 'x')
    except FileExistsError:
        pass
    with open(file_path, 'w') as f:
        f.write('\n'.join([''.join(i) for i in text]) + '\n'*2)
