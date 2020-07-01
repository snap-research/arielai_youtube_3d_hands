import json

def load_dataset(fp_data='./data/youtube_val.json'):
    """Load the YouTube dataset.

    Args:
        fp_data: Filepath to the json file.

    Returns:
        Hand mesh dataset.
    """    
    with open(fp_data, "r") as file:
        data = json.load(file)

    return data

def retrieve_sample(data, ann_index):
    """Retrieve an annotation-image pair from the dataset.

    Args:
        data: Hand mesh dataset.
        ann_index: Annotation index.

    Returns:
        A sample from the hand mesh dataset.
    """    
    ann = data['annotations'][ann_index]
    images = data['images']
    img_idxs = [im['id'] for im in images]
    
    img = images[img_idxs.index(ann['image_id'])]
    return ann, img

def viz_sample(data, ann_index, faces=None, db_root='./data/'):
    """Visualize a sample from the dataset.

    Args:
        data: Hand mesh dataset.
        ann_index: Annotation index.
        faces: MANO faces.
        db_root: Filepath to the youtube parent directory.
    """   
    import imageio
    import matplotlib.pyplot as plt
    import numpy as np
    from os.path import join

    ann, img = retrieve_sample(data, ann_index)

    image = imageio.imread(join(db_root, img['name']))
    vertices = np.array(ann['vertices'])

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    if faces is None:
        plt.plot(vertices[:, 0], vertices[:, 1], 'o', color='green', markersize=1)
    else:
        plt.triplot(vertices[:, 0], vertices[:, 1], faces, lw=0.2)
    plt.show()

if __name__ == "__main__":
    data = load_dataset()

    print("Data keys:", [k for k in data.keys()])
    print("Image keys:", [k for k in data['images'][0].keys()])
    print("Annotations keys:", [k for k in data['annotations'][0].keys()])

    print("The number of images:", len(data['images']))
    print("The number of annotations:", len(data['annotations']))
