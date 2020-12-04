import cv2
import numpy as np
import os 
import mimetypes

def get_video(filepath, capture_count=1):
    images = []

    cap = cv2.VideoCapture(filepath)
    v_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # v_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # v_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # v_fps = cap.get(cv2.CAP_PROP_FPS)
    # v_duration = v_frames / v_fps

    jump_frame = int(v_frames / capture_count)

    for i in range(capture_count):
        pos = 1 + (jump_frame * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

        #print(v_frames, v_width, v_height, v_fps, v_duration)
        ret, frame = cap.read()
        if ret:
            images.append(frame)
            # cv2.imshow("frame", frame)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    cap.release()
    return images

def create_collage(image_list, thumb_size=(210,137), rowcols=(5, 5)):
    canvas_width = thumb_size[0] * rowcols[0]
    canvas_height = thumb_size[1] * rowcols[1]
    canvas = np.zeros(shape=(canvas_height, canvas_width, 3), dtype=np.uint8)
    canvas.fill(255)

    cursor = [0, 0]

    for img in image_list:
        img = cv2.resize(img, thumb_size)
        # image[y: y+h, x: x + w]
        canvas[cursor[1]:cursor[1] + thumb_size[1], cursor[0]:cursor[0] + thumb_size[0]] = img
        cursor[0] += thumb_size[0]

        if cursor[0] >= rowcols[0] * thumb_size[0]:
            cursor[1] += thumb_size[1]
            cursor[0] = 0

    return canvas 

def search_dir(dirname):
    result_file_lists = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filepath = os.path.join(dirname, filename)
        if os.path.isdir(full_filepath):
            result_file_lists.extend(search_dir(full_filepath))
        else:

            mimetype = "" if mimetypes.guess_type(full_filepath)[0] is None else mimetypes.guess_type(full_filepath)[0]

            # mimetype = mimetypes.guess_type(full_filepath)
            # if mimetype[0] is None:
            #     mimetype = ""
            # else:
            #     mimetype = mimetype[0]

            if mimetype.find("video") >= 0:
                result_file_lists.append(full_filepath)

    return result_file_lists

def my_imwrite(filename, img):
    try:
        ext = os.path.splitext(filename)[-1]
        result, buffer = cv2.imencode(ext, img)

        if result:
            with open(filename, mode="wb") as f:
                buffer.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

target = ""

filelist = search_dir(target)
for file in filelist:
    new_filename = os.path.splitext(file)[0] + ".jpg"

    images = get_video(file, 9)
    canvas = create_collage(images, rowcols=(3, 3))
    my_imwrite(new_filename, canvas)



# filepath = ""
# images = get_video(filepath, 8)
# canvas = create_collage(images, rowcols=(3,3))
# cv2.imshow("canvas", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()